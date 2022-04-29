import pandas as pd
import yfinance as yahooFinance
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import tensorflow as tf
import matplotlib.pyplot as plt

def msftsavingmodel():

    GetMicrosoftInformation = yahooFinance.Ticker("MSFT")
    df = GetMicrosoftInformation.history(period="5y")
    df = df[['Close']].copy()
    df1 = np.array(df)

    plt.plot(df1)
    plt.savefig("FrontEnd/stock-price-prediction/src/msftstatic/msftinitialdata.png")

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

    model = Sequential()
    model.add(LSTM(50, return_sequences = True, activation = 'sigmoid', input_shape=(100, 1)))
    model.add(LSTM(50, return_sequences = True))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(loss = 'mean_squared_error', optimizer = 'adam')

    model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 100, batch_size = 64, verbose = 1)
    
    model.save("savedmodels/msftsavedmodel.h5")

    return(model)

msftsavingmodel()