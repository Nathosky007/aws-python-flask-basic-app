from flask import Flask

application = Flask(__name__)

app = application

@app.route('/', methods=['GET', 'POST'])
def hello():
        return "Hello World!"

if __name__ == "__main__":
        app.run()

