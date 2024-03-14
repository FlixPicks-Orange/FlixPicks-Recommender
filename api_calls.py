import os, requests

def get_user_ids():
    r = requests.get(os.getenv('DB_URL') + "/watch_history/")
    if(r.status_code == 200): 
        unique_user_ids = set()
        for record in r.json():
            unique_user_ids.add(record['user_id'])


    #this is my user_ids
    print(list(unique_user_ids))
    return list(unique_user_ids)

def get_movie_ids():
    movie_ids = []
    user_movie_ids = (1,2,3,4)
    user_movie_ids2 = (1,4,5,2,3)
    movie_ids.append(tuple(user_movie_ids))
    movie_ids.append(tuple(user_movie_ids2))
    movie_ids.append(tuple(user_movie_ids))
    movie_ids.append(tuple(user_movie_ids2))
    movie_ids.append(tuple(user_movie_ids))
    movie_ids.append(tuple(user_movie_ids2))
    movie_ids.append(tuple(user_movie_ids))
    movie_ids.append(tuple(user_movie_ids2))
    return movie_ids

def get_user_movie_ids(user_id):
    user_movie_ids = []

    movie_ids = get_movie_ids()
    user_movie_ids = movie_ids[user_id - 1]
    print(f"For user {user_id} their ids are {user_movie_ids}")
    return user_movie_ids

def get_users_since_login():
    logged_in_users = []
    logged_in_users = [1,2]
    return logged_in_users

