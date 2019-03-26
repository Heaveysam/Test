from flask import Flask, request
from localwebsite import app


@app.route('/test/<x>', methods=['GET','POST'])
def test(x):
	return '''<html>\n<body><h1>You wanted {}, you got Thor instead</h1>
			<video width="320" height="240" controls>
  			<source src="movie.mp4" type="video/mp4">
  
"Your browser does not support the video tag."</video>	
</body>\n</html>

	'''.format(x)

@app.route('/')
def index():
	return '''<title> Welcome </title>
			<h1> Welcome </h1>
			 <a href="/test/test">Have a look at the test</a> '''

