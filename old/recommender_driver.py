import recommender
import datetime
import schedule
import sqlite3
import time
import requests, os
#global db variable
database_path = 'databasev1.db'
minSup = .3
minConf = .4

repeater = .15
testvar = datetime.datetime.now()
def recommendmovie():
    movierecommendations = []

    itemSetList = recommender.load_data(database_path)
    freqItemSet, rules = recommender.apriori(itemSetList, minSup, minConf)
    movierecommendation = []
    for user in user_list():
       
        movierecommendation, user_titles = recommender.findmatch(rules, user, database_path)
        movierecommendation = recommender.filter_out_watched(movierecommendation, user_titles)
        movierecommendations.append(movierecommendation)



    #print(movierecommendations)
    #return movierecommendations

def user_list():    
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    userlist = [1,2,3,4,5,6,7,8,9]
    initiallist = recommender.get_user_ids(database_path)
        

    conn.close()
    return userlist

def time_difference(last_login):
    current_time = datetime.datetime.now()
    time_difference = current_time - last_login
    print(current_time)
    print(last_login)
    print(time_difference)


#A proposed system to run every x minutes
schedule.every(repeater).minutes.do(recommendmovie)
while True:
    schedule.run_pending()
    time.sleep(1)