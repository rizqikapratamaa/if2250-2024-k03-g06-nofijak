import flet as ft

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
    # appBar = ft.Container(
    #     padding = 10,
    #     content = ft.AppBar(title=ft.Text("Flet app"))
    # )
    
    # ==============================================
    # ================= Components =================
    # ==============================================
    # >> Header buttons
    allEntries = ft.Container(
        padding = 15,
        alignment=ft.alignment.center,
        content = ft.ElevatedButton("All Entries", on_click=lambda _: change_view(ALL_ENTRIES), bgcolor=BUTTON_ON_COLOR, color='#000000'),
        data = ALL_ENTRIES
    )
    completed = ft.Container(
        padding = ft.padding.only(left=50,right=350),
        alignment=ft.alignment.center,
        content = ft.ElevatedButton("Completed", on_click=lambda _: change_view(COMPLETED), bgcolor=BUTTON_OFF_COLOR, color='#000000'),
        data = COMPLETED
    )
    ongoing = ft.Container(
        padding = ft.padding.only(left=50,right=50),
        alignment=ft.alignment.center,
        content = ft.ElevatedButton("Ongoing", on_click=lambda _: change_view(ONGOING), bgcolor=BUTTON_OFF_COLOR, color='#000000'),
        data = ONGOING
    )
    watchlist = ft.Container(
        padding = ft.padding.only(left=350,right=50),
        alignment=ft.alignment.center,
        content = ft.ElevatedButton("Watchlist", on_click=lambda _: change_view(WATCHLIST), bgcolor=BUTTON_OFF_COLOR, color='#000000'),
        data = WATCHLIST
    )

    header_buttons = [allEntries, completed, ongoing, watchlist]

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