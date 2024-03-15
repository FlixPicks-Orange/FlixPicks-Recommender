import os, requests, json

def get_user_ids():
    r = requests.get(os.getenv('DB_URL') + "/watch_history")
    if(r.status_code == 200): 
        unique_user_ids = set()
        for record in r.json():
            unique_user_ids.add(record['user_id'])


    #this is my user_ids
    print(list(unique_user_ids))
    return list(unique_user_ids)

def get_movie_ids():
    movie_ids = {}

    #Gets our request, and builds all the movie_ids to be associated in lists with the proper user
    r = requests.get(os.getenv('DB_URL') + "/watch_history")
    if(r.status_code == 200):
        data_str = r.content.decode('utf-8')
        json_data = json.loads(data_str)
        for entry in json_data:
            print(entry)
            print("\n")
            user_id = entry['user_id']
            movie_id = entry['movie_id']
            if user_id not in movie_ids:
                movie_ids[user_id] = []
            movie_ids[user_id].append(movie_id)
    return tuple(movie_ids.values())

    

            
    return movie_ids

def get_user_movie_ids(user_id):
    movie_ids = {}
    """
    THIS NEEDS TO BE SWITCHED TO A DIRECT API CALL FOR JUST A USER_IDS WATCH HISTORY
    """
    #Gets our request, and builds all the movie_ids to be associated in lists with the proper user
    r = requests.get(os.getenv('DB_URL') + "/watch_history")
    if(r.status_code == 200):
        data_str = r.content.decode('utf-8')
        json_data = json.loads(data_str)
        for entry in json_data:
            print(entry)
            print("\n")
            user_id = entry['user_id']
            movie_id = entry['movie_id']
            if user_id not in movie_ids:
                movie_ids[user_id] = []
            movie_ids[user_id].append(movie_id)

    return movie_ids.get(user_id)

def get_users_since_login():
    logged_in_users = []
    logged_in_users = [1,2]
    return logged_in_users

