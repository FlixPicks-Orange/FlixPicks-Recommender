from itertools import combinations
from apriori_python import apriori
import calls

def findmatch(rules, user):
    allcombinations, movie_ids = get_user_combinations(calls.get_user_movie_ids(user))
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
    #print(movie_ids)
    allcombinations = []
    max_range = len(movie_ids) + 1
    if max_range > 3:
        max_range = 3
    for r in range(2, max_range):
        allcombinations.extend(list(combinations(movie_ids,r)))
    return allcombinations, movie_ids

def filter_watched(recommendations, movie_ids):
    changed_watched = [int(movie) for movie in movie_ids]
    set_watched = set(changed_watched)
    
    changed_recommendations = [int(movie) for movie in recommendations]
    set_recommendations = set(changed_recommendations)

    return set_recommendations - set_watched

def filter_recommended(recommendations, user):
    previous_recommended = calls.get_recommendaitons(user)
    set_previousrecommended = set(previous_recommended)
    set_recommended = set(recommendations)

    return set_recommended - set_previousrecommended



