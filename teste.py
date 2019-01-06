import json
import math
import string

# Open json file
with open('crawler/filmResult.json') as json_data:
  films_json = json.load(json_data)

allgenres = []

def avgFilmRating(genre):
  allRatingValues = []
  highRatingValues = []

  for film in films_json:
    try:
      if genre == film['Genre']:
        allRatingValues.append(float(film['RatingValue']))
    except:
      pass

  for value in allRatingValues:
    if value >= 8:
      highRatingValues.append(value)
  
  avgRatingValues = str((len(highRatingValues) / float(len(allRatingValues)))*100) + '%'

  return avgRatingValues


for film in films_json:
  allgenres.append(film['Genre'])

setgenres = set(allgenres)

print setgenres

print avgFilmRating('Mystery')