from add_page import *
import flet as ft

def main(page: ft.Page):
    page.scroll = True
    page.title = "Nofijak"
    page.bgcolor = "#000D20"

    page.vertical_alignment = ft.MainAxisAlignment.START
    film_page = AddPage(page)
    film_page.show_page(page)


ft.app(target=main)