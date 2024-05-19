import pytest
import sqlite3

@pytest.fixture(scope="module")
def db_connection():
    connection = sqlite3.connect("src/database/database.db")
    connection.row_factory = sqlite3.Row
    
    cursor = connection.cursor()
    cursor.executescript("""
    DELETE FROM review_movies;
    DELETE FROM ongoing_movies;
    DELETE FROM finished_movies;
    DELETE FROM watchlist_movies;
    DELETE FROM movies;
    DELETE FROM review_series;
    DELETE FROM ongoing_series;
    DELETE FROM finished_series;
    DELETE FROM watchlist_series;
    DELETE FROM series;
    """)
    connection.commit()
    
    yield connection
    
    connection.close()

def test_movies(db_connection):
    with db_connection as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO movies (movies_id, name, duration, release_year, genre, synopsis) VALUES (?, ?, ?, ?, ?, ?)", [
            (1, 'movie1', 3600, 2024, 'Action', None),
            (2, 'movie2', 3600, 2024, 'Action', None),
            (3, 'movie3', 3600, 2024, 'Action', None),
            (4, 'movie4', 3600, 2024, 'Action', None),
            (5, 'movie5', 3600, 2024, 'Action', None)
        ])
        cursor.execute("SELECT * FROM movies")
        result = cursor.fetchall()
        assert len(result) == 5

def test_watchlist_movies(db_connection):
    with db_connection as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO watchlist_movies (movies_id) VALUES (?)", [
            (1,),
            (2,),
            (3,),
            (4,),
            (5,)
        ])
        cursor.execute("SELECT * FROM watchlist_movies")
        result = cursor.fetchall()
        assert len(result) == 5

def test_finished_movies(db_connection):
    with db_connection as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO finished_movies (movies_id, finished_date) VALUES (?, ?)", [
            (1, '2024-04-04'),
            (2, '2024-04-04'),
            (3, '2024-04-04'),
            (4, '2024-04-04'),
            (5, '2024-04-04')
        ])
        cursor.execute("SELECT * FROM finished_movies")
        result = cursor.fetchall()
        assert len(result) == 5

def test_ongoing_movies(db_connection):
    with db_connection as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO ongoing_movies (movies_id, watched_duration) VALUES (?, ?)", [
            (1, 1200),
            (2, 1200),
            (3, 1200),
            (4, 1200),
            (5, 1200)
        ])
        cursor.execute("SELECT * FROM ongoing_movies")
        result = cursor.fetchall()
        assert len(result) == 5

def test_review_movies(db_connection):
    with db_connection as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO review_movies (movies_id, rating) VALUES (?, ?)", [
            (1, 10),
            (2, 10),
            (3, 10),
            (4, 10),
            (5, 10)
        ])
        cursor.execute("SELECT * FROM review_movies")
        result = cursor.fetchall()
        assert len(result) == 5

def test_series(db_connection):
    with db_connection as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO series (series_id, name, duration, release_year, genre, synopsis, season, episode) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [
            (1, 'serie1', 3600, 2024, 'Action', None, 6, 20),
            (2, 'serie2', 3600, 2024, 'Action', None, 6, 20),
            (3, 'serie3', 3600, 2024, 'Action', None, 6, 20),
            (4, 'serie4', 3600, 2024, 'Action', None, 6, 20),
            (5, 'serie5', 3600, 2024, 'Action', None, 6, 20)
        ])
        cursor.execute("SELECT * FROM series")
        result = cursor.fetchall()
        assert len(result) == 5

def test_watchlist_series(db_connection):
    with db_connection as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO watchlist_series (series_id) VALUES (?)", [
            (1,),
            (2,),
            (3,),
            (4,),
            (5,)
        ])
        cursor.execute("SELECT * FROM watchlist_series")
        result = cursor.fetchall()
        assert len(result) == 5

def test_finished_series(db_connection):
    with db_connection as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO finished_series (series_id, finished_date) VALUES (?, ?)", [
            (1, '2024-04-04'),
            (2, '2024-04-04'),
            (3, '2024-04-04'),
            (4, '2024-04-04'),
            (5, '2024-04-04')
        ])
        cursor.execute("SELECT * FROM finished_series")
        result = cursor.fetchall()
        assert len(result) == 5

def test_ongoing_series(db_connection):
    with db_connection as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO ongoing_series (series_id, season_progress, episode_progress, watched_duration) VALUES (?, ?, ?, ?)", [
            (1, 2, 10, 1200),
            (2, 2, 10, 1200),
            (3, 2, 10, 1200),
            (4, 2, 10, 1200),
            (5, 2, 10, 1200)
        ])
        cursor.execute("SELECT * FROM ongoing_series")
        result = cursor.fetchall()
        assert len(result) == 5

def test_review_series(db_connection):
    with db_connection as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO review_series (series_id, rating, review) VALUES (?, ?, ?)", [
            (1, 10, None),
            (2, 10, None),
            (3, 10, None),
            (4, 10, None),
            (5, 10, None)
        ])
        cursor.execute("SELECT * FROM review_series")
        result = cursor.fetchall()
        assert len(result) == 5
