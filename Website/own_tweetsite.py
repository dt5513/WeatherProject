import pymongo
import bottle


@bottle.route('/')

def home_page():
    mythings = ['Darren','Rachael','Deniss']
    img = "C:\\Git\\TwittProj\\WeatherTwitterProject\\WeatherTwitterProject\\Website\\img\\cat.gif"
    return bottle.template('C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\\tweetSite.tpl',{"username":"Darren","things":mythings, "img":img})

@bottle.post('/word')
def tweetSearch():
    word = bottle.request.forms.get('word')
    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.metoffice
    collection = db.tweets_rawish
    data = collection.find({'text': {'$regex': word}}, {'text': 1, '_id': 0, 'date':1})




    data = [d['text'] + '  |  '+ d['date'].encode('utf-8') for d in data]
    return bottle.template('C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\\tweetSearch.tpl',{'data':data})





bottle.debug(True)
bottle.run(host='localhost', port=8082)
