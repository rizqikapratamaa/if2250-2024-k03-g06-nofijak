import flet as ft
from content import *
from edit_button import *

series = Movie("1", "The Falcon and The Winter Soldier", 1000, 5000, "Sam Wilson and Bucky Barnes realize that their futures are anything but normal.", ["Action", "Adventure", "Drama"], 8.0, 1000, "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg")

def convert_seconds(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return hours, minutes, seconds
    
def convert_hours(hour, minutes, seconds):
    return (hour * 3600) + (minutes * 60) + seconds

def main(page: ft.Page):
    
    page.title = "Nofijak"
    page.bgcolor = "#000D20"

    page.vertical_alignment = ft.MainAxisAlignment.START

    hours_duration, minutes_duration, seconds_duration = convert_seconds(series.getDuration())
    hours_lastplay, minutes_lastplay, seconds_lastplay = convert_seconds(series.getLastPlay())


    hour_dropdown_duration = ft.Dropdown(label="Jam", border_radius=70, value=hours_duration, width=100, options = [ft.dropdown.Option(str(i)) for i in range(60)], bgcolor=ft.colors.WHITE, color=ft.colors.BLACK)
    minute_dropdown_duration = ft.Dropdown(label="Menit", border_radius=70, value=minutes_duration, width=100, options= [ft.dropdown.Option(str(i)) for i in range(60)], bgcolor=ft.colors.WHITE, color=ft.colors.BLACK)
    second_dropdown_duration = ft.Dropdown(label="Menit", border_radius=70, value=seconds_duration, width=100, options= [ft.dropdown.Option(str(i)) for i in range(60)], bgcolor=ft.colors.WHITE, color=ft.colors.BLACK)
    
    hour_dropdown_lastplay = ft.Dropdown(label="Jam", border_radius=70, value=hours_lastplay, width=100, options = [ft.dropdown.Option(str(i)) for i in range(60)])
    minute_dropdown_lastplay = ft.Dropdown(label="Menit", border_radius=70, value=minutes_lastplay, width=100, options = [ft.dropdown.Option(str(i)) for i in range(60)])
    second_dropdown_lastplay = ft.Dropdown(label="Detik", value=seconds_lastplay, width=100, options = [ft.dropdown.Option(str(i)) for i in range(60)])

    rating = ft.TextField(value = str(series.getRating()), text_align=ft.TextAlign.RIGHT, width=100)

    edit_text = ft.Container(
        ft.Text("Edit Information", size=20)
    )

    name = ft.Container(
        ft.Text("Name"),
        padding=ft.padding.only(left=10,right=350)
    )
    name_table = ft.TextField(value=series.getName(), text_align=ft.TextAlign.LEFT, width=300, fill_color=ft.colors.WHITE, color=ft.colors.BLACK, border_radius=70, border_color="#000D20", focused_border_color="#FED466", selection_color="#FED466", label_style= ft.TextStyle(color="#FED466", font_family="Consolas"))

    duration = ft.Container(
        ft.Text("Duration"),
        padding=ft.padding.only(left=10, right=295)
    )

    watch_progress = ft.Container(
        ft.Text("Watch Progress"),
        padding=ft.padding.only(left=10)
    )

    duration_table = ft.Container(
        ft.Row([
            hour_dropdown_duration,
            minute_dropdown_duration,
            second_dropdown_duration       
        ]),
        padding=ft.padding.only(right=20)
    )

    lastplay_table = ft.Container(
        ft.Row([
            hour_dropdown_lastplay,
            minute_dropdown_lastplay,
            second_dropdown_lastplay
        ]),
        padding=ft.padding.only(left=20)
    )

    release_date = ft.Container(

    )

        
    rating_number = ft.TextField(value = str(series.getRating()), text_align=ft.TextAlign.RIGHT, width=100)
    
    

    # genre = ', '.join(series.getGenre())


    def submit_click(e):
        series.setRating(float(rating_number.value))
        series.setName(name_table.value)

        # Duration
        hours = int(hour_dropdown_duration.value)
        minutes = int(minute_dropdown_duration.value)
        seconds = int(second_dropdown_duration.value)

        new_duration = convert_hours(hours, minutes, seconds)
        series.setDuration(new_duration)
        
        page.clean()
        page.add(ft.Text(f"Hello, {new_duration}!"))
    
    submit_button = ft.Container(
        ft.Row([
            MyButton("Submit", on_click=submit_click)
        ]),
        padding=ft.padding.only(top=20, left= 1000)
    )

    page.add(
        ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda e: page.clean()),
        ft.Container(
            content= 
            ft.Column([
                edit_text,
                name,
                name_table,
                ft.Row([
                    duration,
                    watch_progress
                ]),
                ft.Row([
                    duration_table,
                    lastplay_table,
                ]),

                ft.Row([
                    rating
                ]),
                submit_button
            ]),
            padding=ft.padding.only(left=50,right=50)
        )
    )

ft.app(target=main)