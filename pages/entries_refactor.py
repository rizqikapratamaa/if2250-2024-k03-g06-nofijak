import flet as ft
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from content import Movie, Series
from film_information import FilmInformation

class informasiFilmSeries(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.width = page.window_width,
        self.height = page.window_height,
        self.bgcolor = '#000D20'

   

class EntryCard(ft.ElevatedButton):
    # Constructor entry card dengan parameter
    def __init__(self, movie : Movie, page, informasi):
        super().__init__()
        self.width = 600
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
            FilmInformation(movie, page)
            # ft.ElevatedButton(
            #     width=600,
            #     bgcolor="#092143",
            #     style=ft.ButtonStyle(
            #         shape=ft.RoundedRectangleBorder(radius=10),
            #     ),
            #     content=ft.Row(
            #         [
            #             ft.Container(
            #                 padding=ft.padding.only(top=10, bottom=10, left=-15),
            #                 content=ft.Image(src=movie.getGambar(), width=115, height=115, fit=ft.ImageFit.COVER),
            #             ),
            #             ft.Column(
            #                 [
            #                     ft.Text(movie.getName(), size=20, color="#DAAB2D"),
            #                     ft.Text(movie.getGenre(), size=15),
            #                 ]
            #             ),
            #             ft.Column(
            #                 [
            #                     ft.Text("Progress", size=20, color="#DAAB2D"),
            #                     ft.Text("{:.2f}%".format(movie.getWatchProgress()/movie.getDuration()*100)),
            #                 ]
            #             ),
            #             ft.Column(
            #                 [
            #                     ft.Text("Rating", size=20, color="#DAAB2D"),
            #                     ft.Text(str(movie.getRating()))
            #                 ]
            #             ),
            #         ],
            #         spacing=18
            #     )
            # )
        )
        page.go("/informasi-film-series")      
        # page.views.append(
        #     ft.View(
        #         [
        #             ft.Container(
        #             width = page.window_width,
        #             height = page.window_height,
        #             bgcolor = '#000D20',
        #             )
        #         ],
        #     )
        # )

class ScrollableCard(ft.Column):
    def __init__(self):
        # Inisialisasi base class dari ft.ColumnF
        super().__init__()
        # Properti untuk scrollable card
        self.height = 250
        self.width = 600
        self.scroll = ft.ScrollMode.ALWAYS
    
    # Method untuk menambahkan film pada halaman entries
    def tambahCard(self, movie, page, Informasi):
        self.controls.append(
            EntryCard(movie, page, Informasi)
        )



        
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
    kolomInformasi = ft.Column(
        width = page.window_width,
        height = page.window_height
    )
    informasi =  ft.Container(
        width = page.window_width,
        height = page.window_height,
        bgcolor = '#000D20',
        content = ft.Column(
            [
                kolomInformasi
            ]
        )
    )
    # Functions
    def tambahFilmSeries(e):
        movie = Movie(1, "Adventure Time", 2010, 74, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis nibh vitae purus consectetur facilisis sed vitae ipsum. Quisque faucibus sed nulla placerat sagittis. Phasellus condimentum risus vitae nulla vestibulum auctor. Curabitur scelerisque, nibh eget imperdiet consequat, odio ante tempus diam, sed volutpat nisl erat eget turpis. Sed viverra, diam sit amet blandit vulputate, mi tellus dapibus lorem, vitae vehicula diam mauris placerat diam. Morbi sit amet pretium turpis, et consequat ligula. Nulla velit sem, suscipit sit amet dictum non, tincidunt sed nulla. Aenean pellentesque odio porttitor sagittis aliquam. Nam varius at metus vitae vulputate. Praesent faucibus nibh lorem, eu pretium dolor dictum nec. Phasellus eget dui laoreet, viverra magna vitae, pellentesque diam.", "Adventure, Melodrama, Animation", 8.5, 45, "https://yt3.googleusercontent.com/ytc/AIdro_kECsRD-CffXuBZyiBFW6eTnfhnvc3Rkmw9EwXWH9TSUw=s900-c-k-c0x00ffffff-no-rj")
        scrollCard.tambahCard(
            movie,
            page,
            kolomInformasi
        )
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
                        informasi
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