import flet as ft
from content import Content, Movie, Series

import flet as ft

class FilmInformation(ft.Container):
    def __init__(self, movie : Movie, page: ft.Page, kolomHalaman: ft.Column):
        super().__init__()
        self.width = page.window_width
        self.height = page.window_height
        
        name = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Text(movie.getName(), weight=ft.FontWeight.BOLD, size=25, color="#CBA133"))
        summary = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Text(movie.getSummary(), weight=ft.FontWeight.W_700, size=15, color="#FED466",)
        )
        genre = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Row(
                [
                    ft.Text("Genre : ", color="#FED466", weight=ft.FontWeight.W_700, size=15),
                    ft.Text(movie.getGenre(), color="#FED466", weight=ft.FontWeight.W_700, size=15)
                ]
            )
        )
        releaseYear = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Row(
                [
                    ft.Text("Release Year : ", color="#FED466", weight=ft.FontWeight.W_700, size=15),
                    ft.Text(movie.getReleaseYear(), color="#FED466", weight=ft.FontWeight.W_700, size=15)
                ]
            )
        )
        rating = ft.Container(
            padding=ft.padding.only(left = 20),
            content =
            ft.Text(f"Rating : {movie.getRating()}/10", color="#FED466", weight=ft.FontWeight.W_700, size=15)
        )
        duration = ft.Container(
            padding = ft.padding.only(left = 20),

            content = ft.Text(f"Duration : {movie.getDuration()// 3600} hours {(movie.getDuration() % 3600) // 60} minutes {movie.getDuration() % 60} seconds", color="#FED466", weight=ft.FontWeight.W_700, size=15)
        )
        watchProgress = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Text(f"Watch Progress : {movie.getWatchProgress()// 3600} hours {(movie.getWatchProgress() % 3600) // 60} minutes {movie.getWatchProgress() % 60} seconds", color="#FED466", weight=ft.FontWeight.W_700, size=15)
        )
        gambar = ft.Container(ft.Image(movie.getGambar(), width=300, height=450, border_radius=30))
        
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
                ft.ElevatedButton("Edit Information",  bgcolor='#DAAB2D',on_click = lambda _: self.handleEditMovie(movie,page,kolomHalaman), color='#000000')
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
                ft.ElevatedButton("Delete Film", bgcolor=ft.colors.RED, on_click=self.deleteMovie(movie, page),color = '#ffffff')
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
    
    def handleEditMovie(self, movie:Movie, page: ft.Page, kolomHalaman: ft.Column):
        #TODO: Implementasi injeksi objek Edit Movie pada halaman edit film series (pakai variabel kolomHalaman dan jangan lupa clear isi kolomHalaman sebelum melakukan append)
        kolomHalaman.controls.clear()
        kolomHalaman.controls.append(
            #TODO: append Objek Edit Movie
            ft.Text("Edit Movie")
        )
        page.go("/edit-film-series")

    def deleteMovie(self, movie : Movie, page: ft.Page):
        #TODO: Implementasi penghapusan film dari database
        page.go("/")

class SeriesInformation(ft.Container):
    def __init__(self, series : Series, page: ft.Page, kolomHalaman: ft.Column):
        super().__init__()
        self.width = page.window_width
        self.height = page.window_height
        
        name = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Text(series.getName(), weight=ft.FontWeight.BOLD, size=25, color="#CBA133"))
        summary = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Text(series.getSummary(), weight=ft.FontWeight.W_700, size=15, color="#FED466",)
        )
        genre = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Row(
                [
                    ft.Text("Genre : ", color="#FED466", weight=ft.FontWeight.W_700, size=15),
                    ft.Text(series.getGenre(), color="#FED466", weight=ft.FontWeight.W_700, size=15)
                ]
            )
        )
        releaseYear = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Row(
                [
                    ft.Text("Release Year : ", color="#FED466", weight=ft.FontWeight.W_700, size=15),
                    ft.Text(series.getReleaseYear(), color="#FED466", weight=ft.FontWeight.W_700, size=15)
                ]
            )
        )
        rating = ft.Container(
            padding=ft.padding.only(left = 20),
            content =
            ft.Text(f"Rating : {series.getRating()}/10", color="#FED466", weight=ft.FontWeight.W_700, size=15)
        )
        duration = int(series.getDuration() or 1)
        duration = ft.Container(
            padding = ft.padding.only(left = 20),

            content = ft.Text(f"Duration : {duration// 3600} hours {(duration % 3600) // 60} minutes {duration % 60} seconds", color="#FED466", weight=ft.FontWeight.W_700, size=15)
        )
        watch_progress = int(series.getWatchProgress() or 0)
        watchProgress = ft.Container(
            padding=ft.padding.only(left = 20),
            content = ft.Text(f"Watch Progress : {watch_progress// 3600} hours {(watch_progress % 3600) // 60} minutes {watch_progress % 60} seconds", color="#FED466", weight=ft.FontWeight.W_700, size=15)
        )
        gambar = ft.Container(ft.Image(series.getGambar(), width=300, height=450, border_radius=30))
        
        header = ft.Container(
            content=ft.Row([
                ft.IconButton(ft.icons.ARROW_BACK, icon_color="#FED466", on_click=self.go_back),
                ft.Text("Series Information", size=30, weight=ft.FontWeight.W_800),
                ft.Text("")
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        )
        
        edit = ft.Container(
            padding=ft.padding.only(right=25),
            content=ft.Row([
                ft.ElevatedButton("Edit Information",  bgcolor='#DAAB2D', color='#000000', on_click = self.handleEditSeries(series,page,kolomHalaman))
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
                ft.ElevatedButton("Delete Film", bgcolor=ft.colors.RED, color = '#ffffff', on_click = lambda _: self.deleteSeries(series))
            ], alignment=ft.MainAxisAlignment.END)
        )
        
        self.content = ft.Column([
            header,
            content_container,
            delete
        ])
        self.page = page
    

    def handleEditSeries(self, series:Series, page: ft.Page, kolomHalaman: ft.Column):
        #TODO: Implementasi injeksi objek Series Movie pada halaman edit film series (pakai variabel kolomHalaman dan jangan lupa clear isi kolomHalaman sebelum melakukan append)
        kolomHalaman.controls.clear()
        kolomHalaman.controls.append(
            #TODO: append Objek Edit Series
            ft.Text("Edit Series")
        )
        page.go("/edit-film-series")

    def deleteSeries(self, movie : Movie):
        #TODO: Implementasi penghapusan series dari database
        self.page.go("/")

    def go_back(self, e):
        self.page.go("/")