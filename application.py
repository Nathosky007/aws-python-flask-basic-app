from flask import Flask
from flask import render_template

application = Flask(__name__)

@application.route('/')
@application.route('/index')
def index():
	return render_template('index.html',title='Home')

if __name__ == "__main__":
        application.run()
