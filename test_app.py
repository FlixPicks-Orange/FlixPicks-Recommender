from recommender import filter_out_watched
import unittest

class TestFilterOutWatched(unittest.TestCase):

    def test_empty_reccomendations(self):
        reccomendations = []
        user_titles = ['Movie1', 'Movie2']
        result = filter_out_watched(reccomendations, user_titles)
        self.assertCountEqual(result, [])
    def test_empty_watchlist(self):
        reccomendations = ['Movie1' , 'Movie2']
        user_titles = []
        result = filter_out_watched(reccomendations, user_titles)
        self.assertCountEqual(result, reccomendations)
    def test_no_common_titles(self):
        reccomendations = ['Movie1' , 'Movie2']
        user_titles = ['Movie3']
        result = filter_out_watched(reccomendations, user_titles)
        self.assertCountEqual(result, reccomendations)
    def test_some_common_titles(self):
        reccomendations = ['Movie1' , 'Movie2']
        user_titles = ['Movie2','Movie3']
        result = filter_out_watched(reccomendations, user_titles)
        self.assertCountEqual(result, ['Movie1'])
    def test_all_common_titles(self):
        reccomendations = ['Movie1' , 'Movie2']
        user_titles = ['Movie1' , 'Movie2']
        result = filter_out_watched(reccomendations, user_titles)
        self.assertCountEqual(result, [])

if __name__ == '__main__':
    unittest.main()