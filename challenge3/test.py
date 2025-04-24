import unittest
from challenge import find_action_movies

class TestFindActionMovies(unittest.TestCase):
    def test_find_action_movies(self):
        expected_result = [('Avatar', '2009'), ('300', '2006'), ('The Avengers', '2012'), ('Vikings', '2013–'), ('Gotham', '2014–'), ('Doctor Strange', '2016'), ('Rogue One: A Star Wars Story', '2016'), ("Assassin's Creed", '2016'), ('Luke Cage', '2016–')]
        self.assertEqual(find_action_movies(), expected_result)

if __name__ == '__main__':
    unittest.main()