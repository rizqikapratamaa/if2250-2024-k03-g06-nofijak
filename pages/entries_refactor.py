import flet as ft

class EntryCard(ft.Card):
    # Constructor entry card dengan parameter
    def __init__(self, title, description, progress, jumlahepisode, rating, imagepath):
        super().__init__()
        self.width = 600
        self.color = "#092143"
        self.content = ft.Row([
            ft.Container(
                padding=ft.padding.only(top=10, bottom=10, left=10),
                content=ft.Image(src=imagepath, width=115, height=115, fit=ft.ImageFit.COVER),
            ),
            ft.Column([
                ft.Text(title, size=20, color="#DAAB2D"),
                ft.Text(description, size=15),
            ]),
            ft.Column([
                ft.Text("Progress", size=20, color="#DAAB2D"),
                ft.Text(f"{progress}% ({jumlahepisode} eps)"),
            ]),
            ft.Column([
                ft.Text("Rating", size=20, color="#DAAB2D"),
                ft.Text(str(rating))
            ]),
        ],
        spacing=25)

class ScrollableCard(ft.Column):
    def __init__(self):
        # Inisialisasi base class dari ft.Column
        super().__init__()
        # Properti untuk scrollable card
        self.height = 250
        self.width = 600
        self.scroll = ft.ScrollMode.ALWAYS
    
    # Method untuk menambahkan film pada halaman entries
    def tambahCard(self, title, description, progress, jumlahEpisode, rating, imagepath):
        self.controls.append(
            EntryCard(title, description, progress, jumlahEpisode, rating, imagepath)
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
    
    # Functions
    def tambahFilmSeries(e):
        page.go("/tambah-film-series")
        scrollCard.tambahCard(
            "Adventure Time",
            "Adventure, Melodrama, Animation",
            74,
            45,
            8.5,
            "https://yt3.googleusercontent.com/ytc/AIdro_kECsRD-CffXuBZyiBFW6eTnfhnvc3Rkmw9EwXWH9TSUw=s900-c-k-c0x00ffffff-no-rj"
        )

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
        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)