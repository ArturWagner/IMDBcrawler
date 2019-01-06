import json
import math
import string

# Open json file
with open('crawler/filmResult.json') as json_data:
  films_json = json.load(json_data)
# Avg Time
filmTimes = []

for film in films_json:
  try:
    hour,minutes = film['FilmTime'].split("h")
    minutes = minutes.strip('min')
    duration = (int(hour)*60 + int(minutes))
    filmTimes.append(duration)
  except:
    0

timesum = 0

for filmTime in filmTimes:
  timesum += filmTime

avg = timesum / float(len(filmTimes))

# Prob Film Rating > 8 /genre

def probFilmRating(genre):
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

  nRatingValues = float(len(allRatingValues))  
  nHighRatingValues = len(highRatingValues)
  probRatingValues = (nHighRatingValues / nRatingValues )*100

  return ("%.2f" % probRatingValues)

# Running probability to all genres
 
allGenres = []
probGenres = []

for film in films_json:
  if film['Genre'] == 'No film genre':
    pass
  else:
    allGenres.append(film['Genre'])

for genre in set(allGenres):
  finalGenreRating = [genre, str(probFilmRating(genre)) + '%']
  probGenres.append(finalGenreRating)
