import flet as ft

class OptionButton(ft.TextButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = "#FED466"
        self.content = ft.Text(text, color=ft.colors.BLACK)
        self.width=200,
        self.height=75,
        self.on_click = on_click

class SubmitButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = "#FED466"
        self.color = ft.colors.BLACK
        self.text = text
        self.on_click = on_click
