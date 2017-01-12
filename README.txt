WeatherTwitterProject
By rachaelecole, denust, dt5513
-----------------------------
Introduction:

The brief of this project was to ingest, blend and analyse forecasted weather data from the MetOffice DataPoint API and Twitter Streaming API to compare the accuracy of MetOffice forecasting to a quantified record of live weather retrieved from the Twitter firehose. The geographical area looked at was London.
-----------------------------
twittMetData.csv

Folders:
Machine Learning
MetOffice
python Scripts
Website
-----------------------------
twittMetData.csv

Weathers were binned according to the following weather categories:
cloudy, cold, foggy, rain, sunny, windy
[n] refers to the date the data was obtained from the Met Office. 0 means on the day, 1 means the day before, and 2 means 2 days before and so on.

Refer to the Met Office datapoint api reference for more information on units and exact details of the values. 

Columns:
[weather category] = The number of words in tweets that are weather-related that belong to that weather-category for that datetime period.
[weather category]Factor = The [weather category] value divided by the mean of [weather category] value for that time period (equalizes weather values and allows for more fair comparisons across time periods and weather categories).
datetime = The format is YYYY-MM-DD-T, where T is the time period as defined by the Met Office. The T*3 returns the hours in T:00 in a 24 hour clock (e.g. T=6 is 18:00).
Day = The date, for easier aggregations. In YYYY-MM-DD format.
Temperature[n] = The temperature as given by the Met Office for that datetime period.
Weather[n] = The weather, binned into our weather categories, as given by the Met Office for that datetime period.
[weather category]W = A calculation performed to calculate the prediction strength of the Met Office forecasts. A matching [weather category] to the column will cause the calculation (SUM(0.75^[n])) where [n] refers to the [n] of Weather[n]. Non matching [weather category] will return a value of 0 for that [n].
feels like temperature[n] = The feels like temperature as given by Met Office for that datetime period.
humidity[n] = The humidity as given by Met Office for that datetime period.
max uv index[n] = The max UV index as given by Met Office for that datetime period.
precipitation probability[n] = The precipitation probability as given by Met Office for that datetime period.
visibility[n] = The visibility as given by Met Office for that datetime period.
wind direction[n] = The wind direction as given by Met Office for that datetime period.
wind gust[n] = The wind gust as given by Met Office for that datetime period.
wind speed[n] = The wind speed as given by Met Office for that datetime period.
-----------------------------
Machine Learning

Contains files for machine learning. Machine_Learning_1.py can be used for testing purposes. The .pickle files can be loaded into other Machine Learning scripts for configuration purposes to test further tweets.

The initial set of .pickle files (allTweets, classifier, wordFeatures) will classify tweets into weather-related tweets (w) and non-weather-related tweets (n). Beware that these tweets may not be directly related to the current weather.

The .pickle files preceded by wt_ will classify tweets into categories sunny, clouy, snow, rain, foggy, none and forecasts. Note, these classifications are not very accurate and require further classifying.

For a better filtering of tweets we recommend filtering out tweets containing 'RT @' as many of these tweets are not relevant to the current weather, or will heavily skew statistics (this is included in the 'Joined DF with factors.ipynb' file found in the Python Scripts folder. )
-----------------------------
MetOffice

Contains the .csv file with 1 month's of data of weather related tweets, and python files for how the weather data was retrieved and modified to be inserted into MongoDB.
-----------------------------
Python Scripts

Contains the csv for easy access using jupyter notebook. Uses jupyter notebook files to create plotly graphs and manipulate pandas DataFrames. 
Also contains .py scripts to take tweets from twitter, and to insert .pickle files into MongoDB for usage.
-----------------------------
Website

Contains files for creating a website for the project to display the work. The website is assembled using the bottle module in python, and can be run by using the .py file to assemble the .tpl templates for the website. 
-----------------------------
