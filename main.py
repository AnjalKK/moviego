from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'helloooooo aboo anjal dev!!!!!!!!!!'