import flet as ft
import sys
import os
import sqlite3
from database import *
from add_page import *

from content import Movie, Series
from film_series_information import FilmInformation, SeriesInformation

# TODO: Refactor pengelolaan basis data dalam bentuk objek atau class
database = Database()

class informasiFilmSeries(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.width = page.window_width,
        self.height = page.window_height,
        self.bgcolor = '#000D20'

class EntryCardMovie(ft.ElevatedButton):
    # Constructor entry card dengan parameter
    def __init__(self, movie : Movie, page, informasi, informasiEdit):
        super().__init__()
        self.width = 900
        self.bgcolor = "#092143"
        self.on_click = lambda _: self.informasiFilm(movie, page, informasi, informasiEdit, database)
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
    
    def informasiFilm(self, movie: Movie , page, informasi : ft.Column, informasiEdit : ft.Column, database: Database):
        informasi.controls.clear()
        informasi.controls.append(
            FilmInformation(movie, page, informasi, informasiEdit, database)
        )
        page.go("/informasi-film-series")

class EntryCardSeries(ft.ElevatedButton):
    # Constructor entry card dengan parameter
    def __init__(self, series : Series, page, informasi, informasiEdit):
        super().__init__()
        self.width = 900
        self.bgcolor = "#092143"
        self.on_click = lambda _: self.informasiSeries(series, page, informasi, informasiEdit, database)
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
    
    def informasiSeries(self, series: Series , page, informasi : ft.Column, informasiEdit : ft.Column, database: Database):
        informasi.controls.clear()
        informasi.controls.append(
            SeriesInformation(series, page, informasiEdit, database)
        )
        page.go("/informasi-film-series")

class ScrollableCard(ft.Column):
    def __init__(self):
        # Inisialisasi base class dari ft.ColumnF
        super().__init__()
        # Properti untuk scrollable card
        self.height = 250
        self.width = 800
        self.scroll = ft.ScrollMode.ALWAYS
    
    # Method untuk menambahkan film pada halaman entries
    def tambahCardMovie(self, movie, page, Informasi, informasiEdit):
        self.controls.append(
            EntryCardMovie(movie, page, Informasi, informasiEdit)
        )
    
    def tambahCardSeries(self, series, page, Informasi, InformasiEdit):
        self.controls.append(
            EntryCardSeries(series, page, Informasi, InformasiEdit)
        )

    def inisialisasiCard(self):
        self.controls.clear()



        
def main(page: ft.Page):
    page.title = "NoFiJak"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # >> Color constants
    BUTTON_ON_COLOR = '#DAAB2D'
    BUTTON_OFF_COLOR = '#4F3D09'
    
    # >> Header button logic
    current_view = 'all-entries'
    
    ALL_ENTRIES = 'all-entries'
    COMPLETED = 'completed'
    ONGOING = 'on-going'
    WATCHLIST = 'watchlist'
    
    header_buttons = []
    kolomHalaman = ft.Column(
        width = page.window_width-50,
        height = page.window_height-80,
        scroll = ft.ScrollMode.AUTO,
    )
    
    halaman =  ft.Container(
        width = page.window_width,
        height = page.window_height,
        bgcolor = '#000D20',
        content = ft.Column(
            [
                kolomHalaman
            ]
        )
    )

    kolomHalamanEdit = ft.Column(
        width = page.window_width-50,
        height = page.window_height-80,
        scroll = ft.ScrollMode.AUTO,
    )
    
    halamanEdit =  ft.Container(
        width = page.window_width,
        height = page.window_height,
        bgcolor = '#000D20',
        content = ft.Column(
            [
                kolomHalamanEdit
            ]
        )
    )

    movie_add_page = MovieAddPage(page, database.getMovies(), database.getOngoingMovies(), database.getReviewMovies(), database.getWatchlistMovies(), database.getFinishedMovies())
    series_add_page = SeriesAddPage(page, database.getSeries(), database.getOngoingSeries(), database.getReviewSeries(), database.getWatchlistSeries(), database.getFinishedSeries())

    # Functions
    def tambahFilm(e):
        page.go("/tambah-film-series/film")
        page.update()

    def tambahSeries(e):
        page.go("/tambah-film-series/series")
        page.update()
    
    def textbox_changed(e):
        t.value = e.control.value
        page.update()

    def change_view(new_view: str):
        global current_view
        current_view = new_view

        for button in header_buttons:
            if button.data == new_view:
                button.content.bgcolor = BUTTON_ON_COLOR
            else:
                button.content.bgcolor = BUTTON_OFF_COLOR
                
        page.update()

    def dropdownFilterchange(e):
        dropdownFilter.value
        scrollCard.inisialisasiCard()
        if(dropdownFilter.value == "Movies"):
            for i in database.getMovies():
                movie = database.make_movies(i)
                scrollCard.tambahCardMovie(
                    movie,
                    page,
                    kolomHalaman,
                    kolomHalamanEdit
                )
        if(dropdownFilter.value == "Series"):
            for i in database.getSeries():
                series = database.make_series(i)
                scrollCard.tambahCardSeries(
                    series,
                    page,
                    kolomHalaman,
                    kolomHalamanEdit
                )
        page.update()
        

    
    # ==============================================
    # ============== Custom Controls ===============
    # ==============================================
    class HeaderButton(ft.Container):
        def __init__(self, ButtonText, ButtonData, ContainerPadding):
            super().__init__()
            self.padding = ContainerPadding
            self.alignment = ft.alignment.center
            self.content = ft.ElevatedButton(ButtonText, on_click=lambda _: change_view(ButtonData), bgcolor=BUTTON_OFF_COLOR, color='#000000')
            self.data = ButtonData
    

    # ==============================================
    # ================== Controls ==================
    # ==============================================
    # >> Header buttons
    # >>>> All Entries button
    allEntries = HeaderButton("All Entries", ALL_ENTRIES, 15)
    
    # >>>> Completed button
    completed = HeaderButton("Completed", COMPLETED, ft.padding.only(left=50,right=350))
    
    # >>>> Ongoing button
    ongoing = HeaderButton("Ongoing", ONGOING, ft.padding.only(left=50,right=50))
    
    # >>>> Watchlist button
    watchlist = HeaderButton("Watchlist", WATCHLIST, ft.padding.only(left=350,right=50))
    
    # >>>> List of header buttons
    header_buttons = [allEntries, completed, ongoing, watchlist]
    change_view(current_view)

    # >> Header dropdowns
    dropdownSort = ft.Dropdown(
        padding = ft.padding.only(top=50,left=25),
        label="Sort",
        bgcolor='#092143',
        hint_text="Sort items by..",
        # on_change=dropdownSortchange,
        options=[
            ft.dropdown.Option("Rating"),
            ft.dropdown.Option("Genre"),
        ],
    )
    dropdownFilter = ft.Dropdown(
        padding = ft.padding.only(top=50,left=25),
        label="Filter",
        bgcolor='#092143',
        hint_text="Filter items by..",
        on_change= dropdownFilterchange,
        options=[
            ft.dropdown.Option("Movies"),
            ft.dropdown.Option("Series"),
        ],
    )
    
    # >> Floating action button
    actionButton = ft.Container(
        alignment=ft.alignment.bottom_right,
        padding=ft.padding.only(right=50),
        content=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=tambahFilm, bgcolor=BUTTON_ON_COLOR, foreground_color='#000000', shape=ft.RoundedRectangleBorder(radius=50))
    )

    
    
    # >> Search box
    t = ft.Text()
    textbox = ft.Container(
        padding = ft.padding.only(top=20),
        alignment=ft.alignment.center,
        shape=ft.RoundedRectangleBorder(radius=50),
        content = ft.TextField(
            width=550,
            text_style=ft.TextStyle(color='#000000'),
            prefix_icon= ft.icons.SEARCH,
            border_radius=50,
            bgcolor='#ffffff',
            border_color='',
            on_change=textbox_changed
        )
    )

    scrollCard = ScrollableCard()
    
    # ==============================================
    # ================== Database ==================
    # ==============================================
    for i in database.getMovies():
        movie = database.make_movies(i)
        scrollCard.tambahCardMovie(
            movie,
            page,
            kolomHalaman,
            kolomHalamanEdit
        )

    for i in database.getSeries():
        series = database.make_series(i)
        scrollCard.tambahCardSeries(
            series,
            page,
            kolomHalaman,
            kolomHalamanEdit
        )


    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Container(
                        width = page.window_width,
                        height = page.window_height,
                        bgcolor = '#000D20',
                        content =
                        ft.Column([
                            ft.Row([
                                dropdownSort,
                                dropdownFilter,
                            ]),
                            allEntries,
                            ft.Container(
                                alignment=ft.alignment.center,
                                content = ft.Row([
                                watchlist,
                                ongoing,
                                completed,
                                ]),

                            ),
                            textbox,
                            ft.Container(
                                alignment=ft.alignment.center,
                                content = scrollCard,
                            ),
                            actionButton,
                        ]),
                    )
                ],

            )
        )


        if page.route == "/informasi-film-series":
            page.views.append(
                ft.View(
                    "/informasi-film-series",
                    [
                        halaman
                    ],
                )
            )
        if page.route == "/tambah-film-series/film":
            page.clean()
            movie_add_page.movies_show_page(page)
        
        if page.route == "/tambah-film-series/series":
            series_add_page.series_show_page(page)

        if page.route == "/edit-film-series":
            page.views.append(
                ft.View(
                    "/edit-film-series",
                    [
                        #TODO: Implementasi halaman edit film/series (caranya mirip kaya informasi-film-series)
                        halamanEdit
                    ],
                )
            )
        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
