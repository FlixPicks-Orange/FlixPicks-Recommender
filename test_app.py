from app import filter_out_watched
import unittest

class TestFilterOutWatched(unittest.TestCase):

    def test_empty_reccomendations(self):
        reccomendations = []
        user_titles = ['Movie1', 'Movie2']
        result = filter_out_watched(reccomendations, user_titles)
        self.assertEqual(result, [])
    def test_empty_watchlist(self):
        reccomendations = ['Movie1' , 'Movie2']
        user_titles = []
        result = filter_out_watched(reccomendations, user_titles)
        self.assertEqual(result, reccomendations)

if __name__ == '__main__':
    unittest.main()