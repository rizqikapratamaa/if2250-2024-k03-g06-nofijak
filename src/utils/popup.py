import flet as ft

class PopUp:
    def __init__(self, title, text, on_close):
        self.clicked = False
        self.on_close = on_close
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(title),
            content=ft.Text(text),
            actions=[
                ft.TextButton("Ok", on_click=self.close_dlg)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=self.on_dismiss,
        )

    def getClicked(self):
        return self.clicked

    def close_dlg(self, e):
        self.dlg_modal.open = False
        self.clicked = True
        print(self.clicked)
        self.on_close(e)  # Call the provided callback function with event argument

    def on_dismiss(self, e):
        print("Modal dialog dismissed!")

    def open_dlg_modal(self, e, page: ft.Page):
        page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        page.update()

class YesOrNo:
    def __init__(self, text, page: ft.Page):
        self.action = False
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Are you sure?"),
            content=ft.Text(text),
            actions=[
                ft.TextButton("Yes", on_click=self.yes),
                ft.TextButton("No", on_click=self.no),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page = page
        self.yes_callback = None
        self.no_callback = None

    def getAction(self):
        return self.action

    def yes(self, e):
        self.dlg_modal.open = False
        self.action = True
        print("Yes")
        print(self.action)
        if self.yes_callback:
            self.yes_callback(e)
        self.page.update()

    def no(self, e):
        self.dlg_modal.open = False
        print("No")
        print(self.action)
        self.action = False
        if self.no_callback:
            self.no_callback(e)
        self.page.update()

    def open_dlg_modal_yes_no(self, e, yes_callback, no_callback):
        self.yes_callback = yes_callback
        self.no_callback = no_callback
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()