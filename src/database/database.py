import sqlite3
from utils.content import *

class Database:
    def __init__(self):
        # Create a cursor object
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        try:

            # Retrieve data from the table
            # Fetch movies and store in a dictionary
            cursor.execute("SELECT * FROM movies")
            movies = cursor.fetchall()
            self.movies_dict = {}
            for row in movies:
                self.movies_dict[row[0]] = list(row)

            # Fetch series and store in a dictionary
            cursor.execute("SELECT * FROM series")
            series = cursor.fetchall()
            self.series_dict = {}
            for row in series:
                self.series_dict[row[0]] = list(row)

            # Fetch finished movies and store in a dictionary
            cursor.execute("SELECT * FROM finished_movies")
            finished_movies = cursor.fetchall()
            self.finished_movies_dict = {}
            for row in finished_movies:
                self.finished_movies_dict[row[0]] = list(row)

            

            cursor.execute("SELECT * FROM finished_series")
            finished_series = cursor.fetchall()
            self.finished_series_dict = {}
            for row in finished_series:
                self.finished_series_dict[row[0]] = list(row)

            cursor.execute("SELECT * FROM ongoing_movies")
            ongoing_movies = cursor.fetchall()
            self.ongoing_movies_dict = {}
            for row in ongoing_movies:
                self.ongoing_movies_dict[row[0]] = list(row)
            
            cursor.execute("SELECT * FROM ongoing_series")
            ongoing_series = cursor.fetchall()
            self.ongoing_series_dict = {}
            for row in ongoing_series:
                self.ongoing_series_dict[row[0]] = list(row)


            cursor.execute("SELECT * FROM review_movies")
            review_movies = cursor.fetchall()
            self.review_movies_dict = {}
            for row in review_movies:
                self.review_movies_dict[row[0]] = list(row)

            cursor.execute("SELECT * FROM review_series")
            review_series = cursor.fetchall()
            self.review_series_dict = {}
            for row in review_series:
                self.review_series_dict[row[0]] = list(row)

            cursor.execute("SELECT * FROM watchlist_movies")
            watchlist_movies = cursor.fetchall()
            self.watchlist_movies_dict = {}
            for row in watchlist_movies:
                self.watchlist_movies_dict[row[0]] = list(row)


            cursor.execute("SELECT * FROM watchlist_series")
            watchlist_series = cursor.fetchall()
            self.watchlist_series_dict = {}
            for row in watchlist_series:
                self.watchlist_series_dict[row[0]] = list(row)

            # Commit changes
            conn.commit()

        except sqlite3.Error as e:
            print("An error occurred:", e)


        finally:
            # Close connection
            conn.close()
    
    def getMovies(self):
        return self.movies_dict
    
    def getSeries(self):
        return self.series_dict
    
    def getFinishedMovies(self):
        return self.finished_movies_dict
    
    def getFinishedSeries(self):
        return self.finished_series_dict
    
    def getOngoingMovies(self):
        return self.ongoing_movies_dict
    
    def getOngoingSeries(self):
        return self.ongoing_series_dict
    
    def getReviewMovies(self):
        return self.review_movies_dict
    
    def getReviewSeries(self):
        return self.review_series_dict
    
    def getWatchlistMovies(self):
        return self.watchlist_movies_dict
    
    def getWatchlistSeries(self):
        return self.watchlist_series_dict

    def addMovie(self, id, name, releaseDate, duration, genre, synopsis):
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?)", (id, name, duration, releaseDate, genre, synopsis))
        self.movies_dict[id] = [id, name, duration, releaseDate, genre, synopsis]
        conn.commit()
        conn.close()

    def addSeries(self, id, name, releaseDate, duration, genre, synopsis, season, episode):
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO series VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id, name, duration, releaseDate, genre, synopsis, season, episode))
        self.series_dict[id] = [id, name, duration, releaseDate, genre, synopsis, season, episode]
        conn.commit()
        conn.close()

    def addFinishedMovie(self, id, rating):
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO finished_movies VALUES (?, ?)", (id, rating))
        self.finished_movies_dict[id] = [id, rating]
        conn.commit()
        conn.close()

    def addFinishedSeries(self, id, rating):
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO finished_series VALUES (?, ?)", (id, rating))
        self.finished_series_dict[id] = [id, rating]
        conn.commit()
        conn.close()

    def addOngoingMovie(self, id, watchProgress):
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ongoing_movies VALUES (?, ?)", (id, watchProgress))
        self.ongoing_movies_dict[id] = [id, watchProgress]
        conn.commit()
        conn.close()

    def addOngoingSeries(self, id, currentSeason, currentEpisode):
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ongoing_series VALUES (?, ?, ?)", (id, currentSeason, currentEpisode))
        self.ongoing_series_dict[id] = [id, currentSeason, currentEpisode]
        conn.commit()
        conn.close()

    def addReviewMovie(self, id, rating):
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO review_movies VALUES (?, ?)", (id, rating))
        self.review_movies_dict[id] = [id, rating]
        conn.commit()
        conn.close()

    def addReviewSeries(self, id, rating):
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO review_series VALUES (?, ?)", (id, rating))
        self.review_series_dict[id] = [id, rating]
        conn.commit()
        conn.close()

    def addWatchlistMovie(self, id):
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO watchlist_movies VALUES (?)", (id,))
        self.watchlist_movies_dict[id] = [id]
        conn.commit()
        conn.close()

    def addWatchlistSeries(self, id):
        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO watchlist_series VALUES (?)", (id,))
        self.watchlist_series_dict[id] = [id]
        conn.commit()
        conn.close()

    def removeMovie(self, id):
        if id in self.movies_dict:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movies WHERE movies_id = ?", (id,))
            del self.movies_dict[id]
            conn.commit()
            conn.close()

    def removeSeries(self, id):
        if id in self.series_dict:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM series WHERE series_id = ?", (id,))
            del self.series_dict[id]
            conn.commit()
            conn.close()

    def removeFinishedMovie(self, id):
        if id in self.finished_movies_dict:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM finished_movies WHERE movies_id = ?", (id,))
            del self.finished_movies_dict[id]
            conn.commit()
            conn.close()

    def removeFinishedSeries(self, id):
        if id in self.finished_series_dict:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM finished_series WHERE series_id = ?", (id,))
            del self.finished_series_dict[id]
            conn.commit()
            conn.close()

    def removeOngoingMovie(self, id):
        if id in self.ongoing_movies_dict:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM ongoing_movies WHERE movies_id = ?", (id,))
            del self.ongoing_movies_dict[id]
            conn.commit()
            conn.close()

    def removeOngoingSeries(self, id):
        if id in self.ongoing_series_dict:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM ongoing_series WHERE series_id = ?", (id,))
            del self.ongoing_series_dict[id]
            conn.commit()
            conn.close()

    def removeReviewMovie(self, id):
        if id in self.review_movies_dict:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM review_movies WHERE movies_id = ?", (id,))
            del self.review_movies_dict[id]
            conn.commit()
            conn.close()

    def removeReviewSeries(self, id):
        if id in self.review_series_dict:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM review_series WHERE series_id = ?", (id,))
            del self.review_series_dict[id]
            conn.commit()
            conn.close()

    def removeWatchlistMovie(self, id):
        if id in self.watchlist_movies_dict:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM watchlist_movies WHERE movies_id = ?", (id,))
            del self.watchlist_movies_dict[id]
            conn.commit()
            conn.close()

    def removeWatchlistSeries(self, id):
        if id in self.watchlist_series_dict:
            conn = sqlite3.connect("database/database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM watchlist_series WHERE series_id = ?", (id,))
            del self.watchlist_series_dict[id]
            conn.commit()
            conn.close()

    def make_movies(self, id):
        id = self.movies_dict[id][0] if id in self.movies_dict else None
        name = self.movies_dict[id][1] if id in self.movies_dict else None
        releaseDate = self.movies_dict[id][3] if id in self.movies_dict else None
        duration = self.movies_dict[id][2] if id in self.movies_dict else 0
        synopsis = self.movies_dict[id][5] if id in self.movies_dict else None
        genre = self.movies_dict[id][4] if id in self.movies_dict else None
        rating = self.review_movies_dict[id][1] if id in self.review_movies_dict else None
        watchProgress = self.ongoing_movies_dict[id][1] if id in self.ongoing_movies_dict else 0

        return Movie(id, name, releaseDate, duration, synopsis, genre, rating, watchProgress, "../assets/img/" + str(id) + "m.jpg")
    
    def make_series(self, id):
        id = self.series_dict[id][0] if id in self.series_dict else None
        name = self.series_dict[id][1] if id in self.series_dict else None
        releaseDate = self.series_dict[id][3] if id in self.series_dict else None
        duration = self.series_dict[id][2] if id in self.series_dict else None
        synopsis = self.series_dict[id][5] if id in self.series_dict else None
        genre = self.series_dict[id][4] if id in self.series_dict else None
        rating = self.review_series_dict[id][1] if id in self.review_series_dict else None
        watchProgress = self.ongoing_series_dict[id][3] if id in self.ongoing_series_dict else None
        season = self.series_dict[id][6] if id in self.series_dict else None
        episode = self.series_dict[id][7] if id in self.series_dict else None
        current_season = self.ongoing_series_dict[id][1] if id in self.ongoing_series_dict else None
        current_episode = self.ongoing_series_dict[id][2] if id in self.ongoing_series_dict else None
        
        return Series(id, name, releaseDate, duration, synopsis, genre, rating, watchProgress, "../assets/img/" + str(id) + "s.jpg", season, episode, current_season, current_episode)