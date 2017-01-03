from pandas import DataFrame
import pandas as pd
import nltk
from nltk import word_tokenize, wordpunct_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.probability import FreqDist, DictionaryProbDist, ELEProbDist, sum_logs
from nltk.classify.api import ClassifierI
import pickle
import csv

#IMPLEMENTATION
with open('C:\Users\Student16\PycharmProjects\MetData Project\machine_learning_weather.csv') as r:
    treader = csv.reader(r)
    rtweets = []
    for t in treader:
        rtweets.append(t)

# combining lists while cleaning and getting rid of words two letters or less
tweets = []
for (words, decision) in rtweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >=3]
    tweets.append((words_filtered, decision))


#extracting word features from tweets
def get_words_in_tweets(tweets):
    all_words = []
    for (words, decision) in tweets:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

for t in get_word_features(get_words_in_tweets(tweets)):
    if t not in word_features:
        word_features.append(t)

word_features = get_word_features(get_words_in_tweets(tweets))

with open('./MachineLearningPickle2', 'wb') as mp:
    pickle.dump(word_features, mp)
#CLASSIFIER
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

#applying features to classifier
training_set = nltk.classify.apply_features(extract_features, tweets)

#training classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)

#print classifier.show_most_informative_features(32)

with open('./MachineLearningPickle','wb') as mlp:
    pickle.dump(classifier,mlp)
