import unittest
from bs4 import BeautifulSoup
from filmparse import Title, RatingValue, RatingCount, FilmTime, FilmGenre

class TestFilmParse(unittest.TestCase):

  def test_filmHasTitle(self):
    # Test if film has title
    noTitle = BeautifulSoup('<div><h1></h1></div>', 'html.parser')
    filmtitle = BeautifulSoup('<div class="title_wrapper"><h1>title</h1></div>', 'html.parser')
    self.assertEqual(Title(noTitle), 'No title') 
    self.assertEqual(Title(filmtitle), 'title')
  
  def test_filmHasRatingValue(self):
    # Test if film has ratingValue
    noRatingValue = BeautifulSoup('<div><span></span></div>', 'html.parser')
    filmRatingValue = BeautifulSoup('<div><span itemprop="ratingValue">1.0e</span></div>', 'html.parser') 
    self.assertEqual(RatingValue(noRatingValue), 'No rating value')
    self.assertEqual(RatingValue(filmRatingValue), '1.0')
  
  def test_filmHasRatingCount(self):
    # Test if film has ratingCount
    noRatingCount = BeautifulSoup('<div><span></span></div>', 'html.parser')
    filmRatingCount = BeautifulSoup('<div><span itemprop="ratingCount">33214</span></div>', 'html.parser')
    self.assertEqual(RatingCount(noRatingCount), 'No rating count') 
    self.assertEqual(RatingCount(filmRatingCount), '33214')

  def test_filmHasFilmTime(self):
    # Test if film has filmTime
    noFilmTime = BeautifulSoup('<div></div>', 'html.parser')
    filmTime = BeautifulSoup('<time>1h 50min</time>', 'html.parser')
    self.assertEqual(FilmTime(noFilmTime), 'No film time') 
    self.assertEqual(FilmTime(filmTime), '1h 50min')
  
  def test_filmHasGenre(self):
    noGenre = BeautifulSoup('<div><time></time></div>', 'html.parser')
    filmGenre = BeautifulSoup('<div><time></time><a>Action</a></div>', 'html.parser')
    self.assertEqual(FilmGenre(noGenre), 'No film genre') 
    self.assertEqual(FilmGenre(filmGenre), 'Action')

if __name__ == '__main__':
  unittest.main()
