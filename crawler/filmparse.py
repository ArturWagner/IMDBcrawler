import re
from bs4 import BeautifulSoup
from directorparse import directorParse

def Title(filmInfo):
  try:
    title = filmInfo.find('div', class_= 'title_wrapper').h1.text.strip()
  except:
    title = 'No title'
  return title

def RatingValue(filmInfo):
  try:
    ratingValue = filmInfo.find('span', itemprop = 'ratingValue').text
    ratingValue = re.sub('[a-zA-Z]', '', ratingValue)
  except:
    ratingValue = 'No rating value'
  return ratingValue

def RatingCount(filmInfo):  
  try:
    ratingCount = filmInfo.find('span', itemprop = 'ratingCount').text.strip()
    ratingCount = re.sub('[a-zA-Z]', '', ratingCount)
  except:
    ratingCount = 'No rating count'
  return ratingCount
  
def FilmTime(filmInfo):
  try:
    time = filmInfo.time.text.strip()
  except:
    time = 'No film time'
  return time

def FilmGenre(filmInfo):
  try:
    genre = filmInfo.time.find_next('a').text.strip()
  except:
    genre = 'No film genre'
  return genre

def Director(filmInfo):
  try:
    directorLink = filmInfo.find('h4',text = re.compile(r'Director:')).find_next('a').get('href')
    director = directorParse(directorLink)
  except:
    director = 'No Director'
  return director

def filmParse(filmInfo):    
  film = {
    'Title' : Title(filmInfo),
    'RatingValue' : RatingValue(filmInfo),
    'RatingCount' : RatingCount(filmInfo),
    'FilmTime' : FilmTime(filmInfo),
    'Genre' : FilmGenre(filmInfo),
    'Director' : Director(filmInfo)
    }
  print film

  return film