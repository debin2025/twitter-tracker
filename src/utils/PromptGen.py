from NewsNER import news_ner_rank
from TweetEntitySentiment import entity_sentiment
from MostCommonNER import most_popular_24h

import pymongo


client = pymongo.MongoClient("mongodb+srv://debin:Kh4AXk%3Dt6_EnK%24%3E%7B@tweetdb1.kbwtapy.mongodb.net/test")
dbname = client["Tweets"]
collection = dbname["LeftWingTweets"]

def news_feed_prompt():
    topic = news_ner_rank(0)
    tweets = list(collection.find({"ner" : topic}))
    overall_sentiment = 0
    for tweet in list(tweets):
        overall_sentiment+=entity_sentiment(topic, tweet["text"])
    print(overall_sentiment)
    if overall_sentiment > 1:
        return f"there is a fictional character named bob who is a trendy millennial that holds positive sentiment toward {topic}, what might bob say about {topic} in tweet form without using simile"
    elif overall_sentiment < -1:
        return f"there is a fictional character named bob who is a trendy millennial that holds negative sentiment toward {topic}, what might bob say about {topic} in tweet form without using simile"
    else:
        topic = news_ner_rank(1)
        tweets = collection.find({"ner" : topic})
        overall_sentiment = 0
        for tweet in tweets:
            overall_sentiment+=entity_sentiment(topic, tweet["text"])
        if overall_sentiment > 1:
            return f"there is a fictional character named bob who is a trendy millennial that holds positive sentiment toward {topic}, what might bob say about {topic} in tweet form without using simile"
        elif overall_sentiment < -1:
            return f"there is a fictional character named bob who is a trendy millennial that holds negative sentiment toward {topic}, what might bob say about {topic} in tweet form without using simile"
        else:
            topic = news_ner_rank(2)
            tweets = collection.find({"ner" : topic})
            overall_sentiment = 0
            for tweet in tweets:
                overall_sentiment+=entity_sentiment(topic, tweet["text"])
            if overall_sentiment > 1:
                return f"there is a fictional character named bob who is a trendy millennial that holds positive sentiment toward {topic}, what might bob say about {topic} in tweet form without using simile"
            elif overall_sentiment < -1:
                return f"there is a fictional character named bob who is a trendy millennial that holds negative sentiment toward {topic}, what might bob say about {topic} in tweet form without using simile"
            else:
                print("No viable candidate.")
                return " "

def user_prompt_gen(tweet_queue):
    topic = most_popular_24h(tweet_queue, 0)
    if topic == "twitter":
        topic = most_popular_24h(tweet_queue, 1)
    print(topic)
    tweets = list(collection.find({"ner" : topic}))
    print(tweets)
    if len(tweets) > 1:
        overall_sentiment = 0
        for tweet in list(tweets):
            overall_sentiment+=entity_sentiment(topic, tweet["text"])
            print(overall_sentiment)
        if overall_sentiment > 1:
            return f"there is a fictional character named bob who is a trendy millennial that holds positive sentiment toward {topic}, what might bob say about {topic} in tweet form in a way that is unique without using simile"
        elif overall_sentiment < -1:
            return f"there is a fictional character named bob who is a trendy millennial that holds negative sentiment toward {topic}, what might bob say about {topic} in tweet form in a way that is unique without using simile"
    else:
        topic = most_popular_24h(tweet_queue, 1)
        tweets = collection.find({"ner" : topic})
        if len(list(tweets)) > 1:
            overall_sentiment = 0
            for tweet in tweets:
                overall_sentiment+=entity_sentiment(topic, tweet["text"])
            if overall_sentiment > 1:
                return f"there is a fictional character named bob who is a trendy millennial that holds positive sentiment toward {topic}, what might bob say about {topic} in tweet form in a way that is unique without using simile"
            elif overall_sentiment < -1:
                return f"there is a fictional character named bob who is a trendy millennial that holds negative sentiment toward {topic}, what might bob say about {topic} in tweet form in a way that is unique without using simile"
        else:
            topic = most_popular_24h(tweet_queue, 2)
            tweets = collection.find({"ner" : topic})
            if len(list(tweets)) > 1:
                overall_sentiment = 0
                for tweet in tweets:
                    overall_sentiment+=entity_sentiment(topic, tweet["text"])
                if overall_sentiment > 1:
                    return f"there is a fictional character named bob who is a trendy millennial that holds positive sentiment toward {topic}, what might bob say about {topic} in tweet form in a way that is unique without using simile"
                elif overall_sentiment < -1:
                    return f"there is a fictional character named bob who is a trendy millennial that holds negative sentiment toward {topic}, what might bob say about {topic} in tweet form in a way that is unique without using simile"
                else:
                    print("No viable candidate.")
                    return " "
