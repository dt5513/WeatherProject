import pymongo
import bottle


@bottle.route('/')

def home_page():
    mythings = ['Darren','Rachael','Deniss']
    img = "C:\\Git\\TwittProj\\WeatherTwitterProject\\WeatherTwitterProject\\Website\\img\\cat.gif"
    return bottle.template('C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\\tweetSite.tpl',{"username":"Darren","things":mythings, "img":img})

@bottle.route('/graphs')
def tweetGraphs():
    mythings = ['Darren', 'Rachael', 'Deniss']
    img = "C:\\Git\\TwittProj\\WeatherTwitterProject\\WeatherTwitterProject\\Website\\img\\cat.gif"
    return bottle.template('C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\\tweetGraphs.tpl',
                           {"username": "Darren", "things": mythings, "img": img})


@bottle.post('/word')



def tweetSearch():
    import pymongo
    import pandas as pd
    import plotly.plotly as py
    import plotly.graph_objs as go
    import plotly.offline as offline
    word = bottle.request.forms.get('word')
    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.metoffice
    collection = db.tweets_rawish
    data = collection.find({'text': {'$regex': word}}, {'text': 1, '_id': 0, 'date':1})
    dateList = db.weather_dt.find({}, {'date obtained': 1, '_id': 0})
    textData = [d['text'] for d in data]
    data = collection.find({'text': {'$regex': word}}, {'text': 1, '_id': 0, 'date': 1})
    dateData = [d['date'] for d in data]
    initDateList = [d['date obtained'] for d in dateList]
    dateDict = {}
    for i in initDateList:
        if i not in dateDict.keys():
            dateDict[i] = 0
    tweetDates = dateData
    for t in tweetDates:
        dateDict[t] += 1
    df = pd.DataFrame(pd.Series(dateDict))
    data = [
        go.Bar(
            x=df.index,
            y=df[0]
        )
    ]
    layout = go.Layout(
        bargap=0,
        title=word + ' tweets'
    )
    fig = go.Figure(data=data, layout=layout)

    html1 = """<!DOCTYPE html>
                                    <html>
                                    <head>


                                    <link rel="stylesheet" type="text/css" href="https://cdn.rawgit.com/rachaelecole/WeatherTwitterProject/master/Website/css/common.css">
                                    <link rel="stylesheet" type="text/css" href="https://cdn.rawgit.com/rachaelecole/WeatherTwitterProject/master/Website/css/normalize.css">
                                    <link rel="stylesheet" type="text/css" href="https://rawgit.com/rachaelecole/WeatherTwitterProject/master/Website/css/twitt.css">



                                    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>


                                    <title>Tweet Data</title>
                                    </head>
                                    <body bgcolor="#ffffff">

                                    <div class = "TopRightSearch">

                                        <a href="graphs"><button class="formButt2 graphsButt">Graphs</button></a>
                                    </div>

                                    <div class = "TopBarSearch">
                                        <div class = "TopImg">
                                            <a href="http://localhost:8082/"><img src="https://raw.githubusercontent.com/rachaelecole/WeatherTwitterProject/master/Website/img/RITMLogo.png" ></a>
                                            </div>
                                    </div>

                                    <div class = "DynamicGraph">"""
    html2 = """    </div>

    <div class = "TweetsList">
        <ul>
          %for thing in data:
        <li>{{thing}}</li>
        %end
    </ul>
    </div>



    </body>
    </html>    """

    graph = offline.plot(fig, include_plotlyjs=False, output_type='div')
    graphTemplate = html1 + graph + html2
    return bottle.template(graphTemplate, {'data':textData})
    #return bottle.template('C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\\tweetSearch.tpl',{'data':textData,'graph':graph})


bottle.debug(True)
bottle.run(host='localhost', port=8082)
