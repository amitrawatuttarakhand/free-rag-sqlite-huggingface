import sqlite3

def init_db():
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        title TEXT,
        year INTEGER,
        genre TEXT,
        description TEXT,
        director TEXT
    )
    """)

    sample_movies = [
        ("The Matrix", 1999, "Sci-Fi", "A hacker discovers reality is a simulation.", "Wachowski"),
        ("Inception", 2010, "Sci-Fi, Thriller", "A thief enters dreams to steal secrets.", "Christopher Nolan"),
        ("Interstellar", 2014, "Sci-Fi, Drama", "Explorers travel through a wormhole to save humanity.", "Christopher Nolan"),
        ("The Dark Knight", 2008, "Action, Crime, Drama", "Batman faces the Joker in Gotham.", "Christopher Nolan"),
        ("Titanic", 1997, "Romance, Drama", "A love story unfolds aboard the ill-fated RMS Titanic.", "James Cameron"),
        ("Avatar", 2009, "Sci-Fi, Adventure", "Humans exploit Pandora while a soldier joins the Na'vi.", "James Cameron"),
        ("Gladiator", 2000, "Action, Drama", "A betrayed Roman general seeks revenge.", "Ridley Scott"),
        ("Jurassic Park", 1993, "Sci-Fi, Adventure", "Dinosaurs are brought back to life in a theme park.", "Steven Spielberg"),
        ("The Shawshank Redemption", 1994, "Drama", "Two imprisoned men bond over years of hardship.", "Frank Darabont"),
        ("Forrest Gump", 1994, "Drama, Romance", "The life journey of a simple man with a big heart.", "Robert Zemeckis"),
        ("The Godfather", 1972, "Crime, Drama", "The aging patriarch transfers control of his empire.", "Francis Ford Coppola"),
        ("Pulp Fiction", 1994, "Crime, Drama", "Interwoven stories of crime in Los Angeles.", "Quentin Tarantino"),
        ("Fight Club", 1999, "Drama, Thriller", "An insomniac and soap maker form an underground club.", "David Fincher"),
        ("The Lord of the Rings: Fellowship of the Ring", 2001, "Fantasy, Adventure", "A hobbit begins a quest to destroy a powerful ring.", "Peter Jackson"),
        ("Harry Potter and the Sorcerer's Stone", 2001, "Fantasy, Adventure", "A boy discovers he is a wizard and attends Hogwarts.", "Chris Columbus")
    ]

    cur.executemany("INSERT INTO movies VALUES (?,?,?,?,?)", sample_movies)
    conn.commit()
    conn.close()

def get_movies():
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")
    rows = cur.fetchall()
    conn.close()
    return [
        {"title": r[0], "year": r[1], "genre": r[2], "description": r[3], "director": r[4]}
        for r in rows
    ]
