from twython import TwythonStreamer
import datetime as dt
import pickle

#Twitter API Keys
print 'The following details are required to access the twitter API.'
consumerKey = raw_input('Type in your consumer key: ')
consumerSecret = raw_input('Type in your consumer secret: ')
accessToken = raw_input('Type in your access token: ')
accessTokenSecret = raw_input('Type in your access token secret: ')

#filepaths
dayFolder = 'C:\MetOfficeProject\Tweet Data\Tweets\\'
batchFolder = 'C:\MetOfficeProject\Tweet Data\Batch\\'
autosaveFolder = 'C:\MetOfficeProject\Tweet Data\Autosave\\'

#savesizes
batchSize = 500
autosaveSize = 100
daysToRunFor = 100

#weatherwords
weatherWords = ['cold', 'rain', 'warm', 'weather hot', 'snow', 'hail ','hailing', 'freezing', 'winter', 'storm',
              ' ice ',' ice.', 'frosty', 'frozen', 'blustery', 'breezy', 'fog', 'foggy', 'drizzle', 'thunder', 'weather',
             ' icy ', 'mild', ' wind ', 'windy', 'misty', 'pouring down','cloudy','clouds','overcast','gust']

#CONFIGURATION OVER

#functions
def strnowdate():
    return dt.datetime.strftime(dt.datetime.now(),'%y-%m-%d')
def strnowdatetime():
    return dt.datetime.strftime(dt.datetime.now(),'%y-%m-%d-%H%M%S')
def intnowhour():
    return int(dt.datetime.strftime(dt.datetime.now(),'%H'))

class MyStreamer(TwythonStreamer):
    autosaveCounter = 0
    tweetCounter = 0
    batchCounter = 0
    batchNo = 0
    tweets = []
    batchTweets = []
    def on_success(self, data):
        #STOP WHEN PAST 11 O CLOCK
        if intnowhour() >= 23:
            with open(''.join([batchFolder, strnowdate(), '-batch', str(MyStreamer.batchNo)]), 'wb') as batchFile:
                pickle.dump(MyStreamer.batchTweets, batchFile)
            with open(''.join([batchFolder, strnowdate(), 'batchNo']), 'wb') as batchNoFile:
                pickle.dump(MyStreamer.batchNo,batchNoFile)
            self.disconnect()
        tweetReceived = False
        if type(data) is dict:
            if len(data.get('text',''))>0:
                for word in weatherWords:
                    if tweetReceived == False:
                        if word in data['text'].encode('utf-8').lower() and 'train' not in data['text'].encode('utf-8').lower():
                            MyStreamer.autosaveCounter += 1
                            MyStreamer.tweetCounter += 1
                            MyStreamer.batchCounter += 1
                            MyStreamer.tweets.append(data)
                            tempDict = {}
                            tempDict['text'] = data['text'].encode('utf-8')
                            tempDict['created_at'] = data['created_at'].encode('utf-8')
                            MyStreamer.batchTweets.append(tempDict)
                            tweetReceived = True
                            print tempDict['created_at'], '--', tempDict['text'], '--', 'Tweet No.', str(MyStreamer.tweetCounter)
                            if MyStreamer.autosaveCounter >= autosaveSize:
                                with open(''.join([autosaveFolder,strnowdatetime()]),'wb') as autosaveFile:
                                    pickle.dump(MyStreamer.tweets,autosaveFile)
                                MyStreamer.tweets[:] = []
                                MyStreamer.autosaveCounter = 0
                                print '\n AUTOSAVE SUCCESSFUL AT ', strnowdatetime(),'\n'
                            if MyStreamer.batchCounter >= batchSize:
                                with open(''.join([batchFolder,strnowdate(),'-batch',str(MyStreamer.batchNo)]),'wb') as batchFile:
                                    pickle.dump(MyStreamer.batchTweets,batchFile)
                                MyStreamer.batchTweets[:] = []
                                MyStreamer.batchCounter = 0
                                MyStreamer.batchNo += 1
                                print '\n BATCH NO.', str(MyStreamer.batchNo), 'SAVED AT', strnowdatetime(),'\n'
                    else:
                        pass
    def reset_counters(self):
        MyStreamer.autosaveCounter = 0
        MyStreamer.tweetCounter = 0
        MyStreamer.batchCounter = 0
        MyStreamer.batchNo = 0
        MyStreamer.tweets = []
        MyStreamer.batchTweets = []
    def on_error(self,status_code,data):
        print status_code, data
        self.disconnect()

stream = MyStreamer(consumerKey,consumerSecret,accessToken,accessTokenSecret)

dayCounter = 0
while dayCounter < daysToRunFor:
    if intnowhour() >= 1 and intnowhour() < 23:
        dayTweets = []
        day = strnowdate()
        stream.statuses.filter(track = 'London',locations=[-0.342464,51.385499,0.077620,51.612533])
        batchFileCounter = 0
        dayCounter += 1
        stream.reset_counters()
        with open(''.join([batchFolder, day, 'batchNo']), 'rb') as batchNoFile:
            totalBatchFileNo = pickle.load(batchNoFile)
        while batchFileCounter <= totalBatchFileNo:
            with open(''.join([batchFolder, day,'-batch', str(batchFileCounter)]), 'rb') as batchFile:
                dayTweets.extend(pickle.load(batchFile))
            batchFileCounter += 1
        with open(''.join([dayFolder,'Tweets_',day,'.pickle']),'wb') as dayFile:
            pickle.dump(dayTweets,dayFile)
        print 'Tweets for', day, 'collected'
        print str(daysToRunFor), 'days left.'
