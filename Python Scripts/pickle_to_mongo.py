import pymongo
import pickle

tweetPath = 'C:\MetOfficeProject\\tweets_wt.pickle'
weatherPath = 'C:\MetOfficeProject\\weather_wt.pickle'

connection = pymongo.MongoClient("mongodb://localhost")

with open(tweetPath,'rb') as file:
    tweets = []
    tweets.extend(p for p in pickle.load(file))

with open(weatherPath,'rb') as file:
    weather = []
    weather.extend(p for p in pickle.load(file))

db = connection.metoffice

tweetCollection = db.tweets_wt
tweetCollection.drop()
for t in tweets:
    tweetCollection.insert_one(t)

weatherCollection = db.weather_dt
weatherCollection.drop()
for w in weather:
    weatherCollection.insert_one(w)
