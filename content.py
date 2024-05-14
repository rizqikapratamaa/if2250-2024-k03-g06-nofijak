class Content:
    def __init__(self, id, name, releaseYear, duration, summary, genre, rating, watchProgress, gambar):
        self.id = id
        self.name = name
        self.releaseYear = releaseYear
        self.duration = duration
        self.summary = summary
        self.genre = genre
        self.rating = rating
        self.watchProgress = watchProgress
        self.gambar = gambar
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getReleaseYear(self):
        return self.releaseYear
    
    def getDuration(self):
        return self.duration
    
    def getSummary(self):
        return self.summary
    
    def getGenre(self):
        return self.genre
    
    def getRating(self):
        return self.rating
    
    def getWatchProgress(self):
        return self.watchProgress
    
    def getGambar(self):
        return self.gambar
    
    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setReleaseYear(self, releaseYear):
        self.releaseYear = releaseYear
    
    def setLastplay(self, lastplay):
        self.lastplay = lastplay

    def setDuration(self, duration):
        self.duration = duration

    def setSummary(self, summary):
        self.summary = summary

    def setGenre(self, genre):
        self.genre = genre

    def setRating(self, rating):
        self.rating = rating
    
    def setWatchProgress(self, watchProgress):
        self.watchProgress = watchProgress
    
    def setGambar(self, gambar):
        self.gambar = gambar

class Movie(Content):
    def __init__(self, id, name, releaseYear, duration, summary, genre, rating, watchProgress, gambar):
        super().__init__(id, name, releaseYear, duration, summary, genre, rating, watchProgress, gambar)

class Series(Content):
    def __init__(self, id, name, releaseYear, duration, summary, genre, rating, watchProgress, gambar, season, episode, seasonProgress, episodeProgress):
        super().__init__(id, name, releaseYear, duration, summary, genre, rating, watchProgress, gambar)
        self.season = season
        self.seasonProgress = seasonProgress
        self.episode = episode
        self.episodeProgress = episodeProgress
    
    def getSeason(self):
        return self.season
    
    def getSeasonProgress(self):
        return self.seasonProgress
    
    def getEpisode(self):
        return self.episode
    
    def getEpisodeProgress(self):
        return self.episodeProgress
    
    def setSeason(self, season):
        self.season = season
    
    def setSeasonProgress(self, seasonProgress):
        self.seasonProgress = seasonProgress
    
    def setEpisode(self, episode):
        self.episode = episode

    def setEpisodeProgress(self, episodeProgress):
        self.episodeProgress = episodeProgress