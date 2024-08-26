import time

import requests
from bs4 import BeautifulSoup
import pprint

base_url = 'https://news.ycombinator.com/news'

res = requests.get(base_url)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)
def create_custom_hn(hn_links,hn_subtext):
    hn = []

    for idx, item in enumerate(hn_links):
        title = hn_links[idx].getText()
        href = hn_links[idx].find('a')['href']
        vote = hn_subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points',''))
            if points > 99:
                hn.append({'title':title,'link':href,'votes':points})


    return sort_stories_by_votes(hn)



# pprint.pprint(create_custom_hn(links,subtext))
pprint.pprint(create_custom_hn(links,subtext))



next_url = soup.find('a', {'class': 'morelink'})
if next_url:
    next_page_url = base_url + next_url['href']
    time.sleep(15)
    next_page_res = requests.get(next_page_url)
    next_page_soup = BeautifulSoup(next_page_res.text, 'html.parser')
    next_page_links = next_page_soup.select('.titleline')
    next_page_subtext = next_page_soup.select('.subtext')

    pprint.pprint(create_custom_hn(next_page_links,next_page_subtext))
