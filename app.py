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
    query = "SELECT movie_id FROM watch_history WHERE user_id IN ({})".format(','.join('?'*len(users)))
    c.execute(query, users)
    rows = c.fetchall()
    conn.close()

    dataset = str([[row[0] for row in rows]])

    return dataset


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
    return user_ids


def findmatch(rules):
    #Query database for a list of all watch history

    #Make a structure of that

    #If structure contains antecedent check for consequent

    #
    for rule in rules:
        antecedent, consequent, confidence = rule
        antecedent_list = list(antecedent)
        if len(antecedent) == 1:
            print(antecedent)
    


    


def recommendmovie():
    movierecommendations = []
    database_path = 'databasev1.db'
    itemSetList = load_data(database_path)
    print(itemSetList)
    freqItemSet, rules = apriori(itemSetList, minSup=.2, minConf=.5)
    findmatch(rules)
    print(rules)
    print(freqItemSet)
    return movierecommendations

recommendmovie()