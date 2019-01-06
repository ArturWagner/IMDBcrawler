import urllib3
import re
import json
from bs4 import BeautifulSoup

def directorParse(directorLink):
  http = urllib3.PoolManager()
  directorPage = http.request(
    'GET',
    'https://www.imdb.com' + directorLink
  )
  directorInfo = BeautifulSoup(directorPage.data, 'html.parser')
  director = { 
    'Name' : directorInfo.find('h1', class_= 'header').text.strip(),
    'Ranking' : directorInfo.find('a', id = 'meterRank').text.strip(),
    'Born' : directorInfo.find('div', id = 'name-born-info').a.text.strip(),
    'From' : directorInfo.find('div', id = 'name-born-info').find_all('a')[2].text
  }

  return director
   