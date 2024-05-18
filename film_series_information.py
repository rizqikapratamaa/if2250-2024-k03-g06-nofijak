import flet as ft
from content import Content, Movie, Series
from popup import *
from database import Database
from edit_page import MovieEditPage, SeriesEditPage
import sqlite3

import flet as ft

class FilmInformation(ft.Container):
    def __init__(self, movie : Movie, page: ft.Page, informasiEdit : ft.Column, database: Movie):
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
                ft.IconButton(ft.icons.ARROW_BACK, icon_color="#FED466", on_click= lambda _: self.go_back(page)),
                ft.Text("Film Information", size=30, weight=ft.FontWeight.W_800),
                ft.Text("")
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        )
        
        edit = ft.Container(
            padding=ft.padding.only(right=25),
            content=ft.Row([
                ft.ElevatedButton("Edit Information",  bgcolor='#DAAB2D',on_click = lambda _: self.handleEditMovie(movie,page,informasiEdit, database), color='#000000')
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
                ft.ElevatedButton("Delete Film", bgcolor=ft.colors.RED, on_click= lambda e: self.deleteMovie(e, movie, page, database),color = '#ffffff')
            ], alignment=ft.MainAxisAlignment.END)
        )
        
        self.content = ft.Column([
            header,
            content_container,
            delete
        ])

    def go_back(self, page: ft.Page):
        page.go("/")
    
    def handleEditMovie(self, movie:Movie, page: ft.Page, kolomHalaman: ft.Column, database: Database):
        #TODO: Implementasi injeksi objek Edit Movie pada halaman edit film series (pakai variabel kolomHalaman dan jangan lupa clear isi kolomHalaman sebelum melakukan append)
        kolomHalaman.controls.clear()
        kolomHalaman.controls.append(
            #TODO: append Objek Edit Movie
            MovieEditPage(movie, page, database.getMovies(),database.getOngoingMovies(), database.getReviewMovies(), database.getWatchlistMovies())
        )
        page.go("/edit-film-series")

    def deleteMovie(e, self, movie: Movie, page: ft.Page, database: Database):
        def on_yes(e):
            database.removeMovie(movie.getId())
            database.removeWatchlistMovie(movie.getId())
            database.removeFinishedMovie(movie.getId())
            database.removeOngoingMovie(movie.getId())
            database.removeReviewMovie(movie.getId())
            success_popup = PopUp("Success!", "Movie has been deleted", page)
            success_popup.open_dlg_modal(e, page)

            success_popup.dlg_modal.on_dismiss = lambda e: page.go("/")
            
        
        def on_no(e):
            pass

        proceed_popup = YesOrNo("You may lose this movie permanently. Do you want to proceed?", page)
        
        proceed_popup.open_dlg_modal_yes_no(e, on_yes, on_no)

class SeriesInformation(ft.Container):
    def __init__(self, series : Series, page: ft.Page, kolomHalaman: ft.Column, database: Database):
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
                ft.IconButton(ft.icons.ARROW_BACK, icon_color="#FED466", on_click= lambda _: self.go_back(page)),
                ft.Text("Series Information", size=30, weight=ft.FontWeight.W_800),
                ft.Text("")
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        )
        
        edit = ft.Container(
            padding=ft.padding.only(right=25),
            content=ft.Row([
                ft.ElevatedButton("Edit Information",  bgcolor='#DAAB2D', color='#000000', on_click = lambda _: self.handleEditSeries(series,page,kolomHalaman,database))
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
                ft.ElevatedButton("Delete Film", bgcolor=ft.colors.RED, color = '#ffffff', on_click = lambda _: self.deleteSeries(series, database))
            ], alignment=ft.MainAxisAlignment.END)
        )
        
        self.content = ft.Column([
            header,
            content_container,
            delete
        ])
        self.page = page
    

    def handleEditSeries(self, series:Series, page: ft.Page, kolomHalaman: ft.Column, database: Database):
        #TODO: Implementasi injeksi objek Series Movie pada halaman edit film series (pakai variabel kolomHalaman dan jangan lupa clear isi kolomHalaman sebelum melakukan append)
        kolomHalaman.controls.clear()
        kolomHalaman.controls.append(
            #TODO: append Objek Edit Series
            SeriesEditPage(series, page, database.getSeries(),database.getOngoingSeries(), database.getReviewSeries(), database.getWatchlistSeries())
        )
        page.go("/edit-film-series")

    def deleteSeries(e, self, series : Series, page: ft.Page, database: Database):
        def on_yes(e):
            database.removeSeries(series.getId())
            database.removeWatchlistSeries(series.getId())
            database.removeFinishedSeries(series.getId())
            database.removeOngoingSeries(series.getId())
            database.removeReviewSeries(series.getId())
            success_popup = PopUp("Success!", "Series has been deleted", page)
            success_popup.open_dlg_modal(e, page)
            success_popup.dlg_modal.on_dismiss = lambda e: page.go("/")
        
        def on_no(e):
            pass

        proceed_popup = YesOrNo("You may lose this series permanently. Do you want to proceed?", page)
        
        proceed_popup.open_dlg_modal_yes_no(e, on_yes, on_no)

    def go_back(self, page):
        page.go("/")
