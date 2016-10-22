from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Brosef'}
	posts = [
		{
			'author' : {'name': 'John'},
			'body': {'What a pain in my ass'}
		},
		{
			'author' : {'name': 'Johanna'},
			'body': 'Life is beautiful and fleeting'
		}
	]
	return render_template('index.html',
			user = user,
			title = '',
			posts = posts)