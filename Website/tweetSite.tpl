<!DOCTYPE html>
<html>
<head>
<title>Tweets Website</title>
</head>
<body>
<p>
Welcome {{username}}!
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