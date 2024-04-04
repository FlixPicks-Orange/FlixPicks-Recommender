from itertools import combinations
from apriori_python import apriori
import random
import sqlite3
import os
import requests
#Uses apriori_python 



def load_data(database_path):
    #Loads data from database watch history

    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    users = get_user_ids(database_path)
    query = "SELECT user_id, GROUP_CONCAT(movie_id) FROM watch_history WHERE user_id IN ({}) GROUP BY user_id".format(','.join('?'*len(users)))
    c.execute(query, users)
    rows = c.fetchall()

    dataset = [(tuple(row[1].split(','))) for row in rows]
    titleset = []
    for movie_ids in dataset:
        title_ids = []
        for movie_id in movie_ids:
            title_ids.append(str(movie_id))
        titleset.append(tuple(title_ids))
    #Test Print
    #print(titleset)
    conn.close()
    return titleset




#Queries database for all user_ids in watch_history to be able to get each transaction
#Gets the users, currently prints them as well
def get_user_ids(database_path):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    query = "SELECT DISTINCT user_id FROM watch_history"
    c.execute(query)
    rows = c.fetchall()
    
    user_ids = [row[0] for row in rows]
    

    conn.close()

    return user_ids

#Creates a list of titles of a specific users history
def get_user_titles(database_path, user_id):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    query = "SELECT movie_id FROM watch_history WHERE user_id = ?"
    c.execute(query, (user_id,))
    result = c.fetchall()
    movies = [row[0] for row in result]
    #print(movies)
    conn.close()
    return movies


#Makes a combination list of that user, limiting to groups of 2, change max_range if you want to change this
def get_user_combinations(titles):
    allcombinations = [f"['{title}']" for title in titles]
    max_range = len(titles)+1
    if max_range > 3:
        max_range = 3
    for r in range(2, max_range):
        allcombinations.extend(list(combinations(titles, r)))
    #for combination in allcombinations:
        #print(combination)
    #print(allcombinations)
    return allcombinations, titles


def findmatch(rules, user_id,database_path):

    user_data, user_titles = get_user_combinations(get_user_titles(database_path, user_id))
    recommendations = []
    for rule in rules:
            
        antecedent, consequent, confidence = rule
        
        for combination in user_data:
   
            if set(antecedent) == set(combination):    
                recommendations.extend(consequent)

    return recommendations,user_titles



    




def filter_out_watched(recommendations, user_titles):
    recommendations = set(recommendations)
    watched_titles = set(user_titles)
    return list(recommendations - watched_titles)



