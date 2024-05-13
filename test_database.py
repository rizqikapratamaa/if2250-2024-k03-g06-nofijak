import pytest
import pymysql

@pytest.fixture(scope="module")
def db_connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='alatreon',
                                 database='repel',
                                 cursorclass=pymysql.cursors.DictCursor)
    yield connection
    connection.close()

def test_movies(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("DELETE FROM review_movies")
        cursor.execute("DELETE FROM ongoing_movies")
        cursor.execute("DELETE FROM finished_movies")
        cursor.execute("DELETE FROM watchlist_movies")
        cursor.execute("DELETE FROM movies")
        cursor.execute("INSERT INTO movies (movies_id, name, duration, release_year, genre, synopsis) VALUES (1, 'movie1', 3600, 2024, 'Action', null)")
        cursor.execute("INSERT INTO movies (movies_id, name, duration, release_year, genre, synopsis) VALUES (2, 'movie2', 3600, 2024, 'Action', null)")
        cursor.execute("INSERT INTO movies (movies_id, name, duration, release_year, genre, synopsis) VALUES (3, 'movie3', 3600, 2024, 'Action', null)")
        cursor.execute("INSERT INTO movies (movies_id, name, duration, release_year, genre, synopsis) VALUES (4, 'movie4', 3600, 2024, 'Action', null)")
        cursor.execute("INSERT INTO movies (movies_id, name, duration, release_year, genre, synopsis) VALUES (5, 'movie5', 3600, 2024, 'Action', null)")
        cursor.execute("SELECT * FROM movies")
        result = cursor.fetchall()
        assert len(result) == 5

def test_watchlist_movies(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("DELETE FROM watchlist_movies")
        cursor.execute("INSERT INTO watchlist_movies (movies_id) VALUES (1)")
        cursor.execute("INSERT INTO watchlist_movies (movies_id) VALUES (2)")
        cursor.execute("INSERT INTO watchlist_movies (movies_id) VALUES (3)")
        cursor.execute("INSERT INTO watchlist_movies (movies_id) VALUES (4)")
        cursor.execute("INSERT INTO watchlist_movies (movies_id) VALUES (5)")
        cursor.execute("SELECT * FROM watchlist_movies")
        result = cursor.fetchall()
        assert len(result) == 5

def test_finished_movies(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("DELETE FROM finished_movies")
        cursor.execute("INSERT INTO finished_movies (movies_id, finished_date) VALUES (1, '2024-04-04')")
        cursor.execute("INSERT INTO finished_movies (movies_id, finished_date) VALUES (2, '2024-04-04')")
        cursor.execute("INSERT INTO finished_movies (movies_id, finished_date) VALUES (3, '2024-04-04')")
        cursor.execute("INSERT INTO finished_movies (movies_id, finished_date) VALUES (4, '2024-04-04')")
        cursor.execute("INSERT INTO finished_movies (movies_id, finished_date) VALUES (5, '2024-04-04')")
        cursor.execute("SELECT * FROM finished_movies")
        result = cursor.fetchall()
        assert len(result) == 5

def test_ongoing_movies(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("DELETE FROM ongoing_movies")
        cursor.execute("INSERT INTO ongoing_movies (movies_id, watched_duration) VALUES (1, 1200)")
        cursor.execute("INSERT INTO ongoing_movies (movies_id, watched_duration) VALUES (2, 1200)")
        cursor.execute("INSERT INTO ongoing_movies (movies_id, watched_duration) VALUES (3, 1200)")
        cursor.execute("INSERT INTO ongoing_movies (movies_id, watched_duration) VALUES (4, 1200)")
        cursor.execute("INSERT INTO ongoing_movies (movies_id, watched_duration) VALUES (5, 1200)")
        cursor.execute("SELECT * FROM ongoing_movies")
        result = cursor.fetchall()
        assert len(result) == 5

def test_review_movies(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("DELETE FROM review_movies")
        cursor.execute("INSERT INTO review_movies (movies_id, rating) VALUES (1, 10)")
        cursor.execute("INSERT INTO review_movies (movies_id, rating) VALUES (2, 10)")
        cursor.execute("INSERT INTO review_movies (movies_id, rating) VALUES (3, 10)")
        cursor.execute("INSERT INTO review_movies (movies_id, rating) VALUES (4, 10)")
        cursor.execute("INSERT INTO review_movies (movies_id, rating) VALUES (5, 10)")
        cursor.execute("SELECT * FROM review_movies")
        result = cursor.fetchall()
        assert len(result) == 5

def test_series(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("DELETE FROM review_series")
        cursor.execute("DELETE FROM ongoing_series")
        cursor.execute("DELETE FROM finished_series")
        cursor.execute("DELETE FROM watchlist_series")
        cursor.execute("DELETE FROM series")
        cursor.execute("INSERT INTO series (series_id, name, duration, release_year, genre, synopsis, season, episode) VALUES (1, 'serie1', 3600, 2024, 'Action', null, 6, 20)")
        cursor.execute("INSERT INTO series (series_id, name, duration, release_year, genre, synopsis, season, episode) VALUES (2, 'serie2', 3600, 2024, 'Action', null, 6, 20)")
        cursor.execute("INSERT INTO series (series_id, name, duration, release_year, genre, synopsis, season, episode) VALUES (3, 'serie3', 3600, 2024, 'Action', null, 6, 20)")
        cursor.execute("INSERT INTO series (series_id, name, duration, release_year, genre, synopsis, season, episode) VALUES (4, 'serie4', 3600, 2024, 'Action', null, 6, 20)")
        cursor.execute("INSERT INTO series (series_id, name, duration, release_year, genre, synopsis, season, episode) VALUES (5, 'serie5', 3600, 2024, 'Action', null, 6, 20)")
        cursor.execute("SELECT * FROM series")
        result = cursor.fetchall()
        assert len(result) == 5

def test_watchlist_series(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("DELETE FROM watchlist_series")
        cursor.execute("INSERT INTO watchlist_series (series_id) VALUES (1)")
        cursor.execute("INSERT INTO watchlist_series (series_id) VALUES (2)")
        cursor.execute("INSERT INTO watchlist_series (series_id) VALUES (3)")
        cursor.execute("INSERT INTO watchlist_series (series_id) VALUES (4)")
        cursor.execute("INSERT INTO watchlist_series (series_id) VALUES (5)")
        cursor.execute("SELECT * FROM watchlist_series")
        result = cursor.fetchall()
        assert len(result) == 5

def test_finished_series(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("DELETE FROM finished_series")
        cursor.execute("INSERT INTO finished_series (series_id, finished_date) VALUES (1, '2024-04-04')")
        cursor.execute("INSERT INTO finished_series (series_id, finished_date) VALUES (2, '2024-04-04')")
        cursor.execute("INSERT INTO finished_series (series_id, finished_date) VALUES (3, '2024-04-04')")
        cursor.execute("INSERT INTO finished_series (series_id, finished_date) VALUES (4, '2024-04-04')")
        cursor.execute("INSERT INTO finished_series (series_id, finished_date) VALUES (5, '2024-04-04')")
        cursor.execute("SELECT * FROM finished_series")
        result = cursor.fetchall()
        assert len(result) == 5

def test_ongoing_series(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("DELETE FROM ongoing_series")
        cursor.execute("INSERT INTO ongoing_series (series_id, season_progress, episode_progress, watched_duration) VALUES (1, 2, 10, 1200)")
        cursor.execute("INSERT INTO ongoing_series (series_id, season_progress, episode_progress, watched_duration) VALUES (2, 2, 10, 1200)")
        cursor.execute("INSERT INTO ongoing_series (series_id, season_progress, episode_progress, watched_duration) VALUES (3, 2, 10, 1200)")
        cursor.execute("INSERT INTO ongoing_series (series_id, season_progress, episode_progress, watched_duration) VALUES (4, 2, 10, 1200)")
        cursor.execute("INSERT INTO ongoing_series (series_id, season_progress, episode_progress, watched_duration) VALUES (5, 2, 10, 1200)")
        cursor.execute("SELECT * FROM ongoing_series")
        result = cursor.fetchall()
        assert len(result) == 5

def test_review_series(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("DELETE FROM review_series")
        cursor.execute("INSERT INTO review_series (series_id, rating, review) VALUES (1, 10, null)")
        cursor.execute("INSERT INTO review_series (series_id, rating, review) VALUES (2, 10, null)")
        cursor.execute("INSERT INTO review_series (series_id, rating, review) VALUES (3, 10, null)")
        cursor.execute("INSERT INTO review_series (series_id, rating, review) VALUES (4, 10, null)")
        cursor.execute("INSERT INTO review_series (series_id, rating, review) VALUES (5, 10, null)")
        cursor.execute("SELECT * FROM review_series")
        result = cursor.fetchall()
        assert len(result) == 5
