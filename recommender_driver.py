import api_calls 
import recommender
import os, requests
from apriori_python import apriori

#print(api_calls.get_user_ids())

def get_all():
    r = requests.get(os.getenv('DB_URL') + "/watch_history")
    print(r.status_code)
    if(r.status_code == 200): return r.json()
    else: return None

print(get_all())
"""print("movie_ids is:")
print(api_calls.get_movie_ids())

print("get_user_ids is:")
print(api_calls.get_user_ids())

print("get_user_movie_ids for 1 is:")
print(api_calls.get_user_movie_ids(1))

print("get_user_movie_ids for 2 is:")
print(api_calls.get_user_movie_ids(2))

print("get users since login is")
print(api_calls.get_users_since_login())"""

minSup = .3
minConf = .4



def recommendmovie():
    movierecommendations = []

    itemSetList = api_calls.get_movie_ids()
    freqItemSet, rules = apriori(itemSetList, minSup, minConf)
    
    print(f"Rules are {rules}")

    print(f"Freq item set list is {freqItemSet}")
    
    for user in api_calls.get_user_ids():
        movierecommendations, movie_ids = recommender.findmatch(rules, user)
        print(f"User {user} movie recommendations are {movierecommendations}, their movie_ids are {movie_ids}")
        recommender.filter_watched(movierecommendations, movie_ids)
        print(f"User {user} movie recommendations after filter are {movierecommendations}, their movie ids are {movie_ids}")
#recommendmovie()
        
