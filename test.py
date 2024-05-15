import datetime
import os
import shutil
import flet as ft
from content import *
from content import Content
from edit_button import MyButton

class AddPage:
    def __init__(self, content: Content, route: str):
        self.route = route

        # Inisialisasi elemen-elemen UI lainnya...
        self.edit_text = ft.Container(
            ft.Text("Edit Information", size=20, color="#FFFFFF")
        )
        self.name_text = ft.Container(
            ft.Text("Name", color="#FFFFFF"),
            padding=ft.padding.only(left=10, right=10, top=20)
        )
        self.name_table = ft.TextField(
            value=content.getName(),
            text_align=ft.TextAlign.LEFT,
            width=400,
            smart_dashes_type=True,
            fill_color=ft.colors.WHITE,
            color=ft.colors.BLACK,
            hover_color="#FED466",
            border_radius=50,
            border_color="#000D20",
            focused_border_color="#FED466",
            selection_color="#FED466",
            label_style=ft.TextStyle(color="#FED466", font_family="Consolas")
        )
        self.release_date_text = ft.Container(
            ft.Text("Release Date", color="#FFFFFF"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )
        self.date_picker = ft.DatePicker(
            on_change=self.change_date,
            on_dismiss=self.date_picker_dismissed,
            date_picker_entry_mode=ft.DatePickerEntryMode.INPUT,
            first_date=datetime.datetime(1990, 10, 1),
            last_date=datetime.datetime(2030, 10, 1),
        )
        self.release_date_table = ft.TextField(
            value=content.getReleaseDate(),
            text_align=ft.TextAlign.LEFT,
            width=120,
            fill_color=ft.colors.WHITE,
            color=ft.colors.BLACK,
            border_radius=50,
            border_color="#000D20",
            focused_border_color="#FED466",
            selection_color="#FED466",
            disabled=True,
            label_style=ft.TextStyle(color="#FED466", font_family="Consolas")
        )
        self.calendar = ft.Container(
            content=ft.ElevatedButton(
                "Calendar",
                icon=ft.icons.CALENDAR_MONTH,
                bgcolor=ft.colors.WHITE,
                color=ft.colors.BLACK,
                on_click=lambda _: self.date_picker.pick_date(),
            ),
            padding=ft.padding.only(left=5)
        )

        # Inisialisasi elemen-elemen UI lainnya seperti durasi, progress, genre, dll...

        self.file_picker = ft.FilePicker(on_result=self.on_file_picker_result)
        self.poster_button = ft.Container(
            ft.ElevatedButton("Upload File", on_click=lambda _: self.file_picker.pick_files()),
            padding=ft.padding.only(left=20)
        )
        self.submit_button = ft.Container(
            ft.Row([
                MyButton("Submit", on_click=self.submit_click)
            ]),
            padding=ft.padding.only(top=20, left=20)
        )

        self.navbar = self.NavBar(route)

    def on_file_picker_result(self, e: ft.FilePickerResultEvent):
        if e.files is not None:
            for f in e.files:
                print(f"File name: {f.name}, size: {f.size} bytes")

    def submit_click(self, e):
        # Implementasi logika submit di sini...
        print("Submit button clicked")

    def change_date(self, e):
        self.release_date_table.value = self.date_picker.value.date()
        e.page.update()
        print(f"Date picker changed, value is {self.date_picker.value}")

    def date_picker_dismissed(self, e):
        print(f"Date picker dismissed, value is {self.date_picker.value}")

    @staticmethod
    def film_button_clicked(e):
        print("Film Button Clicked")

    @staticmethod
    def series_button_clicked(e):
        print("Series Button Clicked")

    @staticmethod
    def Film_button(current_page):
        return ft.TextButton(
            text="Film",
            width=100,
            height=50,
            style=ft.ButtonStyle(
                bgcolor="#CBA133" if current_page == "Movie" else "#FED466",
                color=ft.colors.BLACK,
                shape=ft.RoundedRectangleBorder(),
            ),
            on_click=AddPage.film_button_clicked
        )

    @staticmethod
    def Series_button(current_page):
        return ft.TextButton(
            text="Series",
            width=100,
            height=50,
            style=ft.ButtonStyle(
                bgcolor="#CBA133" if current_page == "Series" else "#FED466",
                color=ft.colors.BLACK,
                shape=ft.RoundedRectangleBorder(),
            ),
            on_click=AddPage.series_button_clicked
        )

    @staticmethod
    def NavBar(current_page):
        return ft.Container(
            content=ft.Row(
                [
                    AddPage.Film_button(current_page),
                    AddPage.Series_button(current_page)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=0,
            ),
            alignment=ft.alignment.center,
            width=200,
            height=50,
            border_radius=30,
            padding=0
        )

    def show_page(self, page: ft.Page):
        page.overlay.append(self.date_picker)
        page.overlay.append(self.file_picker)
        page.add(
            ft.IconButton(ft.icons.ARROW_BACK, icon_color="#FED466", on_click=lambda e: page.update()),
            self.navbar,
            ft.Container(
                content=ft.Row([
                    ft.Container(
                        ft.Column([
                            self.edit_text,
                            self.name_text,
                            self.name_table,
                            # Add other UI elements here
                        ])
                    ),
                    # Add more containers and elements as needed
                ]),
                padding=ft.padding.only(left=50, right=50)
            ),
        )
        page.update()

class MovieAddPage(AddPage):
    def __init__(self, movie: Movie):
        super().__init__(movie, "Movie")

class SeriesAddPage(AddPage):
    def __init__(self, series: Series):
        super().__init__(series, "Series")
        self.season_text = ft.Container(
            ft.Text("Season"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )
        self.season_table = ft.TextField(
            value=str(series.season),
            text_align=ft.TextAlign.LEFT,
            width=300,
            fill_color=ft.colors.WHITE,
            color=ft.colors.BLACK,
            border_radius=50,
            border_color="#000D20",
            focused_border_color="#FED466",
            selection_color="#FED466",
            label_style=ft.TextStyle(color="#FED466", font_family="Consolas")
        )
        self.episode_text = ft.Container(
            ft.Text("Episode"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )
        self.episode_table = ft.TextField(
            value=str(series.episode),
            text_align=ft.TextAlign.LEFT,
            width=300,
            fill_color=ft.colors.WHITE,
            color=ft.colors.BLACK,
            border_radius=50,
            border_color="#000D20",
            focused_border_color="#FED466",
            selection_color="#FED466",
            label_style=ft.TextStyle(color="#FED466", font_family="Consolas")
        )

    def show_page(self, page: ft.Page):
        super().show_page(page)
        page.add(
            ft.Container(
                content=ft.Row([
                    ft.Column([
                        self.season_text,
                        self.season_table,
                        self.episode_text,
                        self.episode_table,
                        # Add other UI elements here
                    ]),
                    # Add more containers and elements as needed
                ]),
                padding=ft.padding.only(left=50, right=50)
            ),
        )
        page.update()

# Contoh penggunaan:
def main(page: ft.Page):
    page.title = "Nofijak"
    page.bgcolor = "#000D20"
    page.vertical_alignment = ft.MainAxisAlignment.START

    movie = Movie("1", "The Falcon and The Winter Soldier", "2020-07-20", 5000, "Sam Wilson and Bucky Barnes realize that their futures are anything but normal.", "Horror", 8.0, 1000, "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg")
    series = Series("2", "The Falcon and The Winter Soldier", "2020-07-20", 5000, "Sam Wilson and Bucky Barnes realize that their futures are anything but normal.", "Horror", 8.0, 1000, "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg", 1, 8)

    film_page = MovieAddPage(movie)
    series_page = SeriesAddPage(series)

    film_page.show_page(page)  # Example: Show the film page
    # series_page.show_page(page)  # Uncomment to show the series page

ft.app(target=main)
