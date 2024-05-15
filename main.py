from add_page import *
import flet as ft

movie = Movie(" ", " ", "2020-07-20", 0, " ", "Adventure", 0, 0, "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg")
series = Series("2", "The Falcon and The Winter Soldier", "2020-07-20", 5000, "Sam Wilson and Bucky Barnes realize that their futures are anything but normal.", "Horror", 8.0, 1000, "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg", 1, 8)
def main(page: ft.Page):
    page.title = "Nofijak"
    page.bgcolor = "#000D20"

    page.vertical_alignment = ft.MainAxisAlignment.START
    film_page = MovieAddPage(movie, page, "Movie")
    series_page = SeriesAddPage(series, page, "Series")

    # film_page.show_page(page)
    film_page.show_page(page)
    # page.update()


ft.app(target=main)