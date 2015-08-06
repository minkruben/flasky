from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello Flasky </h1>'

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s! </h1>' % name

@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, %s</h1>' % user.name


@app.route('/browser')
def detect_browser():
	user_agent = request.headers.get('User-Agent')
	return '<h1> Your browser is %s </h1>' % user_agent

@app.route('/response')
def response_obj():
	response = make_response('<h1> This Document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response

@app.route('/url_redirect')
def url_redirect():
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)