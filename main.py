import flet as ft
from content import *\

series = Movie("1", "The Falcon and The Winter Soldier", 50, "Sam Wilson and Bucky Barnes realize that their futures are anything but normal.", ["Action", "Adventure", "Drama"], 8.0, "2021-04-23", "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg")

def main(page: ft.Page):
    page.title = "Nofijak"
    page.vertical_alignment = ft.MainAxisAlignment.START

    rating_number = ft.TextField(value = str(series.getRating()), text_align=ft.TextAlign.RIGHT, width=100)

    genre = ', '.join(series.getGenre())

    def minus_click(e):
        rating_number.value = str(float(rating_number.value) - 1.0)
        page.update()

    def plus_click(e):
        rating_number.value = str(float(rating_number.value) + 1.0)
        page.update()


    page.add(
        ft.Row(
            [
                ft.Text("Name: "),
                ft.TextField(value = str(series.getName()), text_align=ft.TextAlign.LEFT, width=300)
            ],
            alignment=ft.MainAxisAlignment.START
        ),
        ft.Row(
            [
                ft.Text("Duration: "),
                ft.TextField(value = str(series.getDuration()), text_align=ft.TextAlign.LEFT, width=100)
            ],
            alignment=ft.MainAxisAlignment.START
        ),
        ft.Row(
            [
                ft.Text("Summary: "),
                ft.TextField(value = str(series.getSummary()), text_align=ft.TextAlign.LEFT, width=500)
            ],
            alignment=ft.MainAxisAlignment.START
        ),
        ft.Row(
            [
                ft.Text("Genre: "),
                ft.TextField(value = str(genre), text_align=ft.TextAlign.LEFT, width=200)
            ],
            alignment=ft.MainAxisAlignment.START
        ),
        ft.Row(
            [
                ft.Text("Rate: "),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                rating_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.START,
        )
        )

ft.app(main)