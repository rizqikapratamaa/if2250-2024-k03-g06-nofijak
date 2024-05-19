import flet as ft
from database.database import *
from page.add_page import *
from utils.search import *

from utils.content import Movie, Series
from page.film_series_information import ScrollableCard

# TODO: Refactor pengelolaan basis data dalam bentuk objek atau class
database = Database()

class informasiFilmSeries(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.width = page.window_width,
        self.height = page.window_height,
        self.bgcolor = '#000D20'


def main(page: ft.Page):
    scrollCard = ScrollableCard()

    kolomHalaman = ft.Column(
        width = page.window_width-50,
        height = page.window_height,
        scroll = ft.ScrollMode.ALWAYS,
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
        width = page.window_width-25,
        height = page.window_height-10,
        scroll = ft.ScrollMode.ADAPTIVE,
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


    movie_add_page = MovieAddPage(page, kolomHalaman, kolomHalamanEdit, scrollCard, database.getMovies(), database.getOngoingMovies(), database.getReviewMovies(), database.getWatchlistMovies(), database.getFinishedMovies(), database)
    series_add_page = SeriesAddPage(page, kolomHalaman, kolomHalamanEdit, scrollCard, database.getSeries(), database.getOngoingSeries(), database.getReviewSeries(), database.getWatchlistSeries(), database.getFinishedSeries(), database)
    
    page.title = "NoFiJak"
    page.overlay.append(movie_add_page.date_picker)
    page.overlay.append(movie_add_page.file_picker)
    page.window_resizable = False
    
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

    def change_view(new_view: str, scrollCard : ScrollableCard):
        global current_view
        current_view = new_view

        for button in header_buttons:
            if button.data == new_view:
                button.content.bgcolor = BUTTON_ON_COLOR
                if (new_view == ALL_ENTRIES):
                    scrollCard.inisialisasiCard()
                    for i in database.getMovies():
                        movie = database.make_movies(i)
                        scrollCard.tambahCardMovie(
                            movie,
                            page,
                            kolomHalaman,
                            kolomHalamanEdit,
                        )
                    for i in database.getSeries():
                        series = database.make_series(i)
                        scrollCard.tambahCardSeries(
                            series,
                            page,
                            kolomHalaman,
                            kolomHalamanEdit
                        )
                if (new_view == WATCHLIST):
                    scrollCard.inisialisasiCard()
                    for i in database.getWatchlistMovies():
                        movie = database.make_movies(i)
                        scrollCard.tambahCardMovie(
                            movie,
                            page,
                            kolomHalaman,
                            kolomHalamanEdit
                        )
                    for i in database.getWatchlistSeries():
                        series = database.make_series(i)
                        scrollCard.tambahCardSeries(
                            series,
                            page,
                            kolomHalaman,
                            kolomHalamanEdit
                        )
                if (new_view == ONGOING):
                    scrollCard.inisialisasiCard()
                    for i in database.getOngoingMovies():
                        movie = database.make_movies(i)
                        scrollCard.tambahCardMovie(
                            movie,
                            page,
                            kolomHalaman,
                            kolomHalamanEdit
                        )
                    for i in database.getOngoingSeries():
                        series = database.make_series(i)
                        scrollCard.tambahCardSeries(
                            series,
                            page,
                            kolomHalaman,
                            kolomHalamanEdit
                        )
                if (new_view == COMPLETED):
                    scrollCard.inisialisasiCard()
                    for i in database.getFinishedMovies():
                        movie = database.make_movies(i)
                        scrollCard.tambahCardMovie(
                            movie,
                            page,
                            kolomHalaman,
                            kolomHalamanEdit
                        )
                    for i in database.getFinishedMovies():
                        series = database.make_series(i)
                        scrollCard.tambahCardSeries(
                            series,
                            page,
                            kolomHalaman,
                            kolomHalamanEdit
                        )
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

    def dropdownSortchange(e):
        dropdownSort.value
        scrollCard.inisialisasiCard()
        if dropdownSort.value == "Rating":
            # Konversi dictionary ke objek Movie dan Series yang dapat diurutkan
            movie_objects = [database.make_movies(id) for id in database.getMovies()]
            series_objects = [database.make_series(id) for id in database.getSeries()]

            # Gabungkan movie dan series menjadi satu list
            all_content = [obj for obj in movie_objects + series_objects if obj is not None]

            # Pengurutan dengan nilai default untuk None. Menetapkan nilai tinggi untuk None agar berada di bawah.
            sorted_content = sorted(
                all_content,
                key=lambda x: x.getRating() if x.getRating() is not None else 0,
                reverse=True
            )

            # Tambahkan hasil yang sudah diurutkan ke scrollCard
            for content in sorted_content:
                if isinstance(content, Movie):
                    scrollCard.tambahCardMovie(
                        content,
                        page,
                        kolomHalaman,
                        kolomHalamanEdit
                    )
                elif isinstance(content, Series):
                    scrollCard.tambahCardSeries(
                        content,
                        page,
                        kolomHalaman,
                        kolomHalamanEdit
                    )

        if(dropdownSort.value == "Genre"):
            all_content = []
            for id in database.getMovies():
                all_content.append(database.make_movies(id))
            for id in database.getSeries():
                all_content.append(database.make_series(id))

            # Hapus None dari all_content jika ada
            all_content = [content for content in all_content if content is not None]

            # Urutkan berdasarkan genre
            sorted_content = sorted(all_content, key=lambda x: x.getGenre())

            # Tambahkan konten yang sudah diurutkan ke scrollCard
            for content in sorted_content:
                if isinstance(content, Movie):
                    scrollCard.tambahCardMovie(
                        content,
                        page,
                        kolomHalaman,
                        kolomHalamanEdit
                    )
                elif isinstance(content, Series):
                    scrollCard.tambahCardSeries(
                        content,
                        page,
                        kolomHalaman,
                        kolomHalamanEdit
                    )

        page.update()

    def searchButtonHandler(scrollCard : ScrollableCard):
        scrollCard.inisialisasiCard()
        print(searchField.value)
        moviesResult = searchMovies(searchField.value)
        seriesResult = searchSeries(searchField.value)
        
        for movie in moviesResult:
            scrollCard.tambahCardMovie(
                movie,
                page,
                kolomHalaman,
                kolomHalamanEdit
            )

        for serie in seriesResult:
            scrollCard.tambahCardSeries(
                serie,
                page,
                kolomHalaman,
                kolomHalamanEdit
            )
        
        print(moviesResult)
        print(seriesResult)
        page.update()
            
    
    # ==============================================
    # ============== Custom Controls ===============
    # ==============================================
    class HeaderButton(ft.Container):
        def __init__(self, ButtonText, ButtonData, ContainerPadding):
            super().__init__()
            self.padding = ContainerPadding
            self.alignment = ft.alignment.center
            self.content = ft.ElevatedButton(ButtonText, on_click=lambda _: change_view(ButtonData, scrollCard), bgcolor=BUTTON_OFF_COLOR, color='#000000')
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
    change_view(current_view, scrollCard)

    # >> Header dropdowns
    dropdownSort = ft.Dropdown(
        padding = ft.padding.only(top=50,left=25),
        label="Sort",
        bgcolor='#092143',
        hint_text="Sort items by..",
        on_change=dropdownSortchange,
        options=[
            ft.dropdown.Option("Rating"),
            ft.dropdown.Option("Genre"),
        ],
    )
    dropdownFilter = ft.Dropdown(
        padding=ft.padding.only(top=50, left=25),
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
    searchField = ft.TextField(
                width=550,
                text_style=ft.TextStyle(color='#000000'),
                border_radius=50,
                bgcolor='#ffffff',
                border_color='',
                on_change=textbox_changed
            )
    searchButton = ft.IconButton(
        ft.icons.SEARCH,
        icon_color='#ffffff',
        on_click= lambda _: searchButtonHandler(scrollCard)
    )
    textbox = ft.Container(
        padding = ft.padding.only(left=315,top=20),
        shape=ft.RoundedRectangleBorder(radius=50),
        content = ft.Row([
                searchButton,
                searchField, 
        ])
    )


    # >> Contoh fungsi untuk meload database ke dalam Scroll Card
    # def load_data():
    #     scrollCard = ScrollableCard()

    #     for i in database.getMovies():
    #         movie = database.make_movies(i)
    #         scrollCard.tambahCardMovie(
    #             movie,
    #             page,
    #             kolomHalaman,
    #             kolomHalamanEdit
    #         )

    #     for i in database.getSeries():
    #         series = database.make_series(i)
    #         scrollCard.tambahCardSeries(
    #             series,
    #             page,
    #             kolomHalaman,
    #             kolomHalamanEdit
    #         )

    #     return scrollCard

    def route_change(route):
        page.views.clear(),
        global database
        database = Database()
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
