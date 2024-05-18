import flet as ft
import sys
import os
import sqlite3


from content import Movie, Series
from film_series_information import FilmInformation, SeriesInformation

# TODO: Refactor pengelolaan basis data dalam bentuk objek atau class
conn = sqlite3.connect("database.db")

movies_dict = {}
series_dict = {}
try:
    # Create a cursor object
    cursor = conn.cursor()

    # Commit changes
    conn.commit()

    # Retrieve data from the table
    # Fetch movies and store in a dictionary
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    
    for row in movies:
        movies_dict[row[0]] = list(row)

    # Fetch series and store in a dictionary
    cursor.execute("SELECT * FROM series")
    series = cursor.fetchall()
    for row in series:
        series_dict[row[0]] = list(row)

    # Fetch finished movies and store in a dictionary
    cursor.execute("SELECT * FROM finished_movies")
    finished_movies = cursor.fetchall()
    finished_movies_dict = {}
    for row in finished_movies:
        finished_movies_dict[row[0]] = list(row)

    

    cursor.execute("SELECT * FROM finished_series")
    finished_series = cursor.fetchall()
    finished_series_dict = {}
    for row in finished_series:
        finished_series_dict[row[0]] = list(row)

    cursor.execute("SELECT * FROM ongoing_movies")
    ongoing_movies = cursor.fetchall()
    ongoing_movies_dict = {}
    for row in ongoing_movies:
        ongoing_movies_dict[row[0]] = list(row)
    
    cursor.execute("SELECT * FROM ongoing_series")
    ongoing_series = cursor.fetchall()
    ongoing_series_dict = {}
    for row in ongoing_series:
        ongoing_series_dict[row[0]] = list(row)


    cursor.execute("SELECT * FROM review_movies")
    review_movies = cursor.fetchall()
    review_movies_dict = {}
    for row in review_movies:
        review_movies_dict[row[0]] = list(row)

    cursor.execute("SELECT * FROM review_series")
    review_series = cursor.fetchall()
    review_series_dict = {}
    for row in review_series:
        review_series_dict[row[0]] = list(row)

    cursor.execute("SELECT * FROM watchlist_movies")
    watchlist_movies = cursor.fetchall()
    watchlist_movies_dict = {}
    for row in watchlist_movies:
        watchlist_movies_dict[row[0]] = list(row)


    cursor.execute("SELECT * FROM watchlist_series")
    watchlist_series = cursor.fetchall()
    watchlist_series_dict = {}
    for row in watchlist_series:
        watchlist_series_dict[row[0]] = list(row)
        
    def make_movies(id):
        id = movies_dict[id][0] if id in movies_dict else None
        name = movies_dict[id][1] if id in movies_dict else None
        releaseDate = movies_dict[id][3] if id in movies_dict else None
        duration = movies_dict[id][2] if id in movies_dict else 0
        synopsis = movies_dict[id][5] if id in movies_dict else None
        genre = movies_dict[id][4] if id in movies_dict else None
        rating = review_movies_dict[id][1] if id in review_movies_dict else None
        watchProgress = ongoing_movies_dict[id][1] if id in ongoing_movies_dict else 0

        return Movie(id, name, releaseDate, duration, synopsis, genre, rating, watchProgress, "assets/img/" + str(id) + ".jpg")
    
    def make_series(id):
        id = series_dict[id][0] if id in series_dict else None
        name = series_dict[id][1] if id in series_dict else None
        releaseDate = series_dict[id][3] if id in series_dict else None
        duration = series_dict[id][2] if id in series_dict else None
        synopsis = series_dict[id][5] if id in series_dict else None
        genre = series_dict[id][4] if id in series_dict else None
        rating = review_series_dict[id][1] if id in review_series_dict else None
        watchProgress = ongoing_series_dict[id][3] if id in ongoing_series_dict else None
        season = series_dict[id][6] if id in series_dict else None
        episode = series_dict[id][7] if id in series_dict else None
        current_season = ongoing_series_dict[id][1] if id in ongoing_series_dict else None
        current_episode = ongoing_series_dict[id][2] if id in ongoing_series_dict else None
        return Series(id, name, releaseDate, duration, synopsis, genre, rating, watchProgress, "assets/img/" + str(id) + ".jpg", season, episode, current_season, current_episode)

except sqlite3.Error as e:
    print("An error occurred:", e)


finally:
    # Close connection
    conn.close()

class informasiFilmSeries(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.width = page.window_width,
        self.height = page.window_height,
        self.bgcolor = '#000D20'

class EntryCardMovie(ft.ElevatedButton):
    # Constructor entry card dengan parameter
    def __init__(self, movie : Movie, page, informasi):
        super().__init__()
        self.width = 1000
        self.bgcolor = "#092143"
        self.on_click = lambda _: self.informasiFilm(movie, page, informasi)
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
    
    def informasiFilm(self, movie: Movie , page, informasi : ft.Column):
        informasi.controls.clear()
        informasi.controls.append(
            FilmInformation(movie, page, informasi)
        )
        page.go("/informasi-film-series")

class EntryCardSeries(ft.ElevatedButton):
    # Constructor entry card dengan parameter
    def __init__(self, series : Series, page, informasi):
        super().__init__()
        self.width = 1000
        self.bgcolor = "#092143"
        self.on_click = lambda _: self.informasiSeries(series, page, informasi)
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
    
    def informasiSeries(self, series: Series , page, informasi : ft.Column):
        informasi.controls.clear()
        informasi.controls.append(
            SeriesInformation(series, page, informasi)
        )
        page.go("/informasi-film-series")

class ScrollableCard(ft.Column):
    def __init__(self):
        # Inisialisasi base class dari ft.ColumnF
        super().__init__()
        # Properti untuk scrollable card
        self.height = 250
        self.width = 1000
        self.scroll = ft.ScrollMode.ALWAYS
    
    # Method untuk menambahkan film pada halaman entries
    def tambahCardMovie(self, movie, page, Informasi):
        self.controls.append(
            EntryCardMovie(movie, page, Informasi)
        )
    
    def tambahCardSeries(self, series, page, Informasi):
        self.controls.append(
            EntryCardSeries(series, page, Informasi)
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
        width = page.window_width,
        height = page.window_height
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

    # Functions
    def tambahFilmSeries(e):
        #TODO: Implementasi halaman untuk menambah film/series (Contoh bisa dilihat pada method informasiFilm dan informasiSeries)
        page.go("/tambah-film-series")
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
                    for i in movies_dict:
                        movie = make_movies(i)
                        scrollCard.tambahCardMovie(
                            movie,
                            page,
                            kolomHalaman
                        )
                    for i in series_dict:
                        series = make_series(i)
                        scrollCard.tambahCardSeries(
                            series,
                            page,
                            kolomHalaman
                        )
                if (new_view == WATCHLIST):
                    scrollCard.inisialisasiCard()
                    for i in watchlist_movies_dict:
                        movie = make_movies(i)
                        scrollCard.tambahCardMovie(
                            movie,
                            page,
                            kolomHalaman
                        )
                    for i in watchlist_series_dict:
                        series = make_series(i)
                        scrollCard.tambahCardSeries(
                            series,
                            page,
                            kolomHalaman
                        )
                if (new_view == ONGOING):
                    scrollCard.inisialisasiCard()
                    for i in ongoing_movies_dict:
                        movie = make_movies(i)
                        scrollCard.tambahCardMovie(
                            movie,
                            page,
                            kolomHalaman
                        )
                    for i in ongoing_series_dict:
                        series = make_series(i)
                        scrollCard.tambahCardSeries(
                            series,
                            page,
                            kolomHalaman
                        )
                if (new_view == COMPLETED):
                    scrollCard.inisialisasiCard()
                    for i in finished_movies_dict:
                        movie = make_movies(i)
                        scrollCard.tambahCardMovie(
                            movie,
                            page,
                            kolomHalaman
                        )
                    for i in finished_series_dict:
                        series = make_series(i)
                        scrollCard.tambahCardSeries(
                            series,
                            page,
                            kolomHalaman
                        )
            else:
                button.content.bgcolor = BUTTON_OFF_COLOR
                
        page.update()

    def dropdownFilterchange(e):
        dropdownFilter.value
        scrollCard.inisialisasiCard()
        if(dropdownFilter.value == "Movies"):
            for i in movies_dict:
                movie = make_movies(i)
                scrollCard.tambahCardMovie(
                    movie,
                    page,
                    kolomHalaman
                )
        if(dropdownFilter.value == "Series"):
            for i in series_dict:
                series = make_series(i)
                scrollCard.tambahCardSeries(
                    series,
                    page,
                    kolomHalaman
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

    allEntries.content.bgcolor = BUTTON_ON_COLOR

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
        content=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=tambahFilmSeries, bgcolor=BUTTON_ON_COLOR, foreground_color='#000000', shape=ft.RoundedRectangleBorder(radius=50))
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
    for i in movies_dict:
        movie = make_movies(i)
        scrollCard.tambahCardMovie(
            movie,
            page,
            kolomHalaman
        )

    for i in series_dict:
        series = make_series(i)
        scrollCard.tambahCardSeries(
            series,
            page,
            kolomHalaman
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
        if page.route == "/tambah-film-series":
            page.views.append(
                ft.View(
                    "/tambah-film-series",
                    [
                        # TODO: Impelementasi halaman tambah film/series
                        # Construct Kelas pada View ini jadi tidak perlu clear dan append kolom pada page
                        # karena halaman page sudah pasti/tidak berubah seperti halaman informasi-film-series
                        

                    ],
                )
            )
        if page.route == "/edit-film-series":
            page.views.append(
                ft.View(
                    "/edit-film-series",
                    [
                        #TODO: Implementasi halaman edit film/series (caranya mirip kaya informasi-film-series)
                        halaman
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
