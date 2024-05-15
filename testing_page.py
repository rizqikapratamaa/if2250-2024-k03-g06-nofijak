import flet as ft
from content import *

def film_button_clicked(e):
    movie = Movie(" ", " ", "2020-07-20", 0, " ", "Adventure", 0, 0, "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg")
    film_page = MovieAddPage(movie)
    film_page.show_page(ft.Page())

def Film_button(current_page):
    return ft.TextButton(
        text="Film",
        width=100,
        height=50,
    
        style=ft.ButtonStyle(
            bgcolor="#CBA133" if current_page == "Movie" else "#FED466",
            color=ft.colors.BLACK,
            shape= ft.RoundedRectangleBorder(),
        ),
        on_click=film_button_clicked

    )

def series_button_clicked(e):
    series = Series("", "", "2020-0-0", 0, "", "Adventure", 0, 0, "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg", 1, 8)
    series_page = SeriesAddPage(series)
    series_page.show_page(ft.Page())

def Series_button(current_page):
    return ft.TextButton(
        text="Series",
        width=100,
        height=50,
        style=ft.ButtonStyle(
            bgcolor="#CBA133" if current_page == "Series" else "#FED466",
            color=ft.colors.BLACK,
            shape= ft.RoundedRectangleBorder(),
        ),
        on_click=series_button_clicked

    )
def NavBar(current_page):
    return ft.Container(
        content= ft.Row(
            [
                Film_button(current_page),
                Series_button(current_page)
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            spacing= 0,
            
        ),
        alignment= ft.alignment.center,
        width=200,
        height=50,
        border_radius= 30,
        padding=0
    )