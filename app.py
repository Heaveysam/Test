# from localwebsite.webtest import app

# app.route('/new')
# def new():
# 	return('Welcome to the Website')

from localwebsite import app

if __name__ == "__main__":
    # Setting debug to Tru efenables debug output. This line should be
    # removed before deploying a production app.
    # app.debug = True

	import os
	HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
	try:
		PORT = int(os.environ.get('SERVER_PORT', '7000'))
	except ValueError:
		PORT = 7000

	app.run(HOST, PORT)