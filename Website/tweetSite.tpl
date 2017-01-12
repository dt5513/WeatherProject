<!DOCTYPE html>
<html>
<head>
    

    
<link rel="stylesheet" type="text/css" href="C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\css\normalize.css">
<link rel="stylesheet" type="text/css" href="C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\css\common.css">
<link rel="stylesheet" type="text/css" href="C:\Git\TwittProj\WeatherTwitterProject\WeatherTwitterProject\Website\css\twitt.css">


    
<title>Tweets Website</title>
</head>
<body bgcolor="#F9ECD8">
<div class = "TopBar">
    <b>yo</b>
    <div class = "TopImg">
        <img src="http://i.imgur.com/oaRAe98.jpg">
      
        </div>
     </div> 
    <p>
Welcome {{username}}!{{img}}
    <p>
<ul>
%for thing in things:
<li>{{thing}}</li>
%end
</ul><p>
<form action="/word" method="POST">
What word to search for?
<input type="text" name="word" size=40 value=""><br>
<input type="submit" value="Submit">
</form>
</body>
</html>

