import datetime
import os
import shutil
import flet as ft
from content import *
from content import Content
from popup import PopUp
from edit_button import MyButton
import sqlite3

class EditPage:
    def __init__(self, content: Content, page: ft.Page):
        self.edit_text = ft.Container(
            ft.Text("Edit Information", size=20)
        )
        self.name_text = ft.Container(
            ft.Text("Name"),
            padding=ft.padding.only(left=10,right=10, top=20)
        )
        self.name_table = ft.TextField(
            value=content.getName(), 
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
            ft.Text("Release Year"),
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
            value=content.getReleaseYear(), 
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
            ft.Text("Duration"),
            padding=ft.padding.only(left=10, right=200, top=10)
        )

        self.watch_progress_text = ft.Container(
            ft.Text("Watch Progress"),
            padding=ft.padding.only(top=10)
        )
        self.jam_duration = ft.Dropdown(
                    label="Jam", 
                    border_radius=50,
                    alignment=ft.alignment.center, 
                    value=content.getDuration() // 3600, 
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
                    value=(content.getDuration() % 3600) // 60,
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
                    value=content.getDuration() % 60, 
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
                    value=content.getWatchProgress() // 3600, 
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
                    value=(content.getWatchProgress() % 3600) // 60, 
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
                    value=content.getWatchProgress() % 60, 
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
            value = str(content.getRating()), 
            text_align=ft.TextAlign.CENTER, 
            width=80, smart_dashes_type=True,
            border_radius=50, hover_color="#FED466",
            border_color="#000D20",
            focused_border_color="#FED466",
            selection_color="#FED466",
            fill_color=ft.colors.WHITE,
            color=ft.colors.BLACK, input_filter=ft.InputFilter(allow=True ,regex_string = r'[-+]?[0-9]*\.?[0-9]*', replacement_string="")
        )

        self.rating_text =ft.Container(
            ft.Text("Rating"),
            padding=ft.padding.only(left=80, right=10, top = 10)
        ) 

        self.genre_text = ft.Container(
            ft.Text("Genre"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )

        self.genre = ft.Dropdown(
                border_radius=50, 
                
                value=(content.getGenre()), 
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

        self.file_picker = ft.FilePicker(on_result=self.on_file_picker_result)

        self.poster_button = ft.Container(
            ft.ElevatedButton("Upload File", on_click=lambda _: self.file_picker.pick_files()),
            padding=ft.padding.only(left=20)
        )

        self.summary_text = ft.Container(
            ft.Text("Synopsis"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )

        self.summary = ft.TextField(
            value=content.getSummary(),
            text_align=ft.TextAlign.LEFT,
            width=480, shift_enter=True,
            fill_color=ft.colors.WHITE,
            color=ft.colors.BLACK, smart_dashes_type=True,
            border_radius=50, max_length=500,
            border_color="#000D20", hover_color="#FED466",
            focused_border_color="#FED466",
            selection_color="#FED466",
            label_style= ft.TextStyle(color="#FED466", font_family="Consolas")
        )

        self.poster = ft.Container(
            ft.Image(content.getGambar(), width=300, height=450, border_radius=30),
            padding=ft.padding.only(left=20, top=70)
        )
        self.submit_button = ft.Container(
            ft.Row([
                MyButton("Submit", on_click=lambda e: self.submit_click(e, content, page))
            ]),
            padding=ft.padding.only(top=20, left= 20)
        )


    def hours_to_seconds(self, hours, minutes, seconds):
        return int(hours * 3600) + int(minutes * 60) + int(seconds)


    def on_file_picker_result(self, e: ft.FilePickerResultEvent):
        if e.files is not None:
            for f in e.files:
                print(f"File name: {f.name}, size: {f.size} bytes")


    def submit_click(self, e,  content: Content, page: ft.Page):
        def is_overlap():
            return self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value) <= self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value)
        if self.name_table.value == "":
            PopUp("Name must be filled", page).open_dlg_modal(e, page)
        elif self.rating.value == "":
            PopUp("Rating must be filled", page).open_dlg_modal(e, page)
            return
        elif (float(self.rating.value) < 0 or float(self.rating.value) > 10) and is_overlap():
            PopUp("Rating must be between 0 and 10 and watch progress must be less than duration", page).open_dlg_modal(e, page)
        elif float(self.rating.value) < 0 or float(self.rating.value) > 10:
            PopUp("Rating must be between 0 and 10", page).open_dlg_modal(e, page)
        elif is_overlap():
            PopUp("Watch progress must be less than duration", page).open_dlg_modal(e, page)
        else:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            if self.file_picker.result != None and self.file_picker.result.files != None:
                for f in self.file_picker.result.files:
                    shutil.copy(f.path, os.path.join('assets/img/', content.getId() + '.jpg'))
            content.setName(self.name_table.value)
            content.setDuration(self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value))
            content.setWatchProgress(self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value))
            if self.date_picker.value != None:
                content.setReleaseYear(self.date_picker.value.date())
            content.setGenre(self.genre.value)
            content.setRating(float(self.rating.value))
            content.setSummary(self.summary.value)
            page.update()
            print(content.getName())
            print(content.getDuration())
            print(content.getWatchProgress())
            print(content.getReleaseYear())
            print(content.getGenre())
            print(content.getRating())
            print(content.getSummary())


    def change_date(self, e, page: ft.Page):
            self.release_year_table.value = self.date_picker.value.year
            page.update()
            print(f"Date picker changed, value is {self.date_picker.value}")

    def date_picker_dismissed(self, e):
        print(f"Date picker dismissed, value is {self.date_picker.value}")

    def show_page(self, page: ft.Page):
        page.overlay.append(self.date_picker)
        page.overlay.append(self.file_picker)
        page.add(
        ft.IconButton(ft.icons.ARROW_BACK, icon_color="#FED466", on_click=lambda e: page.update_async()),
        ft.Container(
            content= 
            ft.Row([
                ft.Container(
                    ft.Column([
                        self.edit_text,
                        self.name_text,
                        self.name_table,
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
                        self.summary,
                    ])
                ),
                ft.Container(
                    ft.Column([
                        self.poster,
                        self.poster_button,
                        self.submit_button,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    padding=ft.padding.only(left=150)
                )
            ]),
            padding=ft.padding.only(left=50,right=50)
        ),
        )
        
class MovieEditPage(EditPage):
    def __init__(self, movie: Movie, page: ft.Page, movies_dict: dict, ongoing_movies_dict: dict, review_movies_dict: dict, watchlist_movies_dict: dict):
        super().__init__(movie, page)
        self.submit_button = ft.Container(
            ft.Row([
                MyButton("Submit", on_click=lambda e: self.submit_click(e, movie, page, movies_dict, ongoing_movies_dict, review_movies_dict, watchlist_movies_dict))
            ]),
            padding=ft.padding.only(top=20, left= 20)
        )
    def submit_click(self, e,  movie: Content, page: ft.Page, movies_dict: dict, ongoing_movies_dict: dict, review_movies_dict: dict, watchlist_movies_dict: dict):
        def is_overlap():
            return self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value) <= self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value)
        if self.name_table.value == "":
            PopUp("Name must be filled", page).open_dlg_modal(e, page)
            return
        elif (float(self.rating.value) < 0 or float(self.rating.value) > 10) and is_overlap():
            PopUp("Rating must be between 0 and 10 and watch progress must be less than duration", page).open_dlg_modal(e, page)
            return
        elif float(self.rating.value) < 0 or float(self.rating.value) > 10:
            PopUp("Rating must be between 0 and 10", page).open_dlg_modal(e, page)
            return
        elif is_overlap():
            PopUp("Watch progress must be less than duration", page).open_dlg_modal(e, page)
            return
        else:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            if self.file_picker.result != None and self.file_picker.result.files != None:
                for f in self.file_picker.result.files:
                    shutil.copy(f.path, os.path.join('assets/img/', movie.getId() + '.jpg'))
        
            movie.setName(self.name_table.value)
            movies_dict[movie.getId()][1] = movie.getName()
            cursor.execute(f"UPDATE movies SET name = '{movie.getName()}' WHERE movies_id = {movie.getId()}")
            
            movie.setDuration(self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value))
            movies_dict[movie.getId()][2] = movie.getDuration()
            cursor.execute(f"UPDATE movies SET duration = {movie.getDuration()} WHERE movies_id = {movie.getId()}")
            
            if movie.getWatchProgress() == 0 and self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value) != 0:
                movie.setWatchProgress(self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value))
                watchlist_movies_dict.pop(movie.getId())
                cursor.execute(f"DELETE FROM watchlist_movies WHERE movies_id = {movie.getId()}")
                ongoing_movies_dict[movie.getId()] = [movie.getId(), self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value)]
                cursor.execute(f"INSERT INTO ongoing_movies VALUES ({movie.getId()}, {self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value)})")
            elif movie.getWatchProgress() != 0 and self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value) == 0:
                movie.setWatchProgress(0)
                ongoing_movies_dict.pop(movie.getId())
                cursor.execute(f"DELETE FROM ongoing_movies WHERE movies_id = {movie.getId()}")
                watchlist_movies_dict[movie.getId()] = [movie.getId()]
                cursor.execute(f"INSERT INTO watchlist_movies VALUES ({movie.getId()})")

            if self.date_picker.value != None:
                movie.setReleaseYear(self.date_picker.value.year)
                movies_dict[movie.getId()][3] = movie.getReleaseYear()
                cursor.execute(f"UPDATE movies SET release_year = '{movie.getReleaseYear()}' WHERE movies_id = {movie.getId()}")
            
            movie.setGenre(self.genre.value)
            movies_dict[movie.getId()][4] = movie.getGenre()
            cursor.execute(f"UPDATE movies SET genre = '{movie.getGenre()}' WHERE movies_id = {movie.getId()}")
            
            if self.rating.value != "" and movie.getId() in review_movies_dict:
                movie.setRating(float(self.rating.value))
                review_movies_dict[movie.getId()][1] = movie.getRating()
                cursor.execute(f"UPDATE review_movies SET rating = {movie.getRating()} WHERE movies_id = {movie.getId()}")
            elif self.rating.value != "" and movie.getId() not in review_movies_dict:
                movie.setRating(float(self.rating.value))
                review_movies_dict[movie.getId()] = [movie.getId(), movie.getRating()]
                cursor.execute(f"INSERT INTO review_movies VALUES ({movie.getId()}, {movie.getRating()})")
            elif self.rating.value == "" and movie.getId() in review_movies_dict:
                movie.setRating(None)
                review_movies_dict.pop(movie.getId())
                cursor.execute(f"DELETE FROM review_movies WHERE movies_id = {movie.getId()}")
            
            
            movie.setSummary(self.summary.value)
            movies_dict[movie.getId()][5] = movie.getSummary()
            cursor.execute(f"UPDATE movies SET synopsis = '{movie.getSummary()}' WHERE movies_id = {movie.getId()}")
            
            conn.commit()

            page.update()
            print("Nama: ", movie.getName())
            print("Durasi: ", movie.getDuration())
            print("Watch Progress: ", movie.getWatchProgress())
            print("Release Date: ", movie.getReleaseYear())
            print("Genre: ", movie.getGenre())
            print("Rating: ", movie.getRating())
            print("Synopsis: ", movie.getSummary())

class SeriesEditPage(EditPage):
    def __init__(self, series: Series, page: ft.Page):
        super().__init__(series, page)

        self.season_text = ft.Container(
            ft.Text("Season"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )

        self.season_table = ft.TextField(
            value=series.getSeason(),
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
            value=series.getSeasonProgress(),
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
            value=series.getEpisode(),
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
            value=series.getEpisodeProgress(),
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

    def submit_click(self, e,  series: Series, page: ft.Page):
        def is_overlap():
            return self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value) <= self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value)
        if self.name_table.value == "":
            PopUp("Name must be filled", page).open_dlg_modal(e, page)
            return
        elif self.season_table.value == "":
            PopUp("Season must be filled", page).open_dlg_modal(e, page)
            return
        elif (int(self.season_table.value) < 1):
            PopUp("Season must be greater than 0", page).open_dlg_modal(e, page)
            return
        elif  self.season_progress_table.value == "":
            PopUp("Season progress must be filled", page).open_dlg_modal(e, page)
            return
        elif (int(self.season_progress_table.value) < 0):
            PopUp("Season progress must be greater than or equal to 0", page).open_dlg_modal(e, page)
            return
        elif self.episode_table.value == "":
            PopUp("Episode must be filled", page).open_dlg_modal(e, page)
            return
        elif (int(self.episode_table.value) < 1):
            PopUp("Episode must be greater than 0", page).open_dlg_modal(e, page)
            return
        elif self.episode_progress_table.value == "":
            PopUp("Episode progress must be filled", page).open_dlg_modal(e, page)
            return
        elif (int(self.episode_progress_table.value) < 0):
            PopUp("Episode progress must be filled and greater than or equal to 0", page).open_dlg_modal(e, page)
            return
        elif (int(self.season_progress_table.value) > int(self.season_table.value)):
            PopUp("Season progress must be less than or equal to season", page).open_dlg_modal(e, page)
            return
        elif (int(self.episode_progress_table.value) > int(self.episode_table.value)):
            PopUp("Episode progress must be less than or equal to episode", page).open_dlg_modal(e, page)
            return
        elif self.rating.value == "":
            PopUp("Rating must be filled", page).open_dlg_modal(e, page)
            return
        elif (float(self.rating.value) < 0 or float(self.rating.value) > 10) and is_overlap():
            PopUp("Rating must be between 0 and 10 and watch progress must be less than duration", page).open_dlg_modal(e, page)
            return
        elif float(self.rating.value) < 0 or float(self.rating.value) > 10:
            PopUp("Rating must be between 0 and 10", page).open_dlg_modal(e, page)
            return
        elif is_overlap():
            PopUp("Watch progress must be less than duration", page).open_dlg_modal(e, page)
            return
        else:
            if self.file_picker.result != None and self.file_picker.result.files != None:
                for f in self.file_picker.result.files:
                    shutil.copy(f.path, os.path.join('assets/img/', series.getId() + '.jpg'))
            series.setName(self.name_table.value)
            series.setSeason(int(self.season_table.value))
            series.setSeasonProgress(int(self.season_progress_table.value))
            series.setEpisode(int(self.episode_table.value))
            series.setEpisodeProgress(int(self.episode_progress_table.value))
            series.setDuration(self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value))
            series.setWatchProgress(self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value))
            if self.date_picker.value != None:
                series.setReleaseYear(self.date_picker.value.date())
            series.setGenre(self.genre.value)
            series.setRating(float(self.rating.value))
            series.setSummary(self.summary.value)
            page.update()
            print(series.getName())
            print(series.getSeason())
            print(series.getSeasonProgress())
            print(series.getEpisode())
            print(series.getEpisodeProgress())
            print(series.getDuration())
            print(series.getWatchProgress())
            print(series.getReleaseYear())
            print(series.getGenre())
            print(series.getRating())
            print(series.getSummary())

    def show_page(self, page: ft.Page):
        page.overlay.append(self.date_picker)
        page.overlay.append(self.file_picker)
        page.add(
        ft.IconButton(ft.icons.ARROW_BACK, icon_color="#FED466", on_click=lambda e: page.update_async()),
        ft.Container(
            content= 
            ft.Row([
                ft.Container(
                    ft.Column([
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
                        self.summary,
                    ])
                ),
                ft.Container(
                    ft.Column([
                        self.poster,
                        self.poster_button,
                        self.submit_button,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    padding=ft.padding.only(left=150)
                )
            ]),
            padding=ft.padding.only(left=50,right=50)
        ),
        )

