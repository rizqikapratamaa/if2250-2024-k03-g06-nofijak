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
    print(database.getMovies())

ft.app(target=main, upload_dir="assets/img", assets_dir="assets")