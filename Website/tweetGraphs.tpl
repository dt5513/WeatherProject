<!DOCTYPE html>
<html>
<head>
    

<link rel="stylesheet" type="text/css" href="https://cdn.rawgit.com/rachaelecole/WeatherTwitterProject/master/Website/css/common.css">
<link rel="stylesheet" type="text/css" href="https://cdn.rawgit.com/rachaelecole/WeatherTwitterProject/master/Website/css/normalize.css">
<link rel="stylesheet" type="text/css" href="https://rawgit.com/rachaelecole/WeatherTwitterProject/master/Website/css/twitt.css">

 
<!--<link rel="stylesheet" type="text/css" href="C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\css\common.css">
<link rel="stylesheet" type="text/css" href="C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\css\normalize.css">
<link rel="stylesheet" type="text/css" href="C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\css\twitt.css">
-->    

    
<title>Tweet Data</title>
</head>
<body bgcolor="#ffffff">

<!--
<div class = "TopRightSearch">
    
    <a href="graphs"><button class="formButt2 graphsButt">Graphs</button></a>
</div>
-->
<div class="parallax">
    <div class = "introText">
        <h1>Twitter Weather Project Analysis <br></h1>
        <div class = "introText2">
        <h2><br>by Darren Tran, Rachael Cole, Deniss Ustinovs</h2>
        
        </div>
        
    </div>
    
    </div>    
<div class = "TopBarSearch">
    <div class = "TopImg">
        <a href="http://localhost:8082/"><img src="https://raw.githubusercontent.com/rachaelecole/WeatherTwitterProject/master/Website/img/RITMLogo.png" ></a>
        </div>
</div>     
<div class = "graphsMain">
    
        <div class = "firstRowText">
            <p>For this project we were given the brief of having to ingest, blend and analyse forecasted weather data from the MetOffice and Twitter to compare the accuracy of MetOffice forecasting to a quantified record of live weather retrieved from the Twitter.  We collected data from the 6th December 2016 to 8th January 2017 in the London region and then used plot.ly to produce graphs to see if there were any relationships.</p><br/><p>
            Files and details used in this project can be found at <a href="https://github.com/rachaelecole/WeatherTwitterProject">our repository.</a>
            </p>
        </div>
    <div class = "firstRow">
         <div class = "textSqueeze"><p> 
            The first 2 graphs show the proportions of words in tweets for each weather type. The pie chart shows the percentages of each weather word in the tweets collected. The stacked bar chart demonstrates the same thing but over datetime. From our tweets we can conclude that over the time period, fog and rain were the most tweeted about weather types. 

</p><br/><p>The third graph shows the weather predictions made by the MetOffice for 'Foggy', 'Cloudy', 'Rain' and 'Sunny' weather types. From this graph it can be seen that it was mostly cloudy but very little rain and fog. The opposing results between Twitter and the MetOffice is most likely to be because Twitter users and the MetOffice have very different interpretations of the weather.  </p></div>
        <div class = "firstGraph">
             <iframe height="400" scrolling="no" seamless="seamless" src="https://plot.ly/~rachaelecole/40.embed" width="400" data-aspect-ratio="1.4780487804878049"></iframe>
        </div>
       </div>
    <div class = "secondGraphRow">
        <div class = "doubleGraphs">
            <div class = "doubleGraphCont graphLeft">
                <iframe height="460" scrolling="no" seamless="seamless" src="https://plot.ly/~rachaelecole/44.embed" width="820" data-aspect-ratio="1.5"></iframe>
            
            </div>
             <div class = "doubleGraphCont graphRight">
                <iframe height="460" scrolling="no" seamless="seamless" src="https://plot.ly/~rachaelecole/46.embed" width="820" data-aspect-ratio="1.5"></iframe>
            
            </div>
        </div>
        <div class = "textSqueeze2"><p> 
            The 4 graphs below show the accuracy of the MetOffice data vs. the factor (see README file) of tweets collected for the corresponding weather type. The 'Sunny' graph shows a correlation between the two variables. On the whole, when it was predicted to be sunny by the MetOffice, people were also tweeting about the weather being sunny. The 'Cloudy' graph also shows a correlation. Both sets of data follow a similar pattern although some peaks/troughs increase/decrease at different rates. There is a slight correlation for rain. Both sets of data have the same peak and follow a general pattern. However, tweets have must larger rates of change between data points. Finally, the fog graph shows not much of a correlation. It can be seen that people tweet about the fog  much more than it is predicted by the MetOffice. </p></div>
        
        
    </div>
    <div class = "secondGraphRow">
        <div class = "doubleGraphs">
            <div class = "doubleGraphCont graphLeft">
                <iframe height="520" scrolling="no" seamless="seamless" src="https://plot.ly/~rachaelecole/24.embed" width="850" data-aspect-ratio="1.4780487804878049"></iframe>
            </div>
            <div class = "doubleGraphCont graphRight">
                <iframe height="520" scrolling="no" seamless="seamless" src="https://plot.ly/~rachaelecole/18.embed" width="850" data-aspect-ratio="1.4780487804878049"></iframe>
            </div>
        
        </div>
        <div class = "doubleGraphs">
            <div class = "doubleGraphCont graphLeft">
                <iframe height="520" scrolling="no" seamless="seamless" src="https://plot.ly/~rachaelecole/34.embed" width="850" data-aspect-ratio="1.4780487804878049"></iframe>
            </div>
            <div class = "doubleGraphCont graphRight">
                <iframe height="520" scrolling="no" seamless="seamless" src="https://plot.ly/~rachaelecole/20.embed" width="850" data-aspect-ratio="1.4780487804878049"></iframe>
            </div>
        <div>
            </div>
        </div>
    </div>
    <div class = "fourthRow">
            <p> Two further graphs were produced between data we thought would have a correlation. 'The number of cold words in tweets and the temperature' graph shows a strong negative correlation between total cold words in tweets and the temperature as predicted by the MetOffice. This is because as the temperature drops, more people are likely to tweet about the cold weather. Interestingly, the temperature always feels colder than it actually is.
'The total rain words in tweets and the precipitation probability' graph shows that an increase in the precipitation probability will generally be followed by a high value for the total rain words in tweets. This is because the precipitation probability is directly related to the rain which causes people to tweet about it.</p>
    </div>
    <div class = "secondGraphRow">
            <div class = "graphsMain">
                <iframe height="520" scrolling="no" seamless="seamless" src="https://plot.ly/~rachaelecole/48.embed" width="850" data-aspect-ratio="1.4780487804878049"></iframe>
            </div>
            <div class = "graphsMain">
                <iframe height="520" scrolling="no" seamless="seamless" src="https://plot.ly/~rachaelecole/36.embed" width="850" data-aspect-ratio="1.4780487804878049"></iframe>
            </div>
    </div>
    <div class = "fourthRow">
    <p>'The MetOffice weather forecasts agreement rate with the weather from tweets' graph shows the rate at which our weather data agreed 
with out Twitter data. We mostly got a low agreement between both sets of data, ie, they were saying different weather types. However, 
this is most likely to be because of people having an overall negative opinion of the weather and therefore over-exaggerating on their 
tweets. 'The weather factors from tweets for each day' graph shows the tweets we were collecting each day for all weather types. It can be seen easily that people were tweeting the most about the fog, rain, and cold.
    </p>
    </div>
    <div class = "secondGraphRow">
        <div class = "graphsMain">
                <iframe height="520" scrolling="no" seamless="seamless" src="https://plot.ly/~rachaelecole/55.embed" width="850" data-aspect-ratio="1.4780487804878049"></iframe>
            </div>
            <div class = "graphsMain">
                <iframe height="520" scrolling="no" seamless="seamless" src="https://plot.ly/~rachaelecole/53.embed" width="850" data-aspect-ratio="1.4780487804878049"></iframe>
            </div>
        
        </div>
    </div>
</div>    
<!--
<ul>    
    
</ul>
-->
</body>
</html>

<!--
 <li>@BIUK In pics - dense #fog in #FinsburyPark, North #London. #ukweather #foggy https://t.co/D1jVRapOBS https://t.co/zxgufd7d5N | 2016-12-28</li>
       <li>@DStarPics In pics - dense #fog in #FinsburyPark, North #London. #ukweather #foggy https://t.co/D1jVRapOBS https://t.co/zxgufd7d5N | 2016-12-28</li>
       <li>@Independent In pics - dense #fog in #FinsburyPark, North #London. #ukweather #foggy https://t.co/D1jVRapOBS https://t.co/zxgufd7d5N | 2016-12-28</li>-->
