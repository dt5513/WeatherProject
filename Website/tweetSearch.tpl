<!DOCTYPE html>
<html>
<head>
    
<link rel="stylesheet" type="text/css" href="C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\css\common.css">
<link rel="stylesheet" type="text/css" href="C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\css\normalize.css">
<link rel="stylesheet" type="text/css" href="C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\css\twitt.css">
    
    
    
<title>Tweet Data</title>
</head>
<body bgcolor="#ffffff">

<div class = "TopRightSearch">
    <p> Button</p>
</div>
    
<div class = "TopBar">
    <div class = "TopImg">
        <img src="https://raw.githubusercontent.com/rachaelecole/WeatherTwitterProject/master/Website/img/RITMLogo.png" >
        </div>
</div>     
    
    
    
%for thing in data:
<li>{{thing}}</li>
%end
</body>
</html>