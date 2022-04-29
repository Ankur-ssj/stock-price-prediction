from pyexpat import model
import pandas as pd
import yfinance as yahooFinance
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import load_model
import math
from sklearn.metrics import mean_squared_error
from numpy import array
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
import statsmodels.api as sm
import statsmodels.formula.api as smf
import warnings
import datetime as dt
import re
from wordcloud import WordCloud, STOPWORDS
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import snscrape.modules.twitter as sntwitter
import nltk
from sklearn.linear_model import LinearRegression
from array import *


#LSTM CODE --------------->

def infosyslstmsavedmodel():
    model = load_model("savedmodels/infosyssavedmodel.h5")
    
    GetInfosysInformation = yahooFinance.Ticker("INFY")
    df = GetInfosysInformation.history(period="5y")
    df = df[['Close']].copy()
    df1 = np.array(df)

    scaler = MinMaxScaler(feature_range=(0, 1))
    df1 = scaler.fit_transform(np.array(df1))

    training_size = int(len(df1)*0.8)
    test_size = len(df1)-training_size
    train_data, test_data = df1[0:training_size,:], df1[training_size:len(df1),:1]

    def create_dataset(dataset, time_step = 1):
        dataX, dataY = [], []
        for i in range(len(dataset)-time_step-1):
            a = dataset[i:(i+time_step), 0]
            dataX.append(a)
            dataY.append(dataset[i + time_step, 0])
        return np.array(dataX), np.array(dataY)


    time_step = 100
    X_train, y_train = create_dataset(train_data, time_step)
    X_test, y_test = create_dataset(test_data, time_step)

    #reshaping inputs
    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    #prediction and performance metrics
    train_predict = model.predict(X_train)
    test_predict = model.predict(X_test)

    #transform back to original form
    train_predict = scaler.inverse_transform(train_predict)
    test_predict = scaler.inverse_transform(test_predict)

    math.sqrt(mean_squared_error(y_train, train_predict))

    math.sqrt(mean_squared_error(y_test, test_predict)) 

    ### Plotting 
    # shift train predictions for plotting
    look_back=100
    trainPredictPlot = np.empty_like(df1)
    trainPredictPlot[:, :] = np.nan
    trainPredictPlot[look_back:len(train_predict)+look_back, :] = train_predict
    # shift test predictions for plotting
    testPredictPlot = np.empty_like(df1)
    testPredictPlot[:, :] = np.nan
    testPredictPlot[len(train_predict)+(look_back*2)+1:len(df1)-1, :] = test_predict
    # plot baseline and predictions
    plt.plot(scaler.inverse_transform(df1))
    plt.plot(trainPredictPlot)
    plt.plot(testPredictPlot)
    plt.savefig("FrontEnd/stock-price-prediction/src/static/infosysstatic/infosyslstmfinalgraph.png")

    x_input = test_data[(len(test_data) - 101): ].reshape(1, -1)

    temp_input = list(x_input)
    temp_input = temp_input[0].tolist()

    # demonstrate prediction for next 7 days
    lst_output=[]
    n_steps=100
    i=0
    while(i<7):
        
        if(len(temp_input)>30):
            #print(temp_input)
            x_input=np.array(temp_input[1:])
            #print("{} day input {}".format(i,x_input))
            x_input=x_input.reshape(1,-1)
            x_input = x_input.reshape((1, n_steps, 1))
            #print(x_input)
            yhat = model.predict(x_input, verbose=0)
            #print("{} day output {}".format(i,yhat))
            temp_input.extend(yhat[0].tolist())
            temp_input=temp_input[1:]
            #print(temp_input)
            lst_output.extend(yhat.tolist())
            i=i+1
        else:
            x_input = x_input.reshape((1, n_steps,1))
            yhat = model.predict(x_input, verbose=0)
            #print(yhat[0])
            temp_input.extend(yhat[0].tolist())
            #print(len(temp_input))
            lst_output.extend(yhat.tolist())
            i=i+1

    next_day_data = scaler.inverse_transform(lst_output)
    final_output = np.array(next_day_data)
    final_output = final_output.flatten()
    final_output_new = np.round_(final_output, decimals=3)
    intToStr = ', '.join([str(x) for x in final_output_new])
    return(intToStr)


#ARIMA CODE --------------->

def infosysarimamodel():
    GetInfosysInformation = yahooFinance.Ticker("INFY")
    df = GetInfosysInformation.history(period="5y")
    df = df[['Close']].copy()

    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(16,4))
    ax1.plot(df.Close)
    ax1.set_title("Original")
    plot_acf(df.Close, ax=ax2)
    plt.savefig("FrontEnd/stock-price-prediction/src/static/infosysstatic/infosysoriginal.png")

    diff = df.Close.diff().dropna()

    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(16, 4))

    ax1.plot(diff)
    ax1.set_title("Difference once")
    plot_acf(diff, ax=ax2)
    plt.savefig("FrontEnd/stock-price-prediction/src/static/infosysstatic/infosysacf.png")

    diff = df.Close.diff().dropna()

    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(16, 4))

    ax1.plot(diff)
    ax1.set_title("Difference once")
    plot_pacf(diff, ax=ax2)
    plt.savefig("FrontEnd/stock-price-prediction/src/static/infosysstatic/infosyspacf.png")

    warnings.filterwarnings("ignore")

    model = sm.tsa.ARIMA(df.Close, order=(5, 1, 4))
    results = model.fit()

    residuals = pd.DataFrame(results.resid)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))
    ax1.plot(residuals)
    ax2.hist(residuals, density=True)
    plt.savefig("FrontEnd/stock-price-prediction/src/static/infosysstatic/infosysresidual.png")

    step = 7

    fc = results.forecast(step)
    final_output_new = np.round_(fc, decimals=3)
    intToStr = ', '.join([str(x) for x in final_output_new])

    return intToStr



def infosyslinearregression():
    GetInfosysInformation = yahooFinance.Ticker("INFY")
    df = GetInfosysInformation.history(period="5y")
    df = df[['Close']].copy()

    # No of days to be forcasted in future
    forecast_out = int(7)
    # Price after n days
    df['Close after n days'] = df['Close'].shift(-forecast_out)
    # New df with only relevant data
    df_new = df[['Close', 'Close after n days']]

    # Structure data for train, test & forecast
    # lables of known data, discard last 35 rows
    y = np.array(df_new.iloc[:-forecast_out, -1])
    y = np.reshape(y, (-1, 1))
    # all cols of known data except lables, discard last 35 rows
    X = np.array(df_new.iloc[:-forecast_out, 0:-1])
    # Unknown, X to be forecasted
    X_to_be_forecasted = np.array(df_new.iloc[-forecast_out:, 0:-1])

    # Traning, testing to plot graphs, check accuracy
    X_train = X[0:int(0.8 * len(df)), :]
    X_test = X[int(0.8 * len(df)):, :]
    y_train = y[0:int(0.8 * len(df)), :]
    y_test = y[int(0.8 * len(df)):, :]

    # Feature Scaling===Normalization
    from sklearn.preprocessing import StandardScaler

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    X_to_be_forecasted = sc.transform(X_to_be_forecasted)

    # Training
    clf = LinearRegression(n_jobs=-1)
    clf.fit(X_train, y_train)

    # Testing
    y_test_pred = clf.predict(X_test)
    y_test_pred = y_test_pred * (1.04)

    import matplotlib.pyplot as plt2

    fig = plt2.figure(figsize=(16, 8))
    plt2.plot(y_test, label='Actual Price')
    plt2.plot(y_test_pred, label='Predicted Price')

    plt2.legend(loc=4)
    plt2.savefig("FrontEnd/stock-price-prediction/src/static/infosysstatic/infosyslr.png")
    plt2.close(fig)

    error_lr = math.sqrt(mean_squared_error(y_test, y_test_pred))
    # Forecasting
    forecast_set = clf.predict(X_to_be_forecasted)
    forecast_set = forecast_set * (1.04)
    mean = forecast_set.mean()
    lr_pred = forecast_set[0, 0]
    forecast_set = forecast_set.flatten()
    forecast_set = np.round_(forecast_set, decimals=3)
    gfg = forecast_set.tolist()
    listTostrlr = ', '.join([str(elem) for elem in gfg])

    return listTostrlr

infosyslstmsavedmodel()
infosysarimamodel()
infosyslinearregression()