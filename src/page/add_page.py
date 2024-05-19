import datetime
import sqlite3
from utils.popup import *
import flet as ft
from utils.content import *
from utils.button import OptionButton, SubmitButton
import os
import shutil

class AddPage:
    def __init__(self, page: ft.Page):
        self.edit_text = ft.Container(
            ft.Text("Edit Information", size=20, color="#FFFFFF")
        )
        
        self.name_text = ft.Container(
            ft.Text("Name", color="#FFFFFF"),
            padding=ft.padding.only(left=10,right=10, top=20)
        )
        
        self.name_table = ft.TextField(
            value=None, 
            text_align=ft.TextAlign.LEFT, 
            width=400, smart_dashes_type=True,
            fill_color=ft.colors.WHITE, 
            color=ft.colors.BLACK, hover_color="#FED466",
            border_radius=50, 
            border_color="#000D20", 
            focused_border_color="#FED466", 
            selection_color="#FED466", 
            label_style= ft.TextStyle(color="#FED466", font_family="Consolas")
        )
        
        self.release_year_text = ft.Container(
            ft.Text("Release Date", color="#FFFFFF"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )

        self.date_picker = ft.DatePicker(
            on_change=lambda e: self.change_date(e, page),
            on_dismiss=self.date_picker_dismissed,
            date_picker_entry_mode=ft.DatePickerEntryMode.INPUT,
            first_date=datetime.datetime(1990, 10, 1),
            last_date=datetime.datetime(2030, 10, 1), 
        )

        self.release_year_table = ft.TextField(
            value=None, 
            text_align=ft.TextAlign.CENTER, 
            width=120, 
            fill_color=ft.colors.WHITE, 
            color=ft.colors.BLACK, 
            border_radius=50, 
            border_color="#000D20", 
            focused_border_color="#FED466", 
            selection_color="#FED466", 
            disabled=True,
            label_style= ft.TextStyle(color="#FED466", font_family="Consolas")
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

        self.duration_text = ft.Container(
            ft.Text("Duration", color="#FFFFFF"),
            padding=ft.padding.only(left=10, right=200, top=10)
        )

        self.watch_progress_text = ft.Container(
            ft.Text("Watch Progress",color="#FFFFFF"),
            padding=ft.padding.only(top=10)
        )
        
        self.jam_duration = ft.Dropdown(
                    label="Jam", 
                    border_radius=50,
                    alignment=ft.alignment.center, 
                    value=0, 
                    width=65,
                    options = [ft.dropdown.Option(str(i)) for i in range(60)], 
                    bgcolor=ft.colors.WHITE, 
                    label_style= ft.TextStyle(color="#FED466", font_family="Consolas", bgcolor="#000D20"),
                    focused_border_color="#FED466",
                    border_color="#000D20",
                    color=ft.colors.BLACK
                )
        self.menit_duration = ft.Dropdown(
                    label="Menit",
                    border_radius=50,
                    value=0,
                    width=65, 
                    options= [ft.dropdown.Option(str(i)) for i in range(60)],
                    label_style= ft.TextStyle(color="#FED466", font_family="Consolas", bgcolor="#000D20"),
                    focused_border_color="#FED466",
                    bgcolor=ft.colors.WHITE,
                    color=ft.colors.BLACK
                )
        self.detik_duration = ft.Dropdown(
                    label="Detik", 
                    border_radius=50, 
                    value=0, 
                    width=65, 
                    options= [ft.dropdown.Option(str(i)) for i in range(60)], 
                    label_style= ft.TextStyle(color="#FED466", font_family="Consolas", bgcolor="#000D20"),
                    focused_border_color="#FED466",
                    bgcolor=ft.colors.WHITE, 
                    color=ft.colors.BLACK
                )
        self.duration_table = ft.Row(
            [
                self.jam_duration,
                self.menit_duration,
                self.detik_duration
            ])

        self.jam_watch_progress = ft.Dropdown(
                    label="Jam",
                    border_radius=50, 
                    value=0, 
                    width=65, 
                    options = [ft.dropdown.Option(str(i)) for i in range(60)], 
                    label_style= ft.TextStyle(color="#FED466", font_family="Consolas", bgcolor="#000D20"),
                    focused_border_color="#FED466",
                    bgcolor=ft.colors.WHITE, 
                    color=ft.colors.BLACK
                )
        self.menit_watch_progress = ft.Dropdown(
                    label="Menit", 
                    border_radius=50, 
                    value=0, 
                    width=65, 
                    options = [ft.dropdown.Option(str(i)) for i in range(60)], 
                    label_style= ft.TextStyle(color="#FED466", font_family="Consolas", bgcolor="#000D20"),
                    focused_border_color="#FED466",
                    bgcolor=ft.colors.WHITE, 
                    color=ft.colors.BLACK
                )
        self.detik_watch_progress = ft.Dropdown(
                    label="Detik", 
                    border_radius=50, 
                    value=0, 
                    width=65,
                    options = [ft.dropdown.Option(str(i)) for i in range(60)], 
                    label_style= ft.TextStyle(color="#FED466", font_family="Consolas", bgcolor="#000D20"),
                    focused_border_color="#FED466",
                    bgcolor=ft.colors.WHITE, 
                    color=ft.colors.BLACK
                )
        self.watch_progress_table = ft.Container(
            ft.Row([
                self.jam_watch_progress,
                self.menit_watch_progress,
                self.detik_watch_progress
            ]),
            padding=ft.padding.only(left=40)
        )

        self.rating = ft.TextField(
            value = None, 
            text_align=ft.TextAlign.CENTER, 
            width=80, smart_dashes_type=True,
            border_radius=50, hover_color="#FED466",
            border_color="#000D20",
            focused_border_color="#FED466",
            selection_color="#FED466",
            fill_color=ft.colors.WHITE,
            color=ft.colors.BLACK
        )

        self.rating_text =ft.Container(
            ft.Text("Rating", color="#FFFFFF"),
            padding=ft.padding.only(left=70, right=10, top = 10)
        ) 

        self.genre_text = ft.Container(
            ft.Text("Genre", color="#FFFFFF"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )

        self.genre = ft.Dropdown(
                border_radius=50, 
                
                value=None, 
                width=120, 
                options = [
                    ft.dropdown.Option("Adventure"),
                    ft.dropdown.Option("Animation"),
                    ft.dropdown.Option("Biography"),
                    ft.dropdown.Option("Comedy"),
                    ft.dropdown.Option("Crime"),
                    ft.dropdown.Option("Documentary"),
                    ft.dropdown.Option("Drama"),
                    ft.dropdown.Option("Family"),
                    ft.dropdown.Option("Fantasy"),
                    ft.dropdown.Option("History"),
                    ft.dropdown.Option("Horror"),
                    ft.dropdown.Option("Music"),
                    ft.dropdown.Option("Musical"),
                    ft.dropdown.Option("Mystery"),
                    ft.dropdown.Option("Romance"),
                    ft.dropdown.Option("Sci-Fi"),
                    ft.dropdown.Option("Sport"),
                    ft.dropdown.Option("Thriller"),
                    ft.dropdown.Option("War"),
                    ft.dropdown.Option("Western")
                ], 
                label_style= ft.TextStyle(color="#FED466", font_family="Consolas", bgcolor="#000D20"),
                focused_border_color="#FED466",
                bgcolor=ft.colors.WHITE, 
                color=ft.colors.BLACK
            )

        self.file_picker = ft.FilePicker(on_result= lambda e: self.on_file_picker_result(e, page))

        self.poster_button = ft.Container(
            ft.ElevatedButton("Upload Image", on_click=lambda _: self.file_picker.pick_files()),
            padding=ft.padding.only(left=20)
        )

        self.summary_text = ft.Container(
            ft.Text("Synopsis",color="#FFFFFF"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )

        self.summary = ft.TextField(
                value=None,
                text_align=ft.TextAlign.LEFT,
                width=480, shift_enter=True,
                fill_color=ft.colors.WHITE,
                color=ft.colors.BLACK, smart_dashes_type=True,
                border_radius=50, max_length=500,
                border_color="#000D20", hover_color="#FED466",
                focused_border_color="#FED466",
                selection_color="#FED466",
                label_style= ft.TextStyle(color="#FED466", font_family="Consolas"),
            )

        self.poster = ft.Image("../assets/img/blank.png", width=300, height=450, border_radius=30)

        self.poster_text = ft.Text(value="", size=20)

        self.option_button = ft.Container(
            content= ft.Row(
                [
                    OptionButton("Movies", on_click=lambda e: MovieAddPage(page).movies_show_page(page), bgcolor="#FED466"),
                    OptionButton("Series", on_click=lambda e: SeriesAddPage(page).series_show_page(page), bgcolor="FEF466")
                ],
                alignment= ft.MainAxisAlignment.CENTER,
                spacing= 0
                
            ),
            animate=True,
            bgcolor="#FED466",
            alignment= ft.alignment.center,
            width=200,
            height=50,
            border_radius= 30,
            padding=0,
            shape= ft.RoundedRectangleBorder(radius=30)
        )

        self.go_back_button = ft.IconButton(ft.icons.ARROW_BACK, icon_color="#FED466", on_click=lambda e: self.back_clicked(page))

    def back_clicked(self, page: ft.Page):
        page.go("/")
        self.poster.src = "../assets/img/blank.png"
        self.poster_text.value = ""
    
    def on_file_picker_result(self, e: ft.FilePickerResultEvent, page: ft.Page):
        if e.files is not None:
            file_name = e.files[0].name
            file_path = e.files[0].path
            self.poster_text.value = file_name
            print(f"Selected file: {file_name}")
            self.poster.src = file_path
            page.update()

    def change_date(self, e, page: ft.Page):
            self.release_year_table.value = self.date_picker.value.year
            page.update()
            print(f"Date picker changed, value is {self.date_picker.value}")

    def date_picker_dismissed(self, e):
        print(f"Date picker dismissed, value is {self.date_picker.value}")
        
    def hours_to_seconds(self, hours, minutes, seconds):
        return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
        
class MovieAddPage(AddPage):
    def __init__(self, page: ft.Page, kolomHalaman : ft.Column, kolomHalamanEdit : ft.Column, scrollCard, movie_dict: dict, ongoing_movie_dict: dict, review_movie_dict: dict, watchlist_movie_dict: dict, finished_movie_dict: dict, database):
        super().__init__(page)
        self.edit_text = ft.Container(
            ft.Text("Add Movie", size=20, color="#FFFFFF")
        )

        self.option_button = ft.Container(
            content= ft.Row(
                [
                    OptionButton("Movies", on_click=None, bgcolor="#CBA133"),
                    OptionButton("Series", on_click=lambda e: page.go("/tambah-film-series/series"), bgcolor="#FED466")
                ],
                alignment= ft.MainAxisAlignment.CENTER,
                spacing= 0
                
            ),
            animate=True,
            bgcolor="#FED466",
            alignment= ft.alignment.center,
            width=200,
            height=50,
            border_radius= 30,
            padding=0,
            shape= ft.RoundedRectangleBorder(radius=30)
        )

        self.add_button = ft.Container(
            ft.Row([
                SubmitButton("Add", on_click=lambda e: self.submit_click(e, page, kolomHalaman, kolomHalamanEdit, scrollCard, movie_dict, ongoing_movie_dict, review_movie_dict, watchlist_movie_dict, finished_movie_dict, database))
            ]),
            padding=ft.padding.only(top=20, left= 20)
        )


    def submit_click(self, e, page: ft.Page, kolomHalaman, kolomHalamanEdit, scrollCard, movie_dict: dict, ongoing_movie_dict: dict, review_movie_dict: dict, watchlist_movie_dict: dict, finished_movie_dict: dict, database):
        print("Submit button clicked")  # Debugging statement
        
        def is_overlap():
            # Check if watching progress is greater than duration
            if self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value) > self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value):
                return True
            else:
                return False
            
        # Additional debugging statements to trace the values
        print(f"Name: {self.name_table.value}, Rating: {self.rating.value}, Duration: {self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value)}, Release Year: {self.release_year_table.value}, Genre: {self.genre.value}")

        def call_back_dummpy(e):
            page.update()

        if self.name_table.value == "":
            print("Name is empty")  # Debugging statement
            PopUp("Warning!", "Name cannot be empty", call_back_dummpy).open_dlg_modal(e, page)
            return
        elif self.rating.value != "":
            if not 0 <= float(self.rating.value) <= 10:
                print("Invalid rating value")  # Debugging statement
                PopUp("Warning!", "Rating must be between 0 and 10", call_back_dummpy).open_dlg_modal(e, page)
                return
        elif self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value) == 0:
            print("Duration is zero")  # Debugging statement
            PopUp("Warning!", "Duration cannot be 0", call_back_dummpy).open_dlg_modal(e, page)
            return
        elif self.release_year_table.value is None:
            print("Release year is empty")  # Debugging statement
            PopUp("Warning!", "Release Date cannot be empty", call_back_dummpy).open_dlg_modal(e, page)
            return
        elif self.genre.value is None:
            print("Genre is empty")  # Debugging statement
            PopUp("Warning!", "Genre cannot be empty", call_back_dummpy).open_dlg_modal(e, page)
            return
        elif is_overlap():
            print("Watch progress is more than duration")  # Debugging statement
            PopUp("Warning!", "Watch Progress cannot be more than Duration", call_back_dummpy).open_dlg_modal(e, page)
            return
        
        print("All conditions passed")  # Debugging statement
        conn = sqlite3.connect('database/database.db')
        cursor = conn.cursor()

        def generate_new_key(dictionary):
            key = 1
            while key in dictionary:
                key += 1
            return key

        id = generate_new_key(movie_dict)
        name = self.name_table.value
        duration = self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value)
        watchProgress = self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value)
        release_year = self.release_year_table.value
        genre = self.genre.value
        rating = self.rating.value
        synopsis = self.summary.value

        print("Inserting data into database")  # Debugging statement
        try:
            if self.file_picker.result is not None and self.file_picker.result.files is not None:
                for f in self.file_picker.result.files:
                    shutil.copy(f.path, os.path.join('../assets/img/', str(id) + 'm.jpg'))

            cursor.execute("INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?)", (id, name, duration, release_year, genre, synopsis))
            movie_dict[id] = [id, name, duration, release_year, genre, synopsis]
            cursor.execute("INSERT INTO review_movies VALUES (?, ?)", (id, rating))
            review_movie_dict[id] = [id, rating]
            if watchProgress != 0:
                cursor.execute("INSERT INTO ongoing_movies VALUES (?, ?)", (id, watchProgress))
                ongoing_movie_dict[id] = [id, watchProgress]
            else:
                cursor.execute("INSERT INTO watchlist_movies VALUES (?)", (id,))
                watchlist_movie_dict[id] = [id]

            if duration == watchProgress:
                cursor.execute("INSERT INTO finished_movies VALUES (?, DATE('now'))", (id,))
                finished_movie_dict[id] = [id]
            conn.commit()
            print("Data inserted successfully")  # Debugging statement
        except Exception as ex:
            print(f"Error during database operations: {ex}")  # Debugging statement
        finally:
            conn.close()
        
        scrollCard.inisialisasiCard()
        for i in database.getMovies():
            moviee = database.make_movies(i)
            scrollCard.tambahCardMovie(
                moviee,
                page,
                kolomHalaman,
                kolomHalamanEdit
            )

        for i in database.getSeries():
            seriess = database.make_series(i)
            scrollCard.tambahCardSeries(
                seriess,
                page,
                kolomHalaman,
                kolomHalamanEdit
            )
        print("id: ", id, "name: ", name, "releaseDate: ", release_year, "duration: ", duration, "synopsis: ", synopsis, "genre: ", genre, "rating: ", rating, "watchProgress: ", watchProgress)

        def navigate_to_root(e):
            page.go("/")
            page.update()

        popup = PopUp("Success!", "Movie has been added", navigate_to_root)
        popup.open_dlg_modal(e, page)


    def movies_show_page(self, page: ft.Page):
        page.clean()
        page.overlay.append(self.date_picker)
        page.overlay.append(self.file_picker)
        page.bgcolor = "#000D20"
        page.views.append(
            ft.View(
                "/tambah-film-series/film",
                [
                    ft.Container(
                        bgcolor="#000D20",
                        content=ft.Row(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Container(
                                                content=self.go_back_button
                                            ),
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        self.option_button,
                                                        self.edit_text,
                                                        self.name_text,
                                                        self.name_table,
                                                        ft.Row(
                                                            controls=[
                                                                self.duration_text,
                                                                self.watch_progress_text
                                                            ]
                                                        ),
                                                        ft.Row(
                                                            controls=[
                                                                self.duration_table,
                                                                self.watch_progress_table,
                                                            ]
                                                        ),
                                                        self.release_year_text,
                                                        ft.Row(
                                                            controls=[
                                                                self.release_year_table,
                                                                self.calendar
                                                            ]
                                                        ),
                                                        ft.Row(
                                                            controls=[
                                                                self.genre_text,
                                                                self.rating_text
                                                            ]
                                                        ),
                                                        ft.Row(
                                                            controls=[
                                                                self.genre,
                                                                self.rating
                                                            ]
                                                        ),
                                                        ft.Row(
                                                            controls=[
                                                                self.summary_text
                                                            ]
                                                        ),
                                                        self.summary
                                                    ]
                                                ),
                                                padding=ft.padding.only(left=50, right=50)
                                            ),
                                        ]
                                    )
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            self.poster,
                                            self.poster_text,
                                            self.poster_button,
                                            self.add_button,
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                    padding=ft.padding.only(left=150)
                                )
                            ]
                        ),
                    )
                ],
                scroll=ft.ScrollMode.AUTO  # Enable scrolling for the view
            )
        )
        page.update()  
    
class SeriesAddPage(AddPage):
    def __init__(self, page: ft.Page, kolomHalaman : ft.Column, kolomHalamanEdit : ft.Column, scrollCard, series_dict, ongoing_series_dict, review_series_dict, watchlist_series_dict, finished_series_dict, database):
        super().__init__(page)

        self.edit_text = ft.Container(
            ft.Text("Add Series", size=20, color="#FFFFFF")
        )

        self.option_button = ft.Container(
            content= ft.Row(
                [
                    OptionButton("Movies", on_click=lambda e: page.go("/tambah-film-series/film"), bgcolor="#FED466"),
                    OptionButton("Series", on_click=None, bgcolor="#CBA133")
                ],
                alignment= ft.MainAxisAlignment.CENTER,
                spacing= 0
                
            ),
            animate=True,
            bgcolor="#FED466",
            alignment= ft.alignment.center,
            width=200,
            height=50,
            border_radius= 30,
            padding=0,
            shape= ft.RoundedRectangleBorder(radius=30)
        )

        self.add_button = ft.Container(
            ft.Row([
                SubmitButton("Add", on_click=lambda e: self.submit_click(e, page, kolomHalaman, kolomHalamanEdit, scrollCard, series_dict, ongoing_series_dict, review_series_dict, watchlist_series_dict, finished_series_dict, database))
            ]),
            padding=ft.padding.only(top=20, left= 20)
        )

        self.season_text = ft.Container(
            ft.Text("Season"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )

        self.season_table = ft.TextField(
            value=None,
            text_align=ft.TextAlign.CENTER,
            width=80, smart_dashes_type=True,
            fill_color=ft.colors.WHITE,
            color=ft.colors.BLACK, hover_color="#FED466",
            border_radius=50,
            border_color="#000D20",
            focused_border_color="#FED466",
            selection_color="#FED466",
            label_style= ft.TextStyle(color="#FED466", font_family="Consolas"),
            input_filter=ft.InputFilter(allow=True ,regex_string = r'\b[0-9]+\b', replacement_string="")
        )

        self.season_progress_text = ft.Container(
            ft.Text("Season Progress"),
            padding=ft.padding.only(left=75, top=10)
        )

        self.season_progress_table = ft.TextField(
            value=None,
            text_align=ft.TextAlign.CENTER,
            width=80, smart_dashes_type=True,
            fill_color=ft.colors.WHITE,
            color=ft.colors.BLACK, hover_color="#FED466",
            border_radius=50,
            border_color="#000D20",
            focused_border_color="#FED466",
            selection_color="#FED466",
            label_style= ft.TextStyle(color="#FED466", font_family="Consolas"),
            input_filter=ft.InputFilter(allow=True ,regex_string = r'\b[0-9]+\b', replacement_string="")
        )

        self.episode_text = ft.Container(
            ft.Text("Episode"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )

        self.episode_table = ft.TextField(
            value=None,
            text_align=ft.TextAlign.CENTER,
            width=80, smart_dashes_type=True,
            fill_color=ft.colors.WHITE,
            color=ft.colors.BLACK, hover_color="#FED466",
            border_radius=50,
            border_color="#000D20",
            focused_border_color="#FED466",
            selection_color="#FED466",
            label_style= ft.TextStyle(color="#FED466", font_family="Consolas"),
            input_filter=ft.InputFilter(allow=True ,regex_string = r'\b[0-9]+\b', replacement_string="")
        )

        self.episode_progress_text = ft.Container(
            ft.Text("Episode Progress"),
            padding=ft.padding.only(left=70, top=10)
        )

        self.episode_progress_table = ft.TextField(
            value=None,
            text_align=ft.TextAlign.CENTER,
            width=80, smart_dashes_type=True,
            fill_color=ft.colors.WHITE,
            color=ft.colors.BLACK, hover_color="#FED466",
            border_radius=50,
            border_color="#000D20",
            focused_border_color="#FED466",
            selection_color="#FED466",
            label_style= ft.TextStyle(color="#FED466", font_family="Consolas"),
            input_filter=ft.InputFilter(allow=True ,regex_string = r'\b[0-9]+\b', replacement_string="")
        )

    def submit_click(self, e, page: ft.Page, kolomHalaman : ft.Column, kolomHalamanEdit : ft.Column, scrollCard, series_dict: dict, ongoing_series_dict: dict, review_series_dict: dict, watchlist_series_dict: dict, finished_series_dict: dict, database):
        print("Submit button clicked")  # Debugging statement
        
        def call_back_dummpy(e):
            page.update()

        def is_overlap():
            # Check if watching progress is greater than duration
            if self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value) > self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value):
                return True
            else:
                return False
            
        # Additional debugging statements to trace the values
        print(f"Name: {self.name_table.value}, Rating: {self.rating.value}, Duration: {self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value)}, Release Year: {self.release_year_table.value}, Genre: {self.genre.value}, Season: {self.season_table.value}, Episode: {self.episode_table.value}")

        if self.name_table.value == "":
            print("Name is empty")  # Debugging statement
            PopUp("Warning!", "Name cannot be empty", call_back_dummpy).open_dlg_modal(e, page)
            return
        elif self.rating.value != "":
            if not 0 <= float(self.rating.value) <= 10:
                print("Invalid rating value")  # Debugging statement
                PopUp("Warning!", "Rating must be between 0 and 10", call_back_dummpy).open_dlg_modal(e, page)
                return
        elif self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value) == 0:
            print("Duration is zero")  # Debugging statement
            PopUp("Warning!", "Duration cannot be 0", call_back_dummpy).open_dlg_modal(e, page)
            return
        elif self.release_year_table.value is None:
            print("Release year is empty")  # Debugging statement
            PopUp("Warning!", "Release Date cannot be empty", call_back_dummpy).open_dlg_modal(e, page)
            return
        elif self.genre.value is None:
            print("Genre is empty")  # Debugging statement
            PopUp("Warning!", "Genre cannot be empty", call_back_dummpy).open_dlg_modal(e, page)
            return
        elif is_overlap():
            print("Watch progress is more than duration")  # Debugging statement
            PopUp("Warning!", "Watch Progress cannot be more than Duration", call_back_dummpy).open_dlg_modal(e, page)
            return
        elif self.season_table.value == 0:
            print("Season is empty")  # Debugging statement
            PopUp("Warning!", "Season cannot be empty", call_back_dummpy).open_dlg_modal(e, page)
            return
        elif self.episode_table.value == "":
            print("Episode is empty")  # Debugging statement
            PopUp("Warning!", "Episode cannot be empty", call_back_dummpy).open_dlg_modal(e, page)
            return
    
        print("All conditions passed")  # Debugging statement
        conn = sqlite3.connect('database/database.db')
        cursor = conn.cursor()
        try:

            def generate_new_key(dictionary):
                key = 1
                while key in dictionary:
                    key += 1
                return key

            id = generate_new_key(series_dict)
            name = self.name_table.value
            season = self.season_table.value
            episode = self.episode_table.value
            season_progress = self.season_progress_table.value
            episode_progress = self.episode_progress_table.value
            duration = self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value)
            watchProgress = self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value)
            release_year = self.release_year_table.value
            genre  = self.genre.value
            rating = self.rating.value
            synopsis = self.summary.value

            print("Inserting data into database")

            if self.file_picker.result is not None and self.file_picker.result.files is not None:
                for f in self.file_picker.result.files:
                    shutil.copy(f.path, os.path.join('../assets/img/', str(id) + 's.jpg'))

            cursor.execute("INSERT INTO series VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id, name, duration, release_year, genre, synopsis, season, episode))
            series_dict[id] = [id, name, duration, release_year, genre, synopsis, season, episode]

            if self.rating.value is not None:
                cursor.execute("INSERT INTO review_series VALUES (?, ?, ?)", (id, rating, "Selamat anda menemukan easter egg"))
                review_series_dict[id] = [id, rating, "Selamat anda menemukan easter egg"]
            
            if (season_progress == "" or season_progress == 0) or (episode_progress == "" or episode_progress == 0):
                cursor.execute("INSERT INTO watchlist_series VALUES (?)", (id,))
                watchlist_series_dict[id] = [id]
            
            if (season_progress is not None and season_progress != 0) or (episode_progress is not None and episode_progress != 0):
                cursor.execute("INSERT INTO ongoing_series VALUES (?, ?, ?, ?)", (id, season_progress, episode_progress, watchProgress))
                ongoing_series_dict[id] = [id, season_progress, episode_progress, watchProgress]
            
            if season == season_progress and episode == episode_progress and duration == watchProgress:
                cursor.execute("INSERT INTO finished_series VALUES (?, DATE('now'))", (id,))
                finished_series_dict[id] = [id]
            
            conn.commit()
            print("Data inserted successfully")  # Debugging statement
        except Exception as ex:
            print(f"Error during database operations: {ex}")  # Debugging statement
        finally:
            conn.close()

        scrollCard.inisialisasiCard()
        for i in database.getMovies():
            moviee = database.make_movies(i)
            scrollCard.tambahCardMovie(
                moviee,
                page,
                kolomHalaman,
                kolomHalamanEdit
            )

        for i in database.getSeries():
            seriess = database.make_series(i)
            scrollCard.tambahCardSeries(
                seriess,
                page,
                kolomHalaman,
                kolomHalamanEdit
            )

        print("id: ", id, "name: ", name, "releaseDate: ", release_year, "duration: ", duration, "synopsis: ", synopsis, "genre: ", genre, "rating: ", rating, "watchProgress: ", watchProgress, "season: ", season, "episode: ", episode, "current_season: ", season_progress, "current_episode: ", episode_progress)

        def navigate_to_root(e):
            page.go("/")
            page.update()

        popup = PopUp("Success!", "series has been added", navigate_to_root)
        popup.open_dlg_modal(e, page)


    def series_show_page(self, page: ft.Page):
        page.overlay.append(self.date_picker)
        page.overlay.append(self.file_picker)
        page.bgcolor = "#000D20"
        page.views.append(
            ft.View(
                "/tambah-film-series/series",
                [
                    ft.Container(
                        bgcolor="#000D20",
                        content = ft.Row([
                            ft.Container(
                                ft.Column([
                                    ft.Container(
                                        content=self.go_back_button
                                    ),
                                    ft.Container(
                                        ft.Column([
                                            self.option_button,
                                            self.edit_text,
                                            self.name_text,
                                            self.name_table,
                                            ft.Row([
                                                self.season_text,
                                                self.season_progress_text
                                            ]),
                                            ft.Row([
                                                self.season_table,
                                                ft.Container(
                                                    self.season_progress_table,
                                                    padding=ft.padding.only(left=50)
                                                ),
                                            ]),
                                            ft.Row([
                                                self.episode_text,
                                                self.episode_progress_text
                                            ]),
                                            ft.Row([
                                                self.episode_table,
                                                ft.Container(
                                                    self.episode_progress_table,
                                                    padding=ft.padding.only(left=50)
                                                )
                                            ]),
                                            ft.Row([
                                                self.duration_text,
                                                self.watch_progress_text
                                            ]),
                                            ft.Row([
                                                self.duration_table,
                                                self.watch_progress_table,
                                            ]),
                                            self.release_year_text,
                                            ft.Row([
                                                self.release_year_table,
                                                self.calendar
                                            ]),
                                            ft.Row([
                                                self.genre_text,
                                                self.rating_text
                                            ]),
                                            ft.Row([
                                                self.genre,
                                                ft.Container(
                                                    self.rating,
                                                    padding=ft.padding.only(left=10)
                                                )
                                            ]),
                                            ft.Row([
                                                self.summary_text
                                            ]),
                                            self.summary
                                        ]),
                                        padding=ft.padding.only(left=50,right=50)
                                    ),
                                    
                                ]),
                            ),
                            ft.Container(
                                ft.Column([
                                    self.poster,
                                    self.poster_text,
                                    self.poster_button,
                                    self.add_button,
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                ),
                                padding=ft.padding.only(left=150)
                            )
                        ]),
                    )
                ],
                scroll=ft.ScrollMode.AUTO 
            )
        )