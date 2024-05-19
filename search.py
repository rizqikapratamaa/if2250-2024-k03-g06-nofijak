from content import *
import sqlite3

def searchMovies(movieName):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT movies_id FROM movies WHERE name LIKE '" + movieName + "%'")
    id = cursor.fetchall()

    result = []

    for i in range (len(id)):
        cursor.execute("SELECT name, release_year, duration, synopsis, genre FROM movies WHERE movies_id = " + str(id[i][0]))
        movie = cursor.fetchall()

        cursor.execute("SELECT rating FROM review_movies WHERE movies_id = " + str(id[i][0]))
        rating = cursor.fetchall()
        if len(rating) == 0:
            rating = 0
        else:
            rating = rating[0][0]

        cursor.execute("SELECT watched_duration FROM ongoing_movies WHERE movies_id = " + str(id[i][0]))
        duration = cursor.fetchall()
        if len(duration) == 0:
            duration = 0
        else:
            duration = duration[0][0]

        result.append(Movie(id[i][0], movie[0][0], movie[0][1], movie[0][2], movie[0][3], movie[0][4], rating, duration, str(id) + "m"))

    return result

def searchSeries(serieName):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT series_id FROM series WHERE name LIKE '" + serieName + "%'")
    id = cursor.fetchall()

    result = []

    for i in range (len(id)):
        cursor.execute("SELECT name, release_year, duration, synopsis, genre, season, episode FROM series WHERE series_id = " + str(id[i][0]))
        series = cursor.fetchall()

        cursor.execute("SELECT rating FROM review_series WHERE series_id = " + str(id[i][0]))
        rating = cursor.fetchall()
        if len(rating) == 0:
            rating = 0
        else:
            rating = rating[0][0]

        cursor.execute("SELECT watched_duration, season_progress, episode_progress FROM ongoing_series WHERE series_id = " + str(id[i][0]))
        duration = cursor.fetchall()
        watchProgress = 0
        seasonProgress = 0
        episodeProgress = 0
        if len(duration) != 0:
            watchProgress = duration[0][0]
            seasonProgress = duration[0][1]
            episodeProgress = duration[0][2]

        result.append(Series(id[i][0], series[0][0], series[0][1], series[0][2], series[0][3], series[0][4], rating, watchProgress, str(id) + "s", series[0][5], series[0][6], seasonProgress, episodeProgress))

    return result