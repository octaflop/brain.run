from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'brain.run is a place for micro apps'

