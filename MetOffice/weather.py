import json
import urllib
import datetime as dt
import pickle

apiKey = 'xxx'                     # Your api key
filePath = 'C:\MetOfficeProject\Weather Data\Unclean\\'             # Your weather pickles will be saved here my friend

urlKey = ''.join(['http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/352409?res=3hourly&key=', apiKey])
URL = urllib.urlopen(urlKey)
data = json.loads(URL.read())

dataForToday = data['SiteRep']['DV']['Location']['Period']   # List of weather per each day for 5 days

# Keys for weather types
weatherType = {'NA': 'Not available', '0':'Clear night','1':'Sunny day',
               '2': 'Partly cloudy (night)', '3': 'Partly cloudy (day)',
               '4': 'Not used', '5': 'Mist'
    , '6': 'Fog', '7': 'Cloudy', '8': 'Overcast', '9': 'Light rain shower (night)'
    , '10': 'Light rain shower (day)', '11': 'Drizzle', '12': 'Light rain'
    , '13': 'Heavy rain shower (night)', '14': 'Heavy rain shower (day)',
               '15': 'Heavy rain', '16': 'Sleet shower (night)', '17': 'Sleet shower (day)'
    , '18': 'Sleet', '19': 'Hail shower (night)', '20': 'Hail shower (day)', '21': 'Hail'
    , '22': 'Light snow shower (night)', '23': 'Light snow shower (day)', '24': 'Light snow'
    , '25': 'Heavy snow shower (night)', '26': 'Heavy snow shower (day)', '27': 'Heavy snow'
    , '28': 'Thunder shower (night)', '29': 'Thunder shower (day)', '30': 'Thunder'}

# Cleansing of weather data
dayDict = {}
y = 0
while y < len(dataForToday):
    dateOfData = dataForToday[y]['value']
    z = 0
    while z < len(dataForToday[y]['Rep']):
        dayDict['/'.join([dateOfData[:-1], str((int(dataForToday[y]['Rep'][z]['$']) / 180))])] = {}
        shortDict = dayDict['/'.join([dateOfData[:-1], str((int(dataForToday[y]['Rep'][z]['$']) / 180))])]
        shortDict['Date'] = '/'.join([dateOfData[:-1], str((int(dataForToday[y]['Rep'][z]['$']) / 180))])
        shortDict['Time (min)'] = dataForToday[y]['Rep'][z]['$']
        shortDict['Precipitation Probability (%)'] = dataForToday[y]['Rep'][z]['Pp']
        shortDict['Wind Direction'] = dataForToday[y]['Rep'][z]['D']
        shortDict['Wind Gust (mph)'] = dataForToday[y]['Rep'][z]['G']
        shortDict['Feels like Temperature (Celsius)'] = dataForToday[y]['Rep'][z]['F']
        shortDict['Screen Relative Humidity (%)'] = dataForToday[y]['Rep'][z]['H']
        shortDict['Wind Speed (mph)'] = dataForToday[y]['Rep'][z]['S']
        shortDict['Max UV Index'] = dataForToday[y]['Rep'][z]['U']
        shortDict['Temperature (Celsius)'] = dataForToday[y]['Rep'][z]['T']
        shortDict['Weather Type'] = dataForToday[y]['Rep'][z]['W']
        shortDict['Weather'] = weatherType[str(dataForToday[y]['Rep'][z]['W'])]
        shortDict['Visibility'] = dataForToday[y]['Rep'][z]['V']
        shortDict['Date Obtained'] = dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d')
        z += 1
    y += 1

# Creating final list
listFin = []
for i in dayDict.keys():
    listFin.append(dayDict[i])

# Pickling weather file
fileName = ''.join([filePath, 'weather_', dt.datetime.strftime(dt.datetime.now(), '%y-%m-%d-%H'), '.pickle'])
with open(fileName, 'wb') as mof:
    pickle.dump(listFin, mof)
print "Weather data collected at " + dt.datetime.strftime(dt.datetime.now(), '%H:%M') + " my friend."

if dt.datetime.strftime(dt.datetime.now(), '%H') == '2':
    fileName = ''.join(['C:\MetOfficeProject\Weather Data\Clean\\', 'weather_', dt.datetime.strftime(dt.datetime.now(), '%y-%m-%d'), '.pickle'])
    with open(fileName, 'wb') as mof:
        pickle.dump(listFin, mof)
