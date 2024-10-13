import flet as ft



class Application():
    def __init__(self,page=ft.Page):
        self.page=page
        self.page.add(ft.SafeArea(ft.Text("Kill Me please")))
def start_app(page: ft.Page):
    app=Application(page)


ft.app(target=start_app)