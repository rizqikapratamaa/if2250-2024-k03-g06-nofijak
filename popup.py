import flet as ft
import time

class PopUp:
    def __init__(self,title, text, page: ft.Page):
        self.clicked = False
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(title),
            content=ft.Text(text),
            actions=[
                ft.TextButton("Ok", on_click=lambda e: self.close_dlg(e, page),)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

    def close_dlg(self,e, page: ft.Page):
        self.clicked = True
        self.dlg_modal.open = False
        page.update()


    def open_dlg_modal(self,e, page: ft.Page):
        page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        page.update()

class YesOrNo:
    def __init__(self,text, page: ft.Page):
        self.action = False
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Are you sure?"),
            content=ft.Text(text),
            actions=[
                ft.TextButton("Yes", on_click=lambda e: self.yes(e, page),),
                ft.TextButton("No", on_click=lambda e: self.no(e, page),),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

    def yes(self,e, page: ft.Page):
        self.action = True
        self.dlg_modal.open = False
        print("Yes")
        page.update()

    def no(self,e, page: ft.Page):
        self.action = False
        self.dlg_modal.open = False
        print("No")
        page.update()

    def open_dlg_modal(self,e, page: ft.Page):
        page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        page.update()