from pandas import DataFrame
import pandas as pd
import nltk
from nltk import word_tokenize, wordpunct_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.probability import FreqDist, DictionaryProbDist, ELEProbDist, sum_logs
from nltk.classify.api import ClassifierI
import pickle
import Machine_Learning_1

with open('./MachineLearningPickle2','rb') as mp:
    word_features = pickle.load(mp)
with open('./MachineLearningPickle','rb') as mlp:
     classifier = pickle.load(mlp)
print len(word_features)

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

#tweet = "Too early and and cold to be going too work\U0001f631,but it's Tuesgay so it's Holby tonight \U0001f61d\U0001f61dwoop woop https://t.co/SilXql3K2D"
tweet = 'Hating the London fog'
print classifier.classify(extract_features(tweet.split()))


