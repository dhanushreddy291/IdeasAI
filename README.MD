# Twitter Bot

A Twitter bot that has been automated to tweet random business/startup ideas once every two hours. Deployed on Heroku. The ideas are sourced from ideasai.net using Web scraping by Beautifulsoup4 once every 24 hours and storing them in a PostgreSQL Database (Cockroach DB).

The twitter account of the bot is: [@startupideas29](https://twitter.com/startupideas29)

# Inspiration

I always wanted to automate things. Upon finding that heroku's free tier is an overkill for this app I instantly got excited to make this. Now I just relax and let my followers grow itself without doing any work. The followers also get valuable startup ideas that are being generated using [Open AI](https://openai.com/) and posted on [ideasai.net](https://ideasai.net/)

# APIs

- I used the Python Library [Tweepy](https://www.tweepy.org/) for authenticating and posting the tweets.
- I have used a free tier of [Cockroach DB](https://cockroachlabs.com/) for the database (for storing the ideas)

# Things Learnt while making

- The website which I source ideas from is ideasai.net, it does not have a public API so as to take ideas from. So I have to make my own API to get the ideas from the website. So I have used a library in python to web scrape the data first into Json and then into an array of strings, finally storing them into a PostgreSQL instance for further use. Since the ideas change once every 24 hours on the primary website so I made use of Cron Job to add entries into database every 24 hours. Every 2 hours I run a different Cron Job to post the idea onto Twitter using their API. 

- While building the project I have learnt about so many things on the go, I never known that Twitter allows people to write tweets in a programmatic way. Upon going to the developer tab I found there are different libraries for different languages. I have learnt about Cron Jobs, hosting the python application on Heroku for cloud automation.

- I have chosen Flask as a quick hack to simplify the trigger process with a function call which can be easily ported to normal python application.
