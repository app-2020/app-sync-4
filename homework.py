#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 08:30:39 2021

@author: pepe
"""

#%% Creating tweets - server

from flask import Flask, request, jsonify

app = Flask("tweeter")

tweets = []

@app.route("/tweet", methods = ["PUT"])
def create_tweet():
    tweet = request.get_json()
    tweets.append(tweet)
    return "Tweet saved"

@app.route("/")
def show_timeline():
    return jsonify(tweets)

@app.route("/<username>")
def show_tweets_by_user(username):
    tweets_by_user = []
    
    for tweet in tweets:
        if tweet["username"] == username:
            tweets_by_user.append(tweet)
            
    return jsonify(tweets_by_user)

app.run()


#%% Creating tweets - client

import requests

tweet = {
    "username": "dani",
    "text": "Let's try tweeter out!"
    }

response = requests.put("http://localhost:5000/tweet", json = tweet)

print(response.text)






















