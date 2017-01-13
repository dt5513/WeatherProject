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

<div class = "TopRightSearch">
    
    <a href="graphs"><button class="formButt2 graphsButt">Graphs</button></a>
</div>
    
<div class = "TopBarSearch">
    <div class = "TopImg">
        <a href="http://localhost:8082/"><img src="https://raw.githubusercontent.com/rachaelecole/WeatherTwitterProject/master/Website/img/RITMLogo.png" ></a>
        </div>
</div>
    
<div class = "DynamicGraph">
    {{graph}}
    </div>    
    
<div class = "TweetsList">
    <ul>    
      %for thing in data:
    <li>{{thing}}</li>
    %end
</ul>
</div>    
    
    
    
</body>
</html>    
    
    
    
    
<!--
<ul>    
    
</ul>
-->


<!--
 <li>@BIUK In pics - dense #fog in #FinsburyPark, North #London. #ukweather #foggy https://t.co/D1jVRapOBS https://t.co/zxgufd7d5N | 2016-12-28</li>
       <li>@DStarPics In pics - dense #fog in #FinsburyPark, North #London. #ukweather #foggy https://t.co/D1jVRapOBS https://t.co/zxgufd7d5N | 2016-12-28</li>
       <li>@Independent In pics - dense #fog in #FinsburyPark, North #London. #ukweather #foggy https://t.co/D1jVRapOBS https://t.co/zxgufd7d5N | 2016-12-28</li>-->
