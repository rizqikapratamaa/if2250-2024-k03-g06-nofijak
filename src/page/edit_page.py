import datetime
import os
import shutil
import flet as ft
from utils.content import *
from utils.popup import PopUp
from utils.button import SubmitButton
import sqlite3

class EditPage(ft.Container):
    def __init__(self, content: Content, page: ft.Page,  movies_dict: dict, ongoing_movies_dict: dict, review_movies_dict: dict, watchlist_movies_dict: dict, finished_movies_dict):
        super().__init__()
        self.width = page.window_width
        self.height = page.window_height
        
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
                    value=content.getDuration() // 3600 if content.getDuration() != None else 0, 
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
                    value=(content.getDuration() % 3600) // 60 if content.getDuration() != None else 0,
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
                    value=content.getDuration() % 60 if content.getDuration() != None else 0, 
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
                    value=content.getWatchProgress() // 3600 if content.getWatchProgress() != None else 0, 
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
                    value=(content.getWatchProgress() % 3600) // 60 if content.getWatchProgress() != None else 0, 
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
                    value=content.getWatchProgress() % 60 if content.getWatchProgress() != None else 0, 
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
        
        self.file_picker = ft.FilePicker(on_result= lambda e: self.on_file_picker_result(e, page))

        self.poster_button = ft.Container(
            ft.ElevatedButton("Upload Image", on_click=lambda _: self.file_picker.pick_files()),
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

        self.submit_button = ft.Container(
            ft.Row([
                SubmitButton("Submit", on_click=lambda e: self.submit_click(e, content, page, movies_dict, ongoing_movies_dict, review_movies_dict, watchlist_movies_dict, finished_movies_dict))
            ]),
            padding=ft.padding.only(top=20, left= 20)
        )

        self.poster = ft.Image(content.getGambar(), width=300, height=450, border_radius=30)

        self.gambar = content.getGambar()

        self.poster_text = ft.Text(value="", size=20)

        self.go_back_button = ft.IconButton(ft.icons.ARROW_BACK, icon_color="#FED466", on_click=lambda e: self.go_back(page))

        self.content = ft.Container(
                        bgcolor="#000D20",
                        content = ft.Row([
                            ft.Container(
                                ft.Column([
                                    ft.Container(
                                        self.go_back_button
                                    ),
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
                                                self.rating
                                            ]),
                                            ft.Row([
                                                self.summary_text
                                            ]),
                                            self.summary
                                        ]),
                                        padding=ft.padding.only(left=50, right=50, bottom=100)
                                    ),
                                    
                                ]),
                            ),
                            ft.Container(
                                ft.Column([
                                    self.poster,
                                    self.poster_text,
                                    self.poster_button,
                                    self.submit_button,
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                ),
                                padding=ft.padding.only(left=150)
                            )
                        ]),
                    )
        page.overlay.append(self.date_picker)
        page.overlay.append(self.file_picker)

        

    def go_back(self, page: ft.Page):
        page.go("/informasi-film-series")
        self.poster.src = self.gambar
        self.poster_text.value = ""

    def hours_to_seconds(self, hours, minutes, seconds):
        return int(hours) * 3600 + int(minutes) * 60 + int(seconds)


    def on_file_picker_result(self, e: ft.FilePickerResultEvent, page: ft.Page):
        if e.files is not None:
            file_name = e.files[0].name
            file_path = e.files[0].path
            self.poster_text.value = file_name
            print(f"Selected file: {file_name}")
            self.poster.src = file_path
            page.update()


    def submit_click(self, e,  content: Content, page: ft.Page,  movies_dict: dict, ongoing_movies_dict: dict, review_movies_dict: dict, watchlist_movies_dict: dict, finished_movies_dict: dict):
        def is_overlap():
            return self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value) <= self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value)
        if self.name_table.value == "":
            PopUp("Name must be filled", page).open_dlg_modal(e, page)
        elif self.rating.value == "":
            PopUp("Rating must be filled", page).open_dlg_modal(e, page)
            return
        elif (float(self.rating.value) < 0 or float(self.rating.value) > 10) and is_overlap():
            PopUp("Rating must be between 0 and 10 and watch progress must be less than duration", page).open_dlg_modal(e, page)
            return
        elif float(self.rating.value) < 0 or float(self.rating.value) > 10:
            PopUp("Rating must be between 0 and 10", page).open_dlg_modal(e, page)
        elif not is_overlap():
            PopUp("Watch progress must be less than duration", page).open_dlg_modal(e, page)
        else:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            if self.file_picker.result != None and self.file_picker.result.files != None:
                for f in self.file_picker.result.files:
                    shutil.copy(f.path, os.path.join('../assets/img/', content.getId() + '.jpg'))
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
        page.clean()
        page.overlay.append(self.date_picker)
        page.overlay.append(self.file_picker)
        page.bgcolor = "#000D20"
        page.add(
                [
                    
                ]
        )
        
class MovieEditPage(EditPage):
    def __init__(self, movie: Movie, page: ft.Page, movies_dict: dict, ongoing_movies_dict: dict, review_movies_dict: dict, watchlist_movies_dict: dict, finished_movies_dict: dict):
        super().__init__(movie, page, movies_dict, ongoing_movies_dict, review_movies_dict, watchlist_movies_dict, finished_movies_dict)
        self.width = page.window_width,
        self.height = page.window_height+100,
        self.submit_button = ft.Container(
            ft.Row([
                SubmitButton("Submit", on_click=lambda e: self.submit_click(e, movie, page, movies_dict, ongoing_movies_dict, review_movies_dict, watchlist_movies_dict, finished_movies_dict))
            ]),
            padding=ft.padding.only(top=20, left= 20)
        )
    def submit_click(self, e, movie: Content, page: ft.Page, movies_dict: dict, ongoing_movies_dict: dict, review_movies_dict: dict, watchlist_movies_dict: dict, finished_movies_dict: dict):
        def is_overlap():
            # Check if watching progress is greater than duration
            if self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value) > self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value):
                return True
            else:
                return False

        def call_back_dummpy(e):
            page.update()

        def show_popup(message):
            PopUp("Warning!", message, call_back_dummpy).open_dlg_modal(e, page)

        # Check for empty name
        if self.name_table.value == "":
            show_popup("Name must be filled")
            return

        # Check for valid rating
        try:
            rating = float(self.rating.value)
            if not (0 <= rating <= 10):
                show_popup("Rating must be between 0 and 10")
                return
        except ValueError:
            rating = None

        # Check for overlap
        if is_overlap():
            show_popup("Watch progress must be less than or equal to duration")
            return
        try:
            conn = sqlite3.connect('database/database.db')
            cursor = conn.cursor()

            # Handle file upload
            if self.file_picker.result and self.file_picker.result.files:
                for f in self.file_picker.result.files:
                    shutil.copy(f.path, os.path.join('../assets/img/', f'{movie.getId()}m.jpg'))

            # Update movie name
            movie.setName(self.name_table.value)
            movies_dict[movie.getId()][1] = movie.getName()
            cursor.execute("UPDATE movies SET name = ? WHERE movies_id = ?", (movie.getName(), movie.getId()))

            # Update movie duration
            duration = self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value)
            movie.setDuration(duration)
            movies_dict[movie.getId()][2] = movie.getDuration()
            cursor.execute("UPDATE movies SET duration = ? WHERE movies_id = ?", (movie.getDuration(), movie.getId()))

            # Update watch progress
            duration = self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value)
            watch_progress = self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value)
            
            if watch_progress == duration:
                movie.setWatchProgress(duration)
                movie.setDuration(duration)
                finished_movies_dict[movie.getId()] = [movie.getId()]
                if movie.getId() in watchlist_movies_dict:
                    watchlist_movies_dict.pop(movie.getId())
                    cursor.execute("DELETE FROM watchlist_movies WHERE movies_id = ?", (movie.getId(),))
                if movie.getId() in ongoing_movies_dict:
                    ongoing_movies_dict.pop(movie.getId())
                    cursor.execute("DELETE FROM ongoing_movies WHERE movies_id = ?", (movie.getId(),))
                cursor.execute("INSERT INTO finished_movies (movies_id) VALUES (?)", (movie.getId(),))

            elif watch_progress != duration and watch_progress != 0:
                if movie.getId() in finished_movies_dict:
                    finished_movies_dict.pop(movie.getId())
                    cursor.execute("DELETE FROM finished_movies WHERE movies_id = ?", (movie.getId(),))
                movie.setWatchProgress(watch_progress)
                ongoing_movies_dict[movie.getId()] = [movie.getId(), watch_progress]
                cursor.execute("INSERT INTO ongoing_movies (movies_id, watched_duration) VALUES (?, ?)", (movie.getId(), watch_progress))
            
            elif movie.getWatchProgress() == 0 and watch_progress != 0:
                movie.setWatchProgress(watch_progress)
                if movie.getId() in watchlist_movies_dict:
                    watchlist_movies_dict.pop(movie.getId())
                    cursor.execute("DELETE FROM watchlist_movies WHERE movies_id = ?", (movie.getId(),))
                ongoing_movies_dict[movie.getId()] = [movie.getId(), watch_progress]
                cursor.execute("INSERT INTO ongoing_movies (movies_id, watched_duration) VALUES (?, ?)", (movie.getId(), watch_progress))

            elif movie.getWatchProgress() != 0 and watch_progress == 0:
                movie.setWatchProgress(0)
                if movie.getId() in ongoing_movies_dict:
                    ongoing_movies_dict.pop(movie.getId())
                    cursor.execute("DELETE FROM ongoing_movies WHERE movies_id = ?", (movie.getId(),))
                watchlist_movies_dict[movie.getId()] = [movie.getId()]
                cursor.execute("INSERT INTO watchlist_movies (movies_id) VALUES (?)", (movie.getId(),))
                

            elif watch_progress != 0:
                movie.setWatchProgress(watch_progress)
                ongoing_movies_dict[movie.getId()][1] = movie.getWatchProgress()
                cursor.execute("UPDATE ongoing_movies SET watched_duration = ? WHERE movies_id = ?", (movie.getWatchProgress(), movie.getId()))


            # Update release year
            if self.date_picker.value:
                movie.setReleaseYear(self.date_picker.value.year)
                movies_dict[movie.getId()][3] = movie.getReleaseYear()
                cursor.execute("UPDATE movies SET release_year = ? WHERE movies_id = ?", (movie.getReleaseYear(), movie.getId()))

            # Update genre
            movie.setGenre(self.genre.value)
            movies_dict[movie.getId()][4] = movie.getGenre()
            cursor.execute("UPDATE movies SET genre = ? WHERE movies_id = ?", (movie.getGenre(), movie.getId()))

            # Update rating
            if rating is not None or rating != 0:
                movie.setRating(rating)
                if movie.getId() in review_movies_dict:
                    review_movies_dict[movie.getId()][1] = movie.getRating()
                    cursor.execute("UPDATE review_movies SET rating = ? WHERE movies_id = ?", (movie.getRating(), movie.getId()))
                else:
                    review_movies_dict[movie.getId()] = [movie.getId(), movie.getRating()]
                    cursor.execute("INSERT INTO review_movies (movies_id, rating) VALUES (?, ?)", (movie.getId(), movie.getRating()))
            elif movie.getId() in review_movies_dict:
                movie.setRating(None)
                review_movies_dict.pop(movie.getId())
                cursor.execute("DELETE FROM review_movies WHERE movies_id = ?", (movie.getId(),))

            # Update summary
            movie.setSummary(self.summary.value)
            movies_dict[movie.getId()][5] = movie.getSummary()
            cursor.execute("UPDATE movies SET synopsis = ? WHERE movies_id = ?", (movie.getSummary(), movie.getId()))

            conn.commit()
        except Exception as error:
            print(f"Error occurred: {error}")
        finally:
            conn.close()

        

        print("Nama: ", movie.getName())
        print("Durasi: ", movie.getDuration())
        print("Watch Progress: ", movie.getWatchProgress())
        print("Release Date: ", movie.getReleaseYear())
        print("Genre: ", movie.getGenre())
        print("Rating: ", movie.getRating())
        print("Synopsis: ", movie.getSummary())


        def navigate_to_information(e):
            page.go("/informasi-film-series")
            page.update()

        popup = PopUp("Success!", "Your movies has successfully updated", navigate_to_information)
        popup.open_dlg_modal(e, page)

class SeriesEditPage(EditPage):
    def __init__(self, series: Series, page: ft.Page, series_dict: dict, ongoing_series_dict: dict, review_series_dict: dict, watchlist_series_dict: dict, finished_series_dict: dict):
        super().__init__(series, page, series_dict, ongoing_series_dict, review_series_dict, watchlist_series_dict, finished_series_dict)
        self.width = page.window_width,
        self.height = page.window_height+150,
        self.body = series

        self.submit_button = ft.Container(
            ft.Row([
                SubmitButton("Submit", on_click=lambda e: self.submit_click(e, series, page, series_dict, ongoing_series_dict, review_series_dict, watchlist_series_dict, finished_series_dict))
            ]),
            padding=ft.padding.only(top=20, left= 20)
        )

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

        self.content = ft.Container(
                        bgcolor="#000D20",
                        content = ft.Row([
                            ft.Container(
                                ft.Column([
                                    ft.Container(
                                        self.go_back_button
                                    ),
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
                                            self.summary
                                        ]),
                                        padding=ft.padding.only(left=50,right=50, bottom=100)
                                    ),
                                    
                                ]),
                            ),
                            ft.Container(
                                ft.Column([
                                    self.poster,
                                    self.poster_text,
                                    self.poster_button,
                                    self.submit_button,
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                ),
                                padding=ft.padding.only(left=150)
                            )
                        ]),
                    )

    def submit_click(self, e, series: Series, page: ft.Page, series_dict: dict, ongoing_series_dict: dict, review_series_dict: dict, watchlist_series_dict: dict, finished_series_dict: dict):
        def is_overlap():
            # Check if watching progress is greater than duration
            if self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value) > self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value):
                return True
            else:
                return False
        def call_back_dummpy(e):
            page.update()

        def show_popup(message):
            PopUp("Warning!", message, call_back_dummpy).open_dlg_modal(e, page)
        
        def hours_to_seconds(hours, minutes, seconds):
            return int(hours) * 3600 + int(minutes) * 60 + int(seconds)

        # Validate fields
        try:
            season = int(self.season_table.value)
            season_progress = int(self.season_progress_table.value)
            episode = int(self.episode_table.value)
            episode_progress = int(self.episode_progress_table.value)
            watch_progress = hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value)
            rating = float(self.rating.value) if self.rating.value != "" else None
        except ValueError:
            show_popup("All numeric fields must be valid numbers")
            return

        if self.name_table.value == "":
            show_popup("Name must be filled")
            return
        elif self.season_table.value == "":
            show_popup("Season must be filled")
            return
        elif season < 1:
            show_popup("Season must be greater than 0")
            return
        elif season_progress < 0:
            show_popup("Season progress must be greater than or equal to 0")
            return
        elif self.episode_table.value == "":
            show_popup("Episode must be filled")
            return
        elif episode < 1:
            show_popup("Episode must be greater than 0")
            return
        elif self.episode_progress_table.value == "":
            show_popup("Episode progress must be filled")
            return
        elif episode_progress < 0:
            show_popup("Episode progress must be greater than or equal to 0")
            return
        elif season_progress > season:
            show_popup("Season progress must be less than or equal to season")
            return
        elif episode_progress > episode:
            show_popup("Episode progress must be less than or equal to episode")
            return
        elif episode_progress == 0 and episode != 0:
            show_popup("Episode shouldn't be 0 for an Ongoing Season")
            return
        elif episode_progress != 0 and season_progress == 0:
            show_popup("Season progress shouldn't be 0 for an Ongoing Watch")
            return
        elif episode_progress == 0 and season_progress == 0 and watch_progress != 0:
            show_popup("Watch progress should be 0 for an Unwatched Series")
            return
        elif rating is not None and (rating < 0 or rating > 10):
            show_popup("Rating must be between 0 and 10")
            return
        elif is_overlap():
            show_popup("Watch progress must be less than or equal to duration")
            return

        try:
            conn = sqlite3.connect('database/database.db')
            cursor = conn.cursor()

            # Handle file upload
            if self.file_picker.result and self.file_picker.result.files:
                for f in self.file_picker.result.files:
                    shutil.copy(f.path, os.path.join('../assets/img/', f'{series.getId()}s.jpg'))

            # Update series name
            series.setName(self.name_table.value)
            series_dict[series.getId()][1] = series.getName()
            cursor.execute("UPDATE series SET name = ? WHERE series_id = ?", (series.getName(), series.getId()))

            # Update series season
            series.setSeason(season)
            series_dict[series.getId()][5] = series.getSeason()
            cursor.execute("UPDATE series SET season = ? WHERE series_id = ?", (series.getSeason(), series.getId()))

            # Update season progress
            if series.getSeasonProgress() == 0 and (season_progress != 0 or episode_progress != 0):
                series.setSeasonProgress(season_progress)
                if series.getId() in watchlist_series_dict:
                    watchlist_series_dict.pop(series.getId())
                    cursor.execute("DELETE FROM watchlist_series WHERE series_id = ?", (series.getId(),))
                ongoing_series_dict[series.getId()] = [series.getId(), season_progress]
                cursor.execute("INSERT INTO ongoing_series (series_id, season_progress) VALUES (?, ?)", (series.getId(), season_progress))
            elif series.getSeasonProgress() != 0 and season_progress == 0:
                series.setSeasonProgress(0)
                if series.getId() in ongoing_series_dict:
                    ongoing_series_dict.pop(series.getId())
                    cursor.execute("DELETE FROM ongoing_series WHERE series_id = ?", (series.getId(),))
                watchlist_series_dict[series.getId()] = [series.getId()]
                cursor.execute("INSERT INTO watchlist_series (series_id) VALUES (?)", (series.getId(),))
            else:
                series.setSeasonProgress(season_progress)
                ongoing_series_dict[series.getId()][1] = series.getSeasonProgress()
                cursor.execute("UPDATE ongoing_series SET season_progress = ? WHERE series_id = ?", (series.getSeasonProgress(), series.getId()))

            # Update series episode
            series.setEpisode(episode)
            series_dict[series.getId()][6] = series.getEpisode()
            cursor.execute("UPDATE series SET episode = ? WHERE series_id = ?", (series.getEpisode(), series.getId()))

            # Update episode progress
            if series.getEpisodeProgress() == 0 and (episode_progress != 0 or season_progress != 0):
                series.setEpisodeProgress(episode_progress)
                if series.getId() in watchlist_series_dict:
                    watchlist_series_dict.pop(series.getId())
                    cursor.execute("DELETE FROM watchlist_series WHERE series_id = ?", (series.getId(),))
                ongoing_series_dict[series.getId()] = [series.getId(), season_progress, episode_progress]
                cursor.execute("INSERT INTO ongoing_series (series_id, season_progress, episode_progress) VALUES (?, ?, ?)", (series.getId(), season_progress, episode_progress))
            elif series.getEpisodeProgress() != 0 and (episode_progress == 0 or season_progress == 0):
                series.setEpisodeProgress(0)
                if series.getId() in ongoing_series_dict:
                    ongoing_series_dict.pop(series.getId())
                    cursor.execute("DELETE FROM ongoing_series WHERE series_id = ?", (series.getId(),))
                watchlist_series_dict[series.getId()] = [series.getId()]
                cursor.execute("INSERT INTO watchlist_series (series_id) VALUES (?)", (series.getId(),))
            else:
                series.setEpisodeProgress(episode_progress)
                ongoing_series_dict[series.getId()][2] = series.getEpisodeProgress()
                cursor.execute("UPDATE ongoing_series SET episode_progress = ? WHERE series_id = ?", (series.getEpisodeProgress(), series.getId()))

            # Update series duration
            duration = self.hours_to_seconds(self.jam_duration.value, self.menit_duration.value, self.detik_duration.value)
            series.setDuration(duration)
            series_dict[series.getId()][2] = series.getDuration()
            cursor.execute("UPDATE series SET duration = ? WHERE series_id = ?", (series.getDuration(), series.getId()))

            # Update watch progress
            watch_progress = self.hours_to_seconds(self.jam_watch_progress.value, self.menit_watch_progress.value, self.detik_watch_progress.value)
            series.setWatchProgress(watch_progress)
            ongoing_series_dict[series.getId()][3] = series.getWatchProgress()
            cursor.execute("UPDATE ongoing_series SET watched_duration = ? WHERE series_id = ?", (series.getWatchProgress(), series.getId()))

            if watch_progress == duration and episode_progress == episode and season_progress == season:
                finished_series_dict[series.getId()] = [series.getId()]
                if series.getId() in watchlist_series_dict:
                    watchlist_series_dict.pop(series.getId())
                    cursor.execute("DELETE FROM watchlist_series WHERE series_id = ?", (series.getId(),))
                if series.getId() in ongoing_series_dict:
                    ongoing_series_dict.pop(series.getId())
                    cursor.execute("DELETE FROM ongoing_series WHERE series_id = ?", (series.getId(),))
                cursor.execute("INSERT INTO finished_series (series_id) VALUES (?)", (series.getId(),))

            # Update release year
            if self.date_picker.value:
                series.setReleaseYear(self.date_picker.value.year)
                series_dict[series.getId()][3] = series.getReleaseYear()
                cursor.execute("UPDATE series SET release_year = ? WHERE series_id = ?", (series.getReleaseYear(), series.getId()))

            # Update genre
            series.setGenre(self.genre.value)
            series_dict[series.getId()][4] = series.getGenre()
            cursor.execute("UPDATE series SET genre = ? WHERE series_id = ?", (series.getGenre(), series.getId()))

            # Update rating
            if rating is not None:
                series.setRating(rating)
                if series.getId() in review_series_dict:
                    review_series_dict[series.getId()][1] = series.getRating()
                    cursor.execute("UPDATE review_series SET rating = ? WHERE series_id = ?", (series.getRating(), series.getId()))
                else:
                    review_series_dict[series.getId()] = [series.getId(), series.getRating()]
                    cursor.execute("INSERT INTO review_series (series_id, rating, review) VALUES (?, ?, 'This is a review')")
            elif series.getId() in review_series_dict:
                series.setRating(None)
                review_series_dict.pop(series.getId())
                cursor.execute("DELETE FROM review_series WHERE series_id = ?", (series.getId(),))

            series.setSummary(self.summary.value)
            series_dict[series.getId()][5] = series.getSummary()
            cursor.execute("UPDATE series SET synopsis = ? WHERE series_id = ?", (series.getSummary(), series.getId()))

            conn.commit()
        except Exception as error:
            print(f"Error occurred: {error}")
        finally:
            conn.close()

        print("Name: ", series.getName())
        print("Season: ", series.getSeason())
        print("Season Progress: ", series.getSeasonProgress())
        print("Episode: ", series.getEpisode())
        print("Episode Progress: ", series.getEpisodeProgress())
        print("Duration: ", series.getDuration())
        print("Watch Progress: ", series.getWatchProgress())
        print("Release Year: ", series.getReleaseYear())
        print("Genre: ", series.getGenre())
        print("Rating: ", series.getRating())
        print("Summary: ", series.getSummary())


        def navigate_to_information(e):
            page.go("/informasi-film-series")
            page.update()

        popup = PopUp("Success!", "Your series has successfully updated", navigate_to_information)
        popup.open_dlg_modal(e, page)

    def show_page(self, page: ft.Page):
        page.overlay.append(self.date_picker)
        page.overlay.append(self.file_picker)
        page.bgcolor = "#000D20"
        page.add(
            [

            ]
        )