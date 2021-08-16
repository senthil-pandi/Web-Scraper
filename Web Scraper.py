import requests
from bs4 import BeautifulSoup
#pprint stands for pretty print which is used to print your output prettier
import pprint

#We are getting the required data from the website using reqquests module
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

#we are creating two soup objects to store the data we got as html
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

#here we are grabbing the links responsible for the required elements we need to scrap
links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hacker_news_list):
  '''This function sorts the list of links we scraped'''
  return sorted(hacker_news_list, key= lambda k:k['votes'], reverse=True)

def create_custom_hacker_news(links, subtext):
  '''This is our main function responsible for 
  grabbing the news feeds having votes more than 99'''
  hacker_news = []
  for index, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[index].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hacker_news.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hacker_news)
 
pprint.pprint(create_custom_hacker_news(mega_links, mega_subtext))
