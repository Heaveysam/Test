from flask import Flask, request

app = Flask(__name__)

@app.route('/test/<x>')
def test(x):
	return '''<h1>the answer is not {}</h1>'''.format(x)

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
app.run(port = 80)
