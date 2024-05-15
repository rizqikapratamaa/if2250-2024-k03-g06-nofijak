from main import main
from unittest.mock import MagicMock

def test_main():
    page = MagicMock()
    page.body.getId = MagicMock(return_value=1)
    page.body.getName = MagicMock(return_value="Series Test")
    page.body.getReleaseYear = MagicMock(return_value=2000)
    page.body.getDuration = MagicMock(return_value=3600)
    page.body.getSummary = MagicMock(return_value="Summary")
    page.body.getGenre = MagicMock(return_value="Action")
    page.body.getRating = MagicMock(return_value=10)
    page.body.getWatchProgress = MagicMock(return_value=1000)
    page.body.getGambar = MagicMock(return_value="this/is/a/path")
    page.body.season = MagicMock(return_value=5)
    page.body.season_progress = MagicMock(return_value=2)
    page.body.episode = MagicMock(return_value=5)
    page.body.episode_progress = MagicMock(return_value=2)

    page.update()
    page.update.assert_called()

    assert page.body.getId() == 1
    assert page.body.getName() == "Series Test"
    assert page.body.getReleaseYear() == 2000
    assert page.body.getDuration() == 3600
    assert page.body.getSummary() == "Summary"
    assert page.body.getGenre() == "Action"
    assert page.body.getRating() == 10
    assert page.body.getWatchProgress() == 1000
    assert page.body.getGambar() == "this/is/a/path"
    assert page.body.season() == 5
    assert page.body.season_progress() == 2
    assert page.body.episode() == 5
    assert page.body.episode_progress() == 2