from flask import Flask
import requests, json, time, psycopg2, os, tweepy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

@app.route("/")
def index():
    return "Hello World!"

@app.route("/fillTheDatabase")
def fillTheDatabase():

    def fillTheDB():

        page = requests.get("https://ideasai.net/", headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all(attrs={"type":"application/ld+json"})

        def find_all(a_str, sub):
            start = 0
            while True:
                start = a_str.find(sub, start)
                if start == -1: return
                yield start
                start += len(sub)

        aa = find_all(str(price), '</script>, <script type="application/ld+json">')
        k = 0
        i = 1
        index5 = 0

        for a in aa:
            if i == 4: index5 = int(a)
            elif i == 5:
                f = open("read.json", "w")
                f.write(str(price)[index5 + 46:a])
            i += 1

    fillTheDB()
    f = open('read.json')
    data = json.load(f)

    conn = psycopg2.connect(
        user = os.getenv('user'), 
        host = os.getenv('host'), 
        database = os.getenv('database'), 
        port = os.getenv('port'), 
        password = os.getenv('password')
    )

    for quoteData in data["itemListElement"]:
        conn.autocommit = True
        cursor = conn.cursor()
        insert_string = "INSERT INTO tIdea (ideaString) VALUES ('" + quoteData['item']['name'] + "')"
        cursor.execute(insert_string)
        conn.commit()
    conn.close()

    os.remove("read.json")

    return "Added New Quotes Successfully to the Database"

@app.route("/postTweet")
def postTweet():

    conn = psycopg2.connect(
        user = os.getenv('user'), 
        host = os.getenv('host'), 
        database = os.getenv('database'), 
        port = os.getenv('port'), 
        password = os.getenv('password')
    )

    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tIdea LIMIT 1')
    a = list(cursor.fetchone())
    delete_string = "DELETE FROM tIdea WHERE ideaID = " + str(a[0])
    cursor.execute(delete_string)
    conn.commit()
    conn.close()

    # Write code here for tweeting instead of Printing.
    auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
    auth.set_access_token(os.getenv('access_token'), os.getenv('access_secret'))
    api = tweepy.API(auth)
    startString = "Startup Idea "
    tweetString =  + str(a[0]) + ":\n" + str(a[1])
    if len(tweetString) + 32 < 281:
        tweetString = "Idea " + tweetString + "\n" + "#StartupIdeas #BusinessIdeas"
    else:
        tweetString = startString + tweetString
    api.update_status(status=(tweetString))
    return "The, Tweet was successful " + str(a[0]) + " " + str(a[1])