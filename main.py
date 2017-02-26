__author__ = 'Noel'
import sys

import requests
import urllib
import urllib.request
from flask import Flask, render_template, request, jsonify
from twitter import *
import twitterapitests
import userprofile

app = Flask(__name__)

config = {}
exec(compile(open("config.py", "rb").read(), "config.py", 'exec'), config)
twitter_config = Twitter(
    auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

def convert_to_dict(profile_array):
    profile_dict_array = []
    for profile in profile_array:
        temp_dict = {}
        temp_dict['name'] = profile.name
        temp_dict['screen_name'] = profile.screen_name
        temp_dict['user_id'] = profile.user_id
        temp_dict['profile_picture_link'] = profile.profile_picture_link
        profile_dict_array.append(temp_dict)
    return profile_dict_array

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
    search_term = request.args.get('searchText', "", type=str)
    profiles = twitterapitests.search_twitter_profiles(twitter_config, search_term, 5)
    serialized_results = convert_to_dict(profiles)
    return jsonify(result=serialized_results)

@app.route('/block', methods=['POST', 'GET'])
def block():
    screen_name = request.args.get('screenName', "", type=str)
    twitterapitests.block_twitter_profile(twitter_config, screen_name)
    return jsonify(result="Success!")

if __name__ == '__main__':
    app.run(debug=False)
    
#look there is stuff here
