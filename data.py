import sqlite3 as sql

genres = {
    
    'Action' : 1023,
    'Romance' : 5034,
    'Drama' : 5235,
    'Sci-Fi' : 1241,
    'Comedy' : 9043
      
    }
 
user_data = [
    ('John Doe', 'john@aol.com'),
    ('kathy doe', 'kathy@email.com')




]

movies_data = [
    ('Batman', 1023),
    ('The Notebook', 5034),
    ('Intersteller', 1241),
    ('Bobs Burgers the movie', 9043)


]

watch_history_data = [




]
def insertgenres(dbname, data):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.executemany("INSERT INTO genre (title, id) VALUES (?, ?)", [(genre_title,genre_id ) for genre_title,genre_id  in data.items()])
    conn.commit()
    conn.close()

def insertmovies(dbname, data):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.executemany("INSERT INTO movies (title, genre_id) VALUES (?,?)", data)
    conn.commit()
    conn.close()
def insertuser(dbname, data):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.executemany("INSERT INTO user (name, email) VALUES (?,?)", data)
    conn.commit()
    conn.close()   
dbname = 'databasev1.db'
"""insertgenres(dbname, genres)
insertmovies(dbname, movies_data)
insertuser(dbname, user_data)"""

#Watch History Driver

moreusers = {
    ('Alice Johnson', 'alice@gmail.com'),
    ('Bob Smith', 'bob@yahoo.com'),
    ('Charlie Brown', 'charlie@hotmail.com'),
    ('David Williams', 'david@gmail.com'),
    ('Emma Davis', 'emma@yahoo.com'),
    ('Frank Miller', 'frank@gmail.com'),
    ('Grace Taylor', 'grace@hotmail.com'),
    ('Henry Wilson', 'henry@gmail.com'),
    ('Ivy Lee', 'ivy@yahoo.com')

}
moremovies = [
    ('Avengers', 1023),
    ('Pride and Prejudice', 5034),
    ('Inception', 1241),
    ('Superbad', 9043),
    ('Die Hard', 1023),
    ('La La Land', 5034),
    ('The Matrix', 1241),
    ('Bridesmaids', 9043),
    ('Spider-Man: Into the Spider-Verse', 1023),
    ('The Fault in Our Stars', 5034),
    ('E.T. the Extra-Terrestrial', 1241),
    ('Anchorman', 9043),
    ('Jurassic Park', 1023),
    ('Casablanca', 5034),
    ('Blade Runner', 1241),
    ('The Hangover', 9043)
]
#movies 1-20
#people 1-11

watchhistory = [
        (1, 'Batman', 1),
        (1, 'The Notebook', 2),
        (1, 'Intersteller', 3),
        (1, 'Bobs Burgers the movie', 4),
        (1, 'Avengers', 5),
        (1, 'Pride and Prejudice', 6),
        (1, 'Inception', 7),
        (1, 'Superbad', 8),
        (1, 'Die Hard', 9),
        (1, 'La La Land', 10),
        (1, 'The Matrix', 11),
        (1, 'Bridesmaids', 12),
        (1, 'Spider-Man: Into the Spider-Verse', 13),
        (1, 'The Fault in Our Stars', 14),
        (1, 'E.T. the Extra-Terrestrial', 15),
        (1, 'Anchorman', 16),
        (1, 'Jurassic Park', 17),
        (1, 'Casablanca', 18),
        (1, 'Blade Runner', 19),
        (1, 'The Hangover', 20),
        (2, 'Batman', 1),
        (2, 'Avengers', 5),
        (2, 'Spider-Man: Into the Spider-Verse', 13),
        (11, 'The Fault in Our Stars', 14),
        (11, 'Pride and Prejudice', 6),
        (11, 'The Notebook', 2),
        (10, 'The Fault in Our Stars', 14),
        (10, 'Pride and Prejudice', 6),
        (10, 'The Notebook', 2),
        (10, 'Batman', 1),
        (10, 'Avengers', 5),
        (10, 'Spider-Man: Into the Spider-Verse', 13),
        (3, 'Batman', 1),
        (3, 'Avengers', 5),
        (3, 'La La Land', 10),
        (3, 'The Matrix', 11),
        (4, 'Batman', 1),
        (4, 'Avengers', 5),
        (4, 'Spider-Man: Into the Spider-Verse', 13),
        (4, 'Anchorman', 16),
        (4, 'Jurassic Park', 17),
        (4, 'Casablanca', 18),



]

def insertwatchhistory(dbname, data):
    conn = sql.connect(dbname)
    c = conn.cursor()
    c.executemany("INSERT INTO watch_history (user_id, title, movie_id) VALUES (?,?,?)", data)
    conn.commit()
    conn.close()   



morewatch = [
        (5, 'Batman', 1),
        (5, 'Avengers', 5),
        (5, 'La La Land', 10),
        (5, 'The Matrix', 11),
        (6, 'Batman', 1),
        (6, 'Avengers', 5),
        (6, 'Spider-Man: Into the Spider-Verse', 13),
        (6, 'Anchorman', 16),
        (6, 'Jurassic Park', 17),
        (6, 'Casablanca', 18),
        (5, 'Batman', 1),
        (7, 'Avengers', 5),
        (7, 'La La Land', 10),
        (7, 'The Matrix', 11),
        (8, 'Batman', 1),
        (8, 'Avengers', 5),
        (8, 'Spider-Man: Into the Spider-Verse', 13),
        (8, 'Anchorman', 16),
        (8, 'Jurassic Park', 17),
        (8, 'Casablanca', 18),
]

#insertwatchhistory(dbname, morewatch)


data = [
    (9, 'Batman', 1),
    (9, 'Avengers', 5)
]
insertwatchhistory(dbname, data)