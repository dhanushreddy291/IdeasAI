from flask import Flask
import tweepy, os, urllib.request
from PIL import Image
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
        return "The, Tweet was successful "