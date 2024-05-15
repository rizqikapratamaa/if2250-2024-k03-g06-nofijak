import flet as ft

def main(page: ft.Page):
    page.title = "NoFiJak"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def tambahFilmSeries(e):
        page.go("/tambah-film-series")

    def textbox_changed(e):
        t.value = e.control.value
        page.update()
    # appBar = ft.Container(
    #     padding = 10,
    #     content = ft.AppBar(title=ft.Text("Flet app"))
    # )
    allEntriesState = ft.Container(
        padding = 15,
        alignment=ft.alignment.center,
        content = ft.ElevatedButton("All Entries", on_click=lambda _: page.go("/"), bgcolor='#DAAB2D', color='#000000')
    )
    watchlistState = ft.Container(
        padding = ft.padding.only(left=350,right=50),
        content =  ft.ElevatedButton("Watchlist", on_click=lambda _: page.go("/watchlist"), bgcolor='#DAAB2D', color='#000000')
    )
    ongoingState = ft.Container(
        padding = ft.padding.only(left=50,right=50),
        content = ft.ElevatedButton("Ongoing", on_click=lambda _: page.go("/on-going"), bgcolor='#DAAB2D', color='#000000')
    )
    completedState = ft.Container(
        padding = ft.padding.only(left=50,right=350),
        content = ft.ElevatedButton("Completed", on_click=lambda _: page.go("/completed"), bgcolor='#DAAB2D', color='#000000')
    )
    allEntries = ft.Container(
        padding = 15,
        alignment=ft.alignment.center,
        content = ft.ElevatedButton("All Entries", on_click=lambda _: page.go("/"), bgcolor='#4F3D09', color='#000000')
    )
    completed = ft.Container(
        padding = ft.padding.only(left=50,right=350),
        alignment=ft.alignment.center,
        content = ft.ElevatedButton("Completed", on_click=lambda _: page.go("/completed"), bgcolor='#4F3D09', color='#000000')
    )
    ongoing = ft.Container(
        padding = ft.padding.only(left=50,right=50),
        alignment=ft.alignment.center,
        content = ft.ElevatedButton("On Going", on_click=lambda _: page.go("/on-going"), bgcolor='#4F3D09', color='#000000')
    )
    watchlist = ft.Container(
        padding = ft.padding.only(left=350,right=50),
        alignment=ft.alignment.center,
        content = ft.ElevatedButton("Watchlist", on_click=lambda _: page.go("/watchlist"), bgcolor='#4F3D09', color='#000000')
    )
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
        hint_text="filter items by..",
        options=[
            ft.dropdown.Option("Movies"),
            ft.dropdown.Option("Series"),
        ],
    )
    actionButton = ft.Container(
        alignment=ft.alignment.bottom_right,
        padding=ft.padding.only(right=50),
        content=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=tambahFilmSeries, bgcolor='#DAAB2D', foreground_color='#000000', shape=ft.RoundedRectangleBorder(radius=50))
    )
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
                            allEntriesState,
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
        if page.route == "/watchlist":
            page.views.append(
            ft.View(
                "/watchlist",
                [
                    ft.Container(
                        width = page.window_width,
                        height = page.window_height,
                        bgcolor = '#000D20',
                        content = ft.Column([
                            ft.Row([
                                dropdownSort,
                                dropdownFilter,
                            ]),
                            allEntries,
                            ft.Container(
                                alignment=ft.alignment.center,
                                content = ft.Row([
                                watchlistState,
                                ongoing,
                                completed,
                                ])
                            ),
                            textbox,
                            actionButton,
                        ])
                    )
                ],
            )
            )
        elif page.route == "/on-going":
            page.views.append(
            ft.View(
                "/on-going",
                [
                    ft.Container(
                        
                        width = page.window_width,
                        height = page.window_height,
                        bgcolor = '#000D20',
                        content = ft.Column([
                             ft.Row([
                                dropdownSort,
                                dropdownFilter,
                            ]),
                            allEntries,
                            ft.Container(
                                alignment=ft.alignment.center,
                                content = ft.Row([
                                watchlist,
                                ongoingState,
                                completed,
                                ])
                            ),
                            textbox,
                            actionButton,
                        ])
                    )
                ],
            )
            )
        elif page.route == "/completed":
            page.views.append(
            ft.View(
                "/completed",
                [
                    ft.Container(
                        width = page.window_width,
                        height = page.window_height,
                        bgcolor = '#000D20',
                        content = ft.Column([
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
                                completedState,
                                ])
                            ),
                            textbox,
                            actionButton,
                        ])
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