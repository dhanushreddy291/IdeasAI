import requests, json, time
from bs4 import BeautifulSoup

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def get_a_quote():
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
        if i == 4:
            index5 = int(a)
        elif i == 5:
            f = open("read.json", "w")
            f.write(str(price)[index5 + 46:a])
        i += 1

get_a_quote()
f = open('read.json')
data = json.load(f)

f = open("ideas.txt", "w")
f.write("")
f.close()

for quoteData in data["itemListElement"]:
    f = open("ideas.txt", "a")
    f.write(quoteData['item']['name'] + "\n")
    print(quoteData['item']['name'])