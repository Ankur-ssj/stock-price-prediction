import pandas as pd
import numpy as np
import datetime as dt
import re
from wordcloud import WordCloud, STOPWORDS
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import snscrape.modules.twitter as sntwitter
import matplotlib.pyplot as plt




#SENTIMENT ANALYSIS------------>
def applesentimentanalysis():
    #Get user input
    query = 'AAPL'

    #As long as the query is valid (not empty or equal to '#')...
    if query != '':
        noOfTweet = '500'
        if noOfTweet != '' :
            noOfDays = '7'
            if noOfDays != '':
                    #Creating list to append tweet data
                    tweets_list = []
                    now = dt.date.today()
                    now = now.strftime('%Y-%m-%d')
                    yesterday = dt.date.today() - dt.timedelta(days = int(noOfDays))
                    yesterday = yesterday.strftime('%Y-%m-%d')
                    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query + ' lang:en since:' +  yesterday + ' until:' + now + ' -filter:links -filter:replies').get_items()):
                        if i > int(noOfTweet):
                            break
                        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

                    #Creating a dataframe from the tweets list above 
                    df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

    
    # Create a function to clean the tweets
    def cleanTxt(text):
        text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
        text = re.sub('#', '', text) # Removing '#' hash tag
        text = re.sub('RT[\s]+', '', text) # Removing RT
        text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
        return text

    #applying this function to Text column of our dataframe
    df["Text"] = df["Text"].apply(cleanTxt)

    #Sentiment Analysis
    def percentage(part,whole):
        return 100 * float(part)/float(whole)

    #Assigning Initial Values
    positive = 0
    negative = 0
    neutral = 0
    #Creating empty lists
    tweet_list1 = []
    neutral_list = []
    negative_list = []
    positive_list = []

    #Iterating over the tweets in the dataframe
    for tweet in df['Text']:
        tweet_list1.append(tweet)
        analyzer = SentimentIntensityAnalyzer().polarity_scores(tweet)
        neg = analyzer['neg']
        neu = analyzer['neu']
        pos = analyzer['pos']
        comp = analyzer['compound']

        if neg > pos:
            negative_list.append(tweet) #appending the tweet that satisfies this condition
            negative += 1 #increasing the count by 1
        elif pos > neg:
            positive_list.append(tweet) #appending the tweet that satisfies this condition
            positive += 1 #increasing the count by 1
        elif pos == neg:
            neutral_list.append(tweet) #appending the tweet that satisfies this condition
            neutral += 1 #increasing the count by 1 

    positive = percentage(positive, len(df)) #percentage is the function defined above
    negative = percentage(negative, len(df))
    neutral = percentage(neutral, len(df))

    #Converting lists to pandas dataframe
    tweet_list1 = pd.DataFrame(tweet_list1)
    neutral_list = pd.DataFrame(neutral_list)
    negative_list = pd.DataFrame(negative_list)
    positive_list = pd.DataFrame(positive_list)
    #using len(length) function for counting

    labels = ['Positive ['+str(round(positive))+'%]' , 'Neutral ['+str(round(neutral))+'%]','Negative ['+str(round(negative))+'%]']
    sizes = [positive, neutral, negative]
    colors = ['yellowgreen', 'blue','red']
    patches, texts = plt.pie(sizes,colors=colors, startangle=90)
    plt.style.use('default')
    plt.legend(labels)
    plt.title("Sentiment Analysis Result for keyword= "+query+"" )
    plt.axis('equal')
    plt.savefig("FrontEnd/stock-price-prediction/src/static/applestatic/applepiechart.png")


    return len(tweet_list1), noOfDays, len(positive_list), len(neutral_list), len(negative_list)


applesentimentanalysis()


#print(noOfDays, len(tweet_list1), len(positive_list), len(neutral_list), len(negative_list))