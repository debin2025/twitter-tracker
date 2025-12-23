from pymongo_get_database import get_database
from collections import Counter

dbname = get_database()
collection = dbname["LeftWingTweets"]

def most_popular_ner():
    unprocessed_tweets = collection.find()
    count = Counter()
    for tweet in unprocessed_tweets:
        for ner in tweet["ner"]:
            count[ner]+=1
    return count

def most_popular_24h(tweet_list, rank):
    unprocessed_tweets = []
    count = Counter()
    for tweet in tweet_list:
        unprocessed_tweets+=collection.find({"text" : tweet[3]})
    for tweet in unprocessed_tweets:
        for ner in tweet["ner"]:
            if ner.startswith("@") == False:
                count[ner]+=1
    return count.most_common(3)[rank][0]
