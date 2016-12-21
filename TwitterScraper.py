# Author : George Poulos
# Version : 1.0
#
# Description : This serves as an API for twitter, getting the top 20 most popular tweets
#
#

from bs4 import BeautifulSoup
import requests

url = 'https://twitter.com/'
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
soup = BeautifulSoup(response.content,"html.parser" )

uName = list()
posts = list()

tableEntries = soup.select('div.Grid div.tweet')

for (li) in tableEntries:
    try:
        curr = str(li)
        soup2 = BeautifulSoup(curr, "html.parser")
        filterForUserName = soup2.select('span.username')
        user = filterForUserName[0].text.strip().rstrip(':')
        uName.append(user)

        filterForPost = soup2.select('div.js-tweet-text-container p.TweetTextSize')
        tweetkey = filterForPost[0].text.strip().rstrip(':')
        tweet = tweetkey.replace('\n','')
        posts.append(tweet)

    except AttributeError:
        break

#print table of info
fmt = '{:<10}{:<40}{}'
for i, (user, post) in enumerate(zip(uName, posts)):
    print(fmt.format(i, user, post))
