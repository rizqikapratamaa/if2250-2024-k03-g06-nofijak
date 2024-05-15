import flet as ft
from content import Content, Movie, Series

import flet as ft

class FilmInformation(ft.Container):
    def __init__(self, content: Content, page: ft.Page):
        super().__init__()
        self.width = page.window_width
        self.height = page.window_height
        
        name = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Text(content.getName(), weight=ft.FontWeight.BOLD, size=25, color="#CBA133"))
        summary = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Text(content.getSummary(), weight=ft.FontWeight.W_700, size=15, color="#FED466",)
        )
        genre = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Row(
                [
                    ft.Text("Genre : ", color="#FED466", weight=ft.FontWeight.W_700, size=15),
                    ft.Text(content.getGenre(), color="#FED466", weight=ft.FontWeight.W_700, size=15)
                ]
            )
        )
        releaseYear = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Row(
                [
                    ft.Text("Release Year : ", color="#FED466", weight=ft.FontWeight.W_700, size=15),
                    ft.Text(content.getReleaseYear(), color="#FED466", weight=ft.FontWeight.W_700, size=15)
                ]
            )
        )
        rating = ft.Container(
            padding=ft.padding.only(left = 20),
            content =
            ft.Text(f"Rating : {content.getRating()}/10", color="#FED466", weight=ft.FontWeight.W_700, size=15)
        )
        duration = ft.Container(
            padding = ft.padding.only(left = 20),

            content = ft.Text(f"Duration : {content.getDuration()// 3600} hours {(content.getDuration() % 3600) // 60} minutes {content.getDuration() % 60} seconds", color="#FED466", weight=ft.FontWeight.W_700, size=15)
        )
        watchProgress = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Text(f"Watch Progress : {content.getWatchProgress()// 3600} hours {(content.getWatchProgress() % 3600) // 60} minutes {content.getWatchProgress() % 60} seconds", color="#FED466", weight=ft.FontWeight.W_700, size=15)
        )
        gambar = ft.Container(ft.Image(content.getGambar(), width=300, height=450, border_radius=30))
        
        header = ft.Container(
            content=ft.Row([
                ft.IconButton(ft.icons.ARROW_BACK, icon_color="#FED466", on_click=self.go_back),
                ft.Text("Film Information", size=30, weight=ft.FontWeight.W_800),
                ft.Text("")
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        )
        
        edit = ft.Container(
            padding=ft.padding.only(right=25),
            content=ft.Row([
                ft.ElevatedButton("Edit Information",  bgcolor='#DAAB2D', color='#000000')
            ], alignment=ft.MainAxisAlignment.END)
        )

        data = ft.Container(
            content=ft.Column([
                name,
                summary,
                genre,
                releaseYear,
                rating,
                duration,
                watchProgress,
                edit
            ], 
            alignment=ft.MainAxisAlignment.SPACE_AROUND),
            bgcolor="#092143",
            margin=ft.margin.only(left=20),
            height=450,
            width=page.window_width - 500,
            border_radius=30
        )
        
        content_container = ft.Container(
            content=ft.Row([
                gambar,
                data
            ])
        )
        
        delete = ft.Container(
            padding=ft.padding.only(right=50),
            content=ft.Row([
                ft.ElevatedButton("Delete Film", bgcolor=ft.colors.RED, color = '#ffffff')
            ], alignment=ft.MainAxisAlignment.END)
        )
        
        self.content = ft.Column([
            header,
            content_container,
            delete
        ])
        self.page = page

    def go_back(self, e):
        self.page.go("/")

# series = Movie("1", "The Falcon and The Winter Soldier", 50, "Sam Wilson and Bucky Barnes realize that their futures are anything but normal.", ["Action", "Adventure", "Drama"], 8.0, "2021-04-23", "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg")

# def main(Page: ft.Page):
#     Page.window_height = 720
#     Page.window_width = 1280
    
#     film = FilmInformation(series, Page)
    
#     film.show_page(Page)
#     ...
    
# ft.app(target=main)