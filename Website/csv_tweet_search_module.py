def tweetSearch():
    import pandas as pd
    import plotly.plotly as py
    import plotly.graph_objs as go
    import plotly.offline as offline
    import csv
    word = bottle.request.forms.get('word')
    with open('tweetSearch.csv', 'rb') as csvFile:
        reader = csv.DictReader(csvFile)
        data = []
        initDateList = []
        for row in reader:
            if row['date'] not in initDateList:
                initDateList.append(row['date'])
            if row['text'].find(word) != -1:
                data.append(row)
        textData = [d['text'] for d in data]
        dateData = [d['date'] for d in data]
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