class Content:
    def __init__(self, id, name, duration, summary, genre, rating, lastPLay, gambar):
        self.id = id
        self.name = name
        self.duration = duration
        self.summary = summary
        self.genre = genre
        self.rating = rating
        self.lastPLay = lastPLay
        self.gambar = gambar
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getDuration(self):
        return self.duration
    
    def getSummary(self):
        return self.summary
    
    def getGenre(self):
        return self.genre
    
    def getRating(self):
        return self.rating
    
    def getLastPlay(self):
        return self.lastPLay
    
    def getGambar(self):
        return self.gambar
    
    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setDuration(self, duration):
        self.duration = duration

    def setSummary(self, summary):
        self.summary = summary

    def setGenre(self, genre):
        self.genre = genre

    def setRating(self, rating):
        self.rating = rating
    
    def setLastPlay(self, lastPLay):
        self.lastPLay = lastPLay
    
    def setGambar(self, gambar):
        self.gambar = gambar

class Movie(Content):
    def __init__(self, id, name, duration, summary, genre, rating, lastPLay, gambar):
        super().__init__(id, name, duration, summary, genre, rating, lastPLay, gambar)

class Series(Content):
    def __init__(self, id, name, duration, summary, genre, rating, lastPLay, gambar, season, episode):
        super().__init__(id, name, duration, summary, genre, rating, lastPLay, gambar)
        self.season = season
        self.episode = episode
    
    def getSeason(self):
        return self.season
    
    def getEpisode(self):
        return self.episode
    
    def setSeason(self, season):
        self.season = season
    
    def setEpisode(self, episode):
        self.episode = episode