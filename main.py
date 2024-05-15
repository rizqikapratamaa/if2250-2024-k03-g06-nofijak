import sqlite3
import flet as ft
from content import *
from edit_page import *
from add_page import *

conn = sqlite3.connect("database.db")

try:
    # Create a cursor object
    cursor = conn.cursor()

    # Commit changes
    conn.commit()

    # Retrieve data from the table
    # Fetch movies and store in a dictionary
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    movies_dict = {}
    for row in movies:
        movies_dict[row[0]] = list(row)

    # Fetch series and store in a dictionary
    cursor.execute("SELECT * FROM series")
    series = cursor.fetchall()
    series_dict = {}
    for row in series:
        series_dict[row[0]] = list(row)

    # Fetch finished movies and store in a dictionary
    cursor.execute("SELECT * FROM finished_movies")
    finished_movies = cursor.fetchall()
    finished_movies_dict = {}
    for row in finished_movies:
        finished_movies_dict[row[0]] = list(row)

    

    cursor.execute("SELECT * FROM finished_series")
    finished_series = cursor.fetchall()
    finished_series_dict = {}
    for row in finished_series:
        finished_series_dict[row[0]] = list(row)

    cursor.execute("SELECT * FROM ongoing_movies")
    ongoing_movies = cursor.fetchall()
    ongoing_movies_dict = {}
    for row in ongoing_movies:
        ongoing_movies_dict[row[0]] = list(row)
    
    cursor.execute("SELECT * FROM ongoing_series")
    ongoing_series = cursor.fetchall()
    ongoing_series_dict = {}
    for row in ongoing_series:
        ongoing_series_dict[row[0]] = list(row)


    cursor.execute("SELECT * FROM review_movies")
    review_movies = cursor.fetchall()
    review_movies_dict = {}
    for row in review_movies:
        review_movies_dict[row[0]] = list(row)

    cursor.execute("SELECT * FROM review_series")
    review_series = cursor.fetchall()
    review_series_dict = {}
    for row in review_series:
        review_series_dict[row[0]] = list(row)

    cursor.execute("SELECT * FROM watchlist_movies")
    watchlist_movies = cursor.fetchall()
    watchlist_movies_dict = {}
    for row in watchlist_movies:
        watchlist_movies_dict[row[0]] = list(row)


    cursor.execute("SELECT * FROM watchlist_series")
    watchlist_series = cursor.fetchall()
    watchlist_series_dict = {}
    for row in watchlist_series:
        watchlist_series_dict[row[0]] = list(row)
        
    def make_movies(id):
        id = movies_dict[id][0] if id in movies_dict else None
        name = movies_dict[id][1] if id in movies_dict else None
        releaseDate = movies_dict[id][3] if id in movies_dict else None
        duration = movies_dict[id][2] if id in movies_dict else 0
        synopsis = movies_dict[id][5] if id in movies_dict else None
        genre = movies_dict[id][4] if id in movies_dict else None
        rating = review_movies_dict[id][1] if id in review_movies_dict else None
        watchProgress = ongoing_movies_dict[id][1] if id in ongoing_movies_dict else 0

        return Movie(id, name, releaseDate, duration, synopsis, genre, rating, watchProgress, "assets/img/" + str(id) + ".jpg")
    
    def make_series(id):
        id = series_dict[id][0] if id in series_dict else None
        name = series_dict[id][1] if id in series_dict else None
        releaseDate = series_dict[id][3] if id in series_dict else None
        duration = series_dict[id][2] if id in series_dict else None
        synopsis = series_dict[id][5] if id in series_dict else None
        genre = series_dict[id][4] if id in series_dict else None
        rating = review_series_dict[id][1] if id in review_series_dict else None
        watchProgress = ongoing_series_dict[id][3] if id in ongoing_series_dict else None
        season = series_dict[id][6] if id in series_dict else None
        episode = series_dict[id][7] if id in series_dict else None
        current_season = ongoing_series_dict[id][1] if id in ongoing_series_dict else None
        current_episode = ongoing_series_dict[id][2] if id in ongoing_series_dict else None

        return Series(id, name, releaseDate, duration, synopsis, genre, rating, watchProgress, "assets/img/" + str(id) + ".jpg", season, episode, current_season, current_episode)

    tes_mov = make_movies(1)
    tes_series = make_series(1)
    movie = Movie("1", "The Falcon and The Winter Soldier", "2020-07-20", 5000, "Sam Wilson and Bucky Barnes realize that their futures are anything but normal.", "Horror", 8.0, 1000, "assets/img/1.jpg")
    series = Series("2", "The Falcon and The Winter Soldier", "2020-07-20", 5000, None, "Horror", 8.0, 1000, "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg", 1, 8, 1, 4)
    def main(page: ft.Page):
        page.scroll = True
        page.title = "Nofijak"
        page.bgcolor = "#000D20"

        page.vertical_alignment = ft.MainAxisAlignment.START
        edit_page = SeriesAddPage(page, movies_dict, ongoing_movies_dict, review_movies_dict, watchlist_movies_dict, finished_movies_dict, series_dict, ongoing_series_dict, review_series_dict, watchlist_series_dict, finished_series_dict)
        edit_page.show_page(page)

    ft.app(target=main, upload_dir="assets/img", assets_dir="assets")

except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    # Close connection
    conn.close()
