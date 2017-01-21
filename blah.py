__author__ = 'Noel'
import sys

import requests
import urllib
import urllib.request
from flask import Flask
from flask import request
from twitter import *

app = Flask(__name__)

@app.route("/login")
def login():
    user = request.form.get("inputEmail")
    pswd = request.form.get("inputPassword")
    r = requests.post("https://api.twitter.com/oauth/request_token",
        data={"oauth_callback": urllib.request.pathname2url("https://www.youtube.com")}
        )

    if r.status_code != '200':
        print("Failed to get request token")
        return

    oauth_token = r['oauth_token']

    r = requests.get(urllib.request.pathname2url("https://api.twitter.com/oauth/authorize?oauth_token=" + oauth_token))

    if r.status_code != '200':
        print("Failed to authorize")
        return

    oauth_verifier = r['oauth_verifier']

    r = requests.post("https://api.twitter.com/oauth/access_token",
        data={"oauth_token": urllib.request.pathname2url(oauth_verifier)}
        )

    if r.status_code != '200':
        print("Failed to get access token")
        return


    user_oauth_token = r['oauth_token']
    user_oauth_token_secret = r['oauth_token_secret']




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
    setup()
    app.run(debug=False)
    
#look there is stuff here
