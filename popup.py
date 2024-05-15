import flet as ft
import time

class PopUp:
    def __init__(self,text, page: ft.Page):
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Warning!"),
            content=ft.Text(text),
            actions=[
                ft.TextButton("Ok", on_click=lambda e: self.close_dlg(e, page),)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

    def close_dlg(self,e, page: ft.Page):
        self.dlg_modal.open = False
        page.update()


    def open_dlg_modal(self,e, page: ft.Page):
        page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        page.update()