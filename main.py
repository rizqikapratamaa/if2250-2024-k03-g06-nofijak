from edit_page import *
import flet as ft

movie = Movie("1", "The Falcon and The Winter Soldier", "2020-07-20", 5000, "Sam Wilson and Bucky Barnes realize that their futures are anything but normal.", "Horror", 8.0, 1000, "assets/img/1.jpg")
series = Series("2", "The Falcon and The Winter Soldier", "2020-07-20", 5000, "Sam Wilson and Bucky Barnes realize that their futures are anything but normal.", "Horror", 8.0, 1000, "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg", 1, 8)
def main(page: ft.Page):
    page.scroll = True
    page.title = "Nofijak"
    page.bgcolor = "#000D20"

    page.vertical_alignment = ft.MainAxisAlignment.START
    edit_page = EditPage(movie, page)
    edit_page.show_page(page)

ft.app(target=main, upload_dir="assets/img", assets_dir="assets")