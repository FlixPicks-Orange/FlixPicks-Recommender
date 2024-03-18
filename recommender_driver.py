import calls 
import recommender
import os, requests
from apriori_python import apriori
import time, schedule
#print(calls.get_user_ids())

time.sleep(5)
repeater = .15
"""print("movie_ids is:")
print(calls.get_movie_ids())

print("get_user_ids is:")
print(calls.get_user_ids())

print("get_user_movie_ids for 1 is:")
print(calls.get_user_movie_ids(1))

print("get_user_movie_ids for 2 is:")
print(calls.get_user_movie_ids(2))

print("get users since login is")
print(calls.get_users_since_login())"""

minSup = .3
minConf = .4



def recommendmovie():
    movierecommendations = []

    itemSetList = calls.get_movie_ids()

    freqItemSet, rules = apriori(itemSetList, minSup, minConf)
    
    #print(f"Rules are {rules}")

    #print(f"Freq item set list is {freqItemSet}")
    users = calls.get_user_ids()
    #print(users)
    for user in users:
        movierecommendations, movie_ids = recommender.findmatch(rules, user)
        #print(f"User {user} movie recommendations are {movierecommendations}, their movie_ids are {movie_ids}")
        movierecommendations = recommender.filter_watched(movierecommendations, movie_ids)
        #print(f"User {user} movie recommendations after filter are {movierecommendations}, their movie ids are {movie_ids}")
        if len(movierecommendations) > 0:
            calls.post_recommendations(user, movierecommendations)

schedule.every(repeater).minutes.do(recommendmovie)
while True:
    schedule.run_pending()
    time.sleep(20)

        
