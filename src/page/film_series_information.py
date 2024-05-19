import flet as ft
from utils.content import Movie, Series
from utils.popup import *
from database.database import Database
from page.edit_page import MovieEditPage, SeriesEditPage
import os

import flet as ft

database = Database()

class ScrollableCard(ft.Column):
    def __init__(self):
        # Inisialisasi base class dari ft.ColumnF
        super().__init__()
        # Properti untuk scrollable card
        self.height = 250
        self.width = 1000
        self.scroll = ft.ScrollMode.ALWAYS
    
    # Method untuk menambahkan film pada halaman entries
    def tambahCardMovie(self, movie, page, Informasi, informasiEdit):
        self.controls.append(
            EntryCardMovie(movie, page, Informasi, informasiEdit, scrollCard=self)
        )
    
    def tambahCardSeries(self, series, page, Informasi, InformasiEdit):
        self.controls.append(
            EntryCardSeries(series, page, Informasi, InformasiEdit, scrollCard=self)
        )

    def inisialisasiCard(self):
        self.controls.clear()

class EntryCardMovie(ft.ElevatedButton):
    # Constructor entry card dengan parameter
    def __init__(self, movie : Movie, page, informasi, informasiEdit, scrollCard : ScrollableCard):
        super().__init__()
        self.width = 1000
        self.bgcolor = "#092143"
        self.on_click = lambda _: self.informasiFilm(movie, page, informasi, informasiEdit, database, scrollCard)
        self.style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            )
        self.content = ft.Row([
            ft.Container(
                padding=ft.padding.only(top=10, bottom=10, left=-15),
                content=ft.Image(src=movie.getGambar(), width=115, height=115, fit=ft.ImageFit.COVER),
            ),
            ft.Column([
                ft.Text(movie.getName(), size=20, color="#DAAB2D"),
                ft.Text(movie.getGenre(), size=15),
            ]),
            ft.Column([
                ft.Text("Progress", size=20, color="#DAAB2D"),
                ft.Text("{:.2f}%".format(movie.getWatchProgress()/movie.getDuration()*100)),
            ]),
            ft.Column([
                ft.Text("Rating", size=20, color="#DAAB2D"),
                ft.Text(str(movie.getRating()))
            ]),
        ],
        spacing=18)
    
    def informasiFilm(self, movie: Movie , page, informasi : ft.Column, informasiEdit : ft.Column, database: Database, scrollCard : ScrollableCard):
        informasi.controls.clear()
        informasi.controls.append(
            FilmInformation(movie, page, informasi, informasiEdit, database, scrollCard)
        )
        page.go("/informasi-film-series")

class EntryCardSeries(ft.ElevatedButton):
    # Constructor entry card dengan parameter
    def __init__(self, series : Series, page, informasi, informasiEdit, scrollCard : ScrollableCard):
        super().__init__()
        self.width = 1000
        self.bgcolor = "#092143"
        self.on_click = lambda _: self.informasiSeries(series, page, informasi, informasiEdit, database, scrollCard)
        self.style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            )
        self.content = ft.Row([
            ft.Container(
                padding=ft.padding.only(top=10, bottom=10, left=-15),
                content=ft.Image(src=series.getGambar(), width=115, height=115, fit=ft.ImageFit.COVER),
            ),
            ft.Column([
                ft.Text(series.getName(), size=20, color="#DAAB2D"),
                ft.Text(series.getGenre(), size=15),
            ]),
            ft.Column([
                ft.Text("Progress", size=20, color="#DAAB2D"),
                # ft.Text(series.getEpisodeProgress()),
                ft.Text("{:.2f}%".format(int(series.getWatchProgress() or 0)/int(series.getDuration() or 1)*100)),
            ]),
            ft.Column([
                ft.Text("Rating", size=20, color="#DAAB2D"),
                ft.Text(str(series.getRating()))
            ]),
        ],
        spacing=18)
    
    def informasiSeries(self, series: Series , page, informasi : ft.Column, informasiEdit : ft.Column, database: Database, scrollCard : ScrollableCard):
        informasi.controls.clear()
        informasi.controls.append(
            SeriesInformation(series, page, informasi, informasiEdit, database, scrollCard)
        )
        page.go("/informasi-film-series")




class FilmInformation(ft.Container):
    def __init__(self, movie : Movie, page: ft.Page, informasi : ft.Column, informasiEdit : ft.Column, database: Movie, scrollCard : ScrollableCard):
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
                ft.ElevatedButton("Delete Film", bgcolor=ft.colors.RED, on_click= lambda e: self.deleteMovie(e, movie, page, informasi, informasiEdit, database, scrollCard),color = '#ffffff')
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
        page.overlay.append(MovieEditPage(movie, page, database.getMovies(),database.getOngoingMovies(), database.getReviewMovies(), database.getWatchlistMovies(), database.getFinishedMovies()).file_picker)
        page.overlay.append(MovieEditPage(movie, page, database.getMovies(),database.getOngoingMovies(), database.getReviewMovies(), database.getWatchlistMovies(), database.getFinishedMovies()).date_picker)
        kolomHalaman.controls.clear()
        kolomHalaman.controls.append(
            #TODO: append Objek Edit Movie
            MovieEditPage(movie, page, database.getMovies(),database.getOngoingMovies(), database.getReviewMovies(), database.getWatchlistMovies(), database.getFinishedMovies())
        )
        
        page.go("/edit-film-series")

    def deleteMovie(e, self, movie: Movie, page: ft.Page, kolomHalaman : ft.Column, kolomHalamanEdit : ft.Column, database: Database, scrollCard : ScrollableCard):
        def on_yes(e):
            database.removeMovie(movie.getId())
            database.removeWatchlistMovie(movie.getId())
            database.removeFinishedMovie(movie.getId())
            database.removeOngoingMovie(movie.getId())
            database.removeReviewMovie(movie.getId())

            # Delete image file
            image_path = f"../assets/img/{movie.getId()}m.jpg"  # Adjust the file extension if necessary
            if os.path.isfile(image_path):
                os.remove(image_path)

            def navigate_to_root(e):
                page.go("/")
                page.update()

            popup = PopUp("Success!", "Your series has successfully deleted", navigate_to_root)
            popup.open_dlg_modal(e, page)
            
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
            
        
        def on_no(e):
            pass

        proceed_popup = YesOrNo("You may lose this movies permanently. Do you want to proceed?", page)
        proceed_popup.open_dlg_modal_yes_no(e, on_yes, on_no)

class SeriesInformation(ft.Container):
    def __init__(self, series : Series, page: ft.Page, kolomHalaman : ft.Column, kolomHalamanEdit: ft.Column, database: Database, scrollCard):
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
                ft.ElevatedButton("Edit Information",  bgcolor='#DAAB2D', color='#000000', on_click = lambda _: self.handleEditSeries(series,page,kolomHalamanEdit,database))
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
                ft.ElevatedButton("Delete Film", bgcolor=ft.colors.RED, color = '#ffffff', on_click = lambda _: self.deleteSeries(series, page, kolomHalaman, kolomHalamanEdit, database, scrollCard))
            ], alignment=ft.MainAxisAlignment.END)
        )
        
        self.content = ft.Column([
            header,
            content_container,
            delete
        ])
        self.page = page
    

    def handleEditSeries(self, series:Series, page: ft.Page, kolomHalamanEdit: ft.Column, database: Database):
        #TODO: Implementasi injeksi objek Series Movie pada halaman edit film series (pakai variabel kolomHalaman dan jangan lupa clear isi kolomHalaman sebelum melakukan append)
        page.overlay.append(SeriesEditPage(series, page, database.getSeries(),database.getOngoingSeries(), database.getReviewSeries(), database.getWatchlistSeries(), database.getFinishedSeries()).file_picker)
        page.overlay.append(SeriesEditPage(series, page, database.getSeries(),database.getOngoingSeries(), database.getReviewSeries(), database.getWatchlistSeries(), database.getFinishedSeries()).date_picker)
        kolomHalamanEdit.controls.clear()
        kolomHalamanEdit.controls.append(
            #TODO: append Objek Edit Series
            SeriesEditPage(series, page, database.getSeries(),database.getOngoingSeries(), database.getReviewSeries(), database.getWatchlistSeries(), database.getFinishedSeries())
        )
        page.go("/edit-film-series")

    def deleteSeries(e, series : Series, page: ft.Page, kolomHalaman: ft.Column, kolomHalamanEdit: ft.Column, database: Database, scrollCard : ScrollableCard):
        def on_yes(e):
            database.removeSeries(series.getId())
            database.removeWatchlistSeries(series.getId())
            database.removeFinishedSeries(series.getId())
            database.removeOngoingSeries(series.getId())
            database.removeReviewSeries(series.getId())

            image_path = f"../assets/img/{series.getId()}s.jpg"
            if os.path.isfile(image_path):
                os.remove(image_path)

            def navigate_to_root(e):
                page.go("/")
                page.update()

            popup = PopUp("Success!", "Your series has successfully deleted", navigate_to_root)
            popup.open_dlg_modal(e, page)

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
        
        def on_no(e):
            pass

        proceed_popup = YesOrNo("You may lose this series permanently. Do you want to proceed?", page)
        proceed_popup.open_dlg_modal_yes_no(e, on_yes, on_no)

    def go_back(self, page):
        page.go("/")
