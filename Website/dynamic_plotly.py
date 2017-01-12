import pymongo
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline

def dynamic_graphing(word):
    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.metoffice
    collection = db.tweets_rawish
    data = collection.find({'text': {'$regex': word}}, {'text': 1, '_id': 0, 'date':1})
    dateList = db.weather_dt.find({},{'date obtained':1,'_id':0})
    initDateList = [d['date obtained'] for d in dateList]
    dateDict = {}
    for i in initDateList:
        if i not in dateDict.keys():
            dateDict[i] = 0
    tweetDates = [d['date'] for d in data]
    for t in tweetDates:
        dateDict[t] += 1
    df = pd.DataFrame(pd.Series(dateDict))
    data = [
        go.Bar(
            x = df.index,
            y = df[0]
        )
    ]
    layout = go.Layout(
        bargap = 0,
        title = word + ' tweets'
    )
    fig = go.Figure(data = data, layout = layout)
    division = offline.plot(fig, include_plotlyjs=False, output_type='div')
    return division