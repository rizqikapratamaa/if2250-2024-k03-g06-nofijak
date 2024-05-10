import datetime
import flet as ft
from content import *
from content import Content
from edit_button import MyButton

class EditPage:
    def __init__(self, content: Content):
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
            width=300, 
            fill_color=ft.colors.WHITE, 
            color=ft.colors.BLACK, 
            border_radius=50, 
            border_color="#000D20", 
            focused_border_color="#FED466", 
            selection_color="#FED466", 
            label_style= ft.TextStyle(color="#FED466", font_family="Consolas"))
        
        self.release_date_text = ft.Container(
            ft.Text("Release Date"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )

        self.date_picker = ft.DatePicker(
            on_change=self.change_date,
            on_dismiss=self.date_picker_dismissed,
            first_date=datetime.datetime(1990, 10, 1),
            last_date=datetime.datetime(2030, 10, 1),
        )

        self.release_date_table = ft.ElevatedButton(
            content.getReleaseDate(),
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.date_picker.pick_date(),
        )

        self.duration_text = ft.Container(
            ft.Text("Duration"),
            padding=ft.padding.only(left=10, right=295, top=10)
        )

        self.watch_progress_text = ft.Container(
            ft.Text("Watch Progress"),
            padding=ft.padding.only(left=10, top=10)
        )

        self.duration_table = ft.Container(
            ft.Row([
                ft.Dropdown(label="Jam", border_radius=50, value=content.getDuration() // 3600, width=100, options = [ft.dropdown.Option(str(i)) for i in range(60)], bgcolor=ft.colors.WHITE, color=ft.colors.BLACK),
                ft.Dropdown(label="Menit", border_radius=50, value=(content.getDuration() % 3600) // 60, width=100, options= [ft.dropdown.Option(str(i)) for i in range(60)], bgcolor=ft.colors.WHITE, color=ft.colors.BLACK),
                ft.Dropdown(label="Detik", border_radius=50, value=content.getDuration() % 60, width=100, options= [ft.dropdown.Option(str(i)) for i in range(60)], bgcolor=ft.colors.WHITE, color=ft.colors.BLACK)
            ])
        )

        self.watch_progress_table = ft.Container(
            ft.Row([
                ft.Dropdown(label="Jam", border_radius=50, value=content.getWatchProgress() // 3600, width=100, options = [ft.dropdown.Option(str(i)) for i in range(60)], bgcolor=ft.colors.WHITE, color=ft.colors.BLACK),
                ft.Dropdown(label="Menit", border_radius=50, value=(content.getWatchProgress() % 3600) // 60, width=100, options = [ft.dropdown.Option(str(i)) for i in range(60)], bgcolor=ft.colors.WHITE, color=ft.colors.BLACK),
                ft.Dropdown(label="Detik", border_radius=50, value=content.getWatchProgress() % 60, width=100, options = [ft.dropdown.Option(str(i)) for i in range(60)], bgcolor=ft.colors.WHITE, color=ft.colors.BLACK)
            ])
        )

        self.rating = ft.TextField(
            value = str(content.getRating()), 
            text_align=ft.TextAlign.CENTER, 
            width=80,
            border_radius=50,
            border_color="#000D20",
            focused_border_color="#FED466",
            selection_color="#FED466",
            fill_color=ft.colors.WHITE,
            color=ft.colors.BLACK
        )

        self.rating_text =ft.Container(
            ft.Text("Rating"),
            padding=ft.padding.only(left=50, right=10, top = 10)
        ) 

        self.genre_text = ft.Container(
            ft.Text("Genre"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )

        self.genre = ft.Container(
            ft.TextField(value=str(content.getGenre()), text_align=ft.TextAlign.LEFT, width=120, fill_color=ft.colors.WHITE, color=ft.colors.BLACK, border_radius=50, border_color="#000D20", focused_border_color="#FED466", selection_color="#FED466", label_style= ft.TextStyle(color="#FED466", font_family="Consolas")),
            padding=ft.padding.only(right=20)
        )

        self.summary_text = ft.Container(
            ft.Text("Summary"),
            padding=ft.padding.only(left=10, right=10, top=10)
        )

        self.summary = ft.Container(
            ft.TextField(
                value=content.getSummary(),
                text_align=ft.TextAlign.LEFT,
                width=500, shift_enter=True,
                fill_color=ft.colors.WHITE,
                color=ft.colors.BLACK,
                border_radius=50,
                border_color="#000D20",
                focused_border_color="#FED466",
                selection_color="#FED466",
                label_style= ft.TextStyle(color="#FED466", font_family="Consolas")
            ),
            padding=ft.padding.only(right=10)
        )

        self.poster = ft.Container(
            ft.Image(content.getGambar(), width=300, height=450, border_radius=30),
            padding=ft.padding.only(left=215)
        )
        self.submit_button = ft.Container(
            ft.Row([
                MyButton("Submit", on_click=lambda e: self.submit_click(e, content))
            ]),
            padding=ft.padding.only(top=20, left= 950)
        )

    def submit_click(self, e,  content: Content):
        content.setName(self.name_table.value)
        content.setReleaseDate(self.date_picker.value)
        
    
    def change_date(self, e):
            print(f"Date picker changed, value is {self.date_picker.value}")

    def date_picker_dismissed(self, e):
        print(f"Date picker dismissed, value is {self.date_picker.value}")

    def convert_seconds(self, seconds):
        hours = seconds // 3600
        remaining_seconds = seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return hours, minutes, seconds
        
    def convert_hours(self, hour, minutes, seconds):
        return (hour * 3600) + (minutes * 60) + seconds

    def show_page(self, page: ft.Page):
        page.overlay.append(self.date_picker)
        page.add(
        ft.IconButton(ft.icons.ARROW_BACK, icon_color="#FED466", on_click=lambda e: page.clean()),
        ft.Container(
            content= 
            ft.Row([
                ft.Column([
                    self.edit_text,
                    self.name_text,
                    self.name_table,
                    self.release_date_text,
                    self.release_date_table,
                    ft.Row([
                        self.duration_text,
                        self.watch_progress_text
                    ])
                    ,
                    ft.Row([
                        self.duration_table,
                        self.watch_progress_table,
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
                    self.summary,
                    self.submit_button
                ]),
                self.poster
            ]),
            padding=ft.padding.only(left=50,right=50)
        ),
        )
        
class MovieEditPage(EditPage):
    def __init__(self, movie: Movie):
        super().__init__(movie)

class SeriesEditPage(EditPage):
    def __init__(self, series: Series):
        super().__init__(series)

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
            label_style= ft.TextStyle(color="#FED466", font_family="Consolas")
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
            label_style= ft.TextStyle(color="#FED466", font_family="Consolas")
        )
    def show_page(self, page: ft.Page):
        page.overlay.append(self.date_picker)
        page.add(
        ft.IconButton(ft.icons.ARROW_BACK, icon_color="#FED466", on_click=lambda e: page.clean()),
        ft.Container(
            content= 
            ft.Row([
                ft.Column([
                    self.edit_text,
                    self.name_text,
                    self.name_table,
                    self.release_date_text,
                    self.release_date_table,
                    ft.Row([
                        self.duration_text,
                        self.watch_progress_text
                    ])
                    ,
                    ft.Row([
                        self.duration_table,
                        self.watch_progress_table,
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
                    self.summary,
                    self.submit_button
                ]),
                self.poster
            ]),
            padding=ft.padding.only(left=50,right=50)
        ),
        )

