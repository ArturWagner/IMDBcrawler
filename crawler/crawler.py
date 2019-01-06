import urllib3
import json
from bs4 import BeautifulSoup
from filmparse import filmParse

films = []

# Every page has 100 films to get a sample to start the app run the crawler with a few pages
for page in range(1,55):
  http = urllib3.PoolManager()
  response = http.request(
    'GET',
    ('https://www.imdb.com/list/ls057823854/?sort=list_order,asc&st_dt=&mode=detail&page=%d' % page)
    )
  html = BeautifulSoup(response.data, 'html.parser')
  for link in html.find_all('h3', class_ = 'lister-item-header'):
    filmPage = http.request(
      'GET',
      'https://www.imdb.com' + link.a.get('href')
    )
    filmInfo = BeautifulSoup(filmPage.data.decode('utf-8'), 'html.parser')
    film = filmParse(filmInfo)
    films.append(film)
  
with open('../filmResult.json', 'w') as outfile:
    json.dump(films, outfile)