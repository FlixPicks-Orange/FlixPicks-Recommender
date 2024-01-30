from itertools import combinations
from apriori_python import apriori
import random
import sqlite3

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
    #Test Print
    #print(dataset)
    query = "SELECT title FROM movies WHERE id = ? "
    #Title set is all the users TUPLES combined
    titleset = []
    #Turns our dataset into movie titles form movie ids

    for movie_ids in dataset:
        #Titles is all the movies for an individual USER as a tuple
        titles = []
        for movie_id in movie_ids:
            #Test Print
            #print(movie_id)
            c.execute(query, (movie_id,))
            title = c.fetchone()
            #Adds one movie the a users list
            titles.append(title[0])
        #Adds all a users movies to the master list    
        titleset.append(tuple(titles))

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
    #print(user_ids)
    names_of_users = []
 
    for user in user_ids:
        c.execute("SELECT name FROM user WHERE id = ?", (int(user),))
        name = c.fetchone()
        names_of_users.append(name)
    #print(names_of_users)
    conn.close()
    #Test Print
    #print(user_ids)
    return user_ids


def findmatch(rules, user_id):
    #Query database for a list of all watch history

    #Make a structure of that

    #If structure contains antecedent check for consequent

    #
    for rule in rules:
        antecedent, consequent, confidence = rule
        antecedent_list = list(antecedent)
        print(antecedent)
    


    


def recommendmovie():
    movierecommendations = []
    database_path = 'databasev1.db'
    itemSetList = load_data(database_path)
    #print("ItemSetlist is")
    #print(itemSetList)
    freqItemSet, rules = apriori(itemSetList, minSup=.5, minConf=.5)
    findmatch(rules)
    print("rules are")
    print(rules)
    print("Freq Item set")
    print(freqItemSet)
    return movierecommendations

recommendmovie()