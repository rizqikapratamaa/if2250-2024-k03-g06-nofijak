import sqlite3
import flet as ft
from content import *
from edit_page import *
from add_page import *
from database import *

def main(page: ft.Page):
    database = Database()
    page.scroll = True
    page.title = "Nofijak"
    page.bgcolor = "#000D20"

    page.vertical_alignment = ft.MainAxisAlignment.START
    # edit_page = SeriesAddPage(page, database.getMovies, database.getOngoingMovies(), database.getReviewMovies, database.getWatchlistMovies(), database.getFinishedMovies(), database.getSeries() series_dict, ongoing_series_dict, review_series_dict, watchlist_series_dict, finished_series_dict)
    # edit_page.show_page(page)

ft.app(target=main, upload_dir="assets/img", assets_dir="assets")