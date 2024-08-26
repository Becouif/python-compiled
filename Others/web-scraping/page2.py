import requests
from bs4 import BeautifulSoup
import time
import pprint

base_url ='https://news.ycombinator.com/news'
res = requests.get(base_url)
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')


next_url = soup.find('a', {'class': 'morelink'})
mega_links = links
mega_subtext = subtext
if next_url:
    next_page_url = base_url + next_url['href']
    time.sleep(15)
    next_page_res = requests.get(next_page_url)
    next_page_soup = BeautifulSoup(next_page_res.text, 'html.parser')
    next_page_links = next_page_soup.select('.titleline')
    next_page_subtext = next_page_soup.select('.subtext')

# join the two lists
    mega_links = links + next_page_links
    mega_subtext = subtext + next_page_subtext


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
pprint.pprint(create_custom_hn(mega_links,mega_subtext))

# create_custom_hn(links,subtext)