import flet as ft
from content import Content, Movie, Series

class FilmInformation:
    def __init__(self, content: Content, page: ft.Page):
        self.name = ft.Container(
            ft.Text(content.getName())
        )
        
        self.summary = ft.Container(
            ft.Text(content.getSummary())
        )
        
        self.genre = ft.Container(
            ft.Text(content.getGenre())
        )
        
        # self.releaseDate = ft.Container(
        #     ft.Text(content.getReleaseDate())
        # )
        
        self.rating = ft.Container(
            ft.Text(content.getRating())
        )
        
        self.duration = ft.Container(
            ft.Text(content.getDuration())
        )
        
        self.lastPlay = ft.Container(
            ft.Text(content.getLastPlay())
        )
        
        self.gambar = ft.Container(
            ft.Image(content.getGambar(), width=300, height=450, border_radius=30),
        )
        
        self.header = ft.Container(
            content = ft.Row([
                ft.IconButton(ft.icons.ARROW_BACK, icon_color="#FED466"),
                ft.Text("Film Information", size=20),
                ft.Text("")
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        )
        
        self.data = ft.Container(
            content=ft.Column([
                self.name,
                self.summary,
                self.genre,
                self.rating,
                self.duration,
                self.lastPlay,
                ft.ElevatedButton("Edit Information")
            ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
            bgcolor="#092143",
            margin=ft.margin.only(left=20),
            height=450,
            width= page.window_width - 500
        )
        
        self.content = ft.Container(
            content = ft.Row([
                self.gambar,
                self.data
            ])
        )
        
        self.delete = ft.Container(
            content=ft.Row([
                ft.ElevatedButton("Delete Film")
            ], alignment=ft.MainAxisAlignment.END)
        )
    
    def show_page(self, page: ft.Page):
        page.add(ft.Container(
            content=ft.Column([
                self.header,
                self.content,
                self.delete
                ]),
            width = page.window_width,
            height = page.window_height,
            bgcolor="#000D20"
        ))
        
series = Movie("1", "The Falcon and The Winter Soldier", 50, "Sam Wilson and Bucky Barnes realize that their futures are anything but normal.", ["Action", "Adventure", "Drama"], 8.0, "2021-04-23", "https://www.themoviedb.org/t/p/original/6kbAMLteGO8yyewYau6bJ683sw7.jpg")

def main(Page: ft.Page):
    Page.window_height = 720
    Page.window_width = 1280
    
    film = FilmInformation(series, Page)
    
    film.show_page(Page)
    ...
    
ft.app(target=main)