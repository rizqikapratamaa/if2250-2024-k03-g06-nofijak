import flet as ft
from content import *\

series = Movie("1", "The Falcon and The Winter Soldier", 50, "Sam Wilson and Bucky Barnes realize that their futures are anything but normal.", ["Action", "Adventure", "Drama"], 8.0, "2021-04-23", "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg")

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text(series.getName())))

ft.app(main)