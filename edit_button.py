import flet as ft

class MyButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = "#FED466"
        self.color = ft.colors.BLACK
        self.text = text
        self.on_click = on_click

        