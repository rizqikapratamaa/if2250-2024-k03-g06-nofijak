from main import main
from unittest.mock import MagicMock

def test_main():
    page = MagicMock()
    page.update()
    page.update.assert_called()

def test_id():
    page = MagicMock()
    page.body.getId = MagicMock(return_value=1)
    assert page.body.getId() == 1
    
def test_name():
    page = MagicMock()
    page.body.getName = MagicMock(return_value="Series Test")
    assert page.body.getName() == "Series Test"
    
def test_releaseyear():
    page = MagicMock()
    page.body.getReleaseYear = MagicMock(return_value=2000)
    assert page.body.getReleaseYear() == 2000
    
def test_duration():
    page = MagicMock()
    page.body.getDuration = MagicMock(return_value=3600)
    assert page.body.getDuration() == 3600
    
def test_summary():
    page = MagicMock()
    page.body.getSummary = MagicMock(return_value="Summary")
    assert page.body.getSummary() == "Summary"
    
def test_genre():
    page = MagicMock()
    page.body.getGenre = MagicMock(return_value="Action")
    assert page.body.getGenre() == "Action"
    
def test_rating():
    page = MagicMock()
    page.body.getRating = MagicMock(return_value=10)
    assert page.body.getRating() == 10

def test_watchprogress():
    page = MagicMock()
    page.body.getWatchProgress = MagicMock(return_value=1000)
    assert page.body.getWatchProgress() == 1000
    
def test_gambar():
    page = MagicMock()
    page.body.getGambar = MagicMock(return_value="this/is/a/path")
    assert page.body.getGambar() == "this/is/a/path"
    
def test_season():
    page = MagicMock()
    page.body.getSeason = MagicMock(return_value=5)
    assert page.body.getSeason() == 5
    
def test_seasonprogress():
    page = MagicMock()
    page.body.getSeasonProgress = MagicMock(return_value=2)
    assert page.body.getSeasonProgress() == 2
    
def test_episode():
    page = MagicMock()
    page.body.getEpisode = MagicMock(return_value=5)
    assert page.body.getEpisode() == 5
    
def test_episodeprogress():
    page = MagicMock()
    page.body.getEpisodeProgress = MagicMock(return_value=2)
    assert page.body.getEpisodeProgress() == 2
