from itertools import combinations
from apriori_python import apriori
import api_calls
import api_calls

def findmatch(rules, user):
    allcombinations, movie_ids = get_user_combinations(api_calls.get_user_movie_ids(user))
    #print(f"All movie_ids are {movie_ids}")
    #print(f"all combinations for user {user} are {allcombinations}")
    movie_recommendations = []
    
    for rule in rules:
        antecedent, consequent, confidence = rule
        
        for combination in allcombinations:
            if set(antecedent) == set(combination):
                movie_recommendations.extend(consequent)
    
    return movie_recommendations, movie_ids 
def get_user_combinations(movie_ids):
    allcombinations = []
    max_range = len(movie_ids) + 1
    if max_range > 3:
        max_range = 3
    for r in range(2, max_range):
        allcombinations.extend(list(combinations(movie_ids,r)))
    return allcombinations, movie_ids

def filter_watched(recommendations, movie_ids):
    recommendations = set(recommendations)
    movie_ids = set(movie_ids)
    return list(recommendations - movie_ids)


