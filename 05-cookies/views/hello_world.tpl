<!DOCTYPE html>
<html>
<head>
	<title>Hello World</title>
</head>
<body>
	<p>
		Welcome {{username}}
	</p>
	<ul>
		%for thing in things:
			<li>{{thing}}</li>
		%end
	</ul>
	<p>
		<form action="/favorite_fruit" method="post">
			What is your favorite fruit?
			<input type="text" name="fruit" size="40"> <br>
			<input type="submit" value="Submit">
		</form>
	</p>
</body>
</html>