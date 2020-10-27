import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def create_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):            
            points = int(vote[0].getText().replace(' points',''))
            print(points)
            hn.append({'title': title, 'link': href, 'votes': points})
    return hn


create_custom_hn(links, subtext)