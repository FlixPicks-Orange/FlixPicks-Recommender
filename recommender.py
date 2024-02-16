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
    print(dataset)
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
    print(titleset)
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
    """    names_of_users = []
 
    for user in user_ids:
        c.execute("SELECT name FROM user WHERE id = ?", (int(user),))
        name = c.fetchone()
        names_of_users.append(name)
    #print(names_of_users)"""
    conn.close()
    #Test Print
    #print(user_ids)
    return user_ids

#Creates a list of titles of a specific users history
def get_user_titles(database_path, user_id):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    query = "SELECT m.title FROM movies m JOIN watch_history wh ON m.id = wh.movie_id WHERE wh.user_id = ?"
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
    return allcombinations, titles


def findmatch(rule_dictionary, user_id,database_path):
    #Query database for a list of all watch history 
    #Make a structure of that
    #Hunter, this does NOT need changed
    user_data, user_titles = get_user_combinations(get_user_titles(database_path, user_id))
    #End don't touch

    # NEW CODE
    # The modification reduces the time complexity from O(n^2) to O(n) by eliminating the nested loop. 
    # With the modified code, we iterate over the rules once, and for each rule, we find the matching users in user_data using a list comprehension.
    # If there are matching users, it extends the recommendations list with the consequent and confidence values.

    # Initialize an empty list to store recommendations
    recommendations = []

    # Iterate over each combination in the user data
    for combination in user_data:
        # Check if the combination's antecedent is in the rule dictionary
        antecedent = tuple(combination)
        if antecedent in rule_dictionary:
            # If there is a match, add the consequents to the recommendations list
            recommendations.extend([(consequent, confidence) for consequent, confidence in rule_dictionary[antecedent]])

    # Return the list of recommendations and the user titles
    return recommendations, user_titles


''' OLD CODE
    #Hunter, update this logic to reflect using a dictionary
    #This should allow us to get rid of this nested loop
    #The combination here reflects the key to the dictionary, it should match an antecedent, when it does that means two users have watched the same x amount of shows
    #That leads to the values of the dictionary, or consequent, the theme of what content they would also like to watch based on the apriori algorithm
    #Store the values retrieved all into a single list or set (probably set to get rid of duplicates)
    #This should help improve the efficiency of the code


    #If structure contains antecedent check for consequent
    recommendations = []
    for rule in rules:
        
        antecedent, consequent, confidence = rule
       
        for combination in user_data:
            
            if set(antecedent) == set(combination):
                
                recommendations.extend(consequent)

    return recommendations,user_titles

 END OF OLD CODE '''


def filter_out_watched(recommendations, user_titles):
    recommendations = set(recommendations)
    watched_titles = set(user_titles)
    return list(recommendations - watched_titles)

def recommended_was_watched(user):
    watched_content = []
    recommended_content = []
    #I need to set everything that is in both recommended and watched to true 


