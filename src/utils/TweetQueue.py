import tweepy
from pymongo_get_database import get_database
import asyncio
import sqlite3
from datetime import datetime
from datetime import timedelta
from TweetEntitySentiment import entity_sentiment
from SQLiteUpdateElo import update_PAS
from IronySwitchTest import irony_switch

dbname = get_database()
collection_name = dbname["LeftWingTweets"]

conn = sqlite3.connect(r"/Entities.db")

day_time_delta = timedelta(hours=24)


authors = {1370219239609659396 : '@socdarling',
           1356514488451817472 : '@TheOmniLiberal',
           1300051637915054082 : '@Eristocracy',
           1293138189272719360 : '@Pisco_95_',
           1265733821175119885 : '@TheOnlyHeem',
           1213256887744942081 : '@DemonMamaReal',
           1154603162050994178 : '@EverydayWarren',
           1099570025491423233 : '@VaushV',
           846411464885747712 : '@theserfstv',
           742601614968553472 : '@KnowingBetterYT',
           2203707806 : '@agenttwelvetoes',
           1733467884 : '@shoe0nhead',
           1515728941 : '@PhilosophyTube',
           731070444 : '@laowhy86',
           326756275 : '@hasanthehun',
           27938182 : '@ContraPoints',
           27000730 : '@Timcast'
           }



def check_tweet_queue(queue_list, api):
    removal_queue = []
    for tweet in queue_list:
        try :
            if tweet[2]+day_time_delta <= datetime.now():
                print(f"Scraping for {tweet[0]} begun")
                interaction_score = api.get_status(tweet[0]).favorite_count * 2 + api.get_status(tweet[0]).retweet_count

                query = f"conversation_id:{tweet[0]} is:reply"
                replies = api.search_tweets(q= query)
                reply_score_total = 0
                for reply in replies:
                    reply_score = entity_sentiment(authors[tweet[1]], reply.text)
                    if reply_score < 0:
                        reply_score -= reply.favorite_count
                    else:
                        reply_score += reply.favorite_count
                    reply_score *= irony_switch(reply.text)
                    reply_score_total += reply_score

                total_score = reply_score_total+interaction_score
                print(f"{authors[tweet[1]]}'s PAS has changed by {total_score}")
                collection_name.update_one({'created_at' : tweet[2]}, {'$set' : {'PAS' : total_score}})
                update_PAS(conn, authors[tweet[1]], total_score)
                removal_queue.append(tweet)
        except tweepy.errors.NotFound:
            print(f"{tweet[0]} not found, removing from queue.")
            removal_queue.append(tweet)
            pass
    return removal_queue
