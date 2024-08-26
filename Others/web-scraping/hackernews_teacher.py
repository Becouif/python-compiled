import requests
from bs4 import BeautifulSoup

import pprint


res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# this already beautiful data compare to from requests
# print(soup)

# we can be this to get a tag
# print(soup.body)

# bring the first element in the body
# print(soup.find('a'))

# we can find using id in the html
# print(soup.find(id=''))

# using select allow using css selector
# one of the best way to access
# select work on class, html tag, id, and so on
# to get first element since its a list
# print(soup.select('.titleline')[0])

links = soup.select('.titleline')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)
def create_custom_hn(hn_links,hn_subtext):
    hn = []
    # if we dont use enumerate we can use len(hn_links)
    #     orelse we cant get the index of the list
    for idx, item in enumerate(hn_links):
        title = hn_links[idx].getText()
        href = hn_links[idx].find('a')['href']
        # print(href)
        vote = hn_subtext[idx].select('.score')
        if len(vote):

            # convert the points to int
            points = int(vote[0].getText().replace('points',''))
            if points > 99:
                hn.append({'title':title,'link':href,'votes':points})
    return sort_stories_by_votes(hn)


# we can print with pprint for better readability
pprint.pprint(create_custom_hn(links,subtext))

# create_custom_hn(links,subtext)