__author__ = 'Noel'
import sys

import requests
import urllib
import urllib.request
from flask import Flask
from flask import render_template
from flask import request
from twitter import *
import twitterapitests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def setup():
    global config
    config = {}
    exec(compile(open("config.py", "rb").read(), "config.py", 'exec'), config)

    global twitter
    twitter = Twitter(
                auth = OAuth(config["access_key"],
                    config["access_secret"],
                    config["consumer_key"],
                    config["consumer_secret"]))


if __name__ == '__main__':
    #setup()
    app.run(debug=False)
    
#look there is stuff here