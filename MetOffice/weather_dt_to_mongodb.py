import pymongo
import datetime as dt

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.metoffice
collection = db.weather.find()

weather = []

sunny = ['0','1']
cloudy = ['2','3','7','8']
snow = ['16','17','18','19','20','21','22','23','24','25','26','27']
rain = ['9','10','11','12','13','14','15','28','29','30']
foggy =['5','6']
none = ['4']

for c in collection:
    tempDict = {}
    date = c['Date'][0:10]
    if c['Date'][11:] == '0':
        time = '00:00:00'
    elif c['Date'][11:] == '1':
        time = '03:00:00'
    elif c['Date'][11:] == '2':
        time = '06:00:00'
    elif c['Date'][11:] == '3':
        time = '09:00:00'
    elif c['Date'][11:] == '4':
        time = '12:00:00'
    elif c['Date'][11:] == '5':
        time = '15:00:00'
    elif c['Date'][11:] == '6':
        time = '18:00:00'
    elif c['Date'][11:] == '7':
        time = '21:00:00'
    else:
        print c['Date'][11:]
    if c['Weather Type'] in sunny:
        wt = 'sunny'
    elif c['Weather Type'] in cloudy:
        wt = 'cloudy'
    elif c['Weather Type'] in snow:
        wt = 'snow'
    elif c['Weather Type'] in rain:
        wt = 'rain'
    elif c['Weather Type'] in foggy:
        wt = 'foggy'
    elif c['Weather Type'] in none:
        wt = 'none'
    tempDict['date'] = date
    tempDict['time'] = time
    tempDict['t'] = int(c['Date'][11:])
    tempDict['weather'] = c['Weather']
    tempDict['temperature'] = c['Temperature (Celsius)']
    tempDict['wt'] = wt
    tempDict['date obtained'] = c['Date Obtained']
    weather.append(tempDict)

dumpCollection = db.weather_dt
dumpCollection.drop()

for c in weather:
    dumpCollection.insert_one(c)