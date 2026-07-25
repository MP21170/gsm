# src/upu/bootstrap/setup.py
import flet as ft
from upu.core.config import settings
from upu.core.router import route
from upu.app import App

class Setup:

    def __init__(self, page: ft.Page):

        self.page = page
        settings.window.apply(page)
        self.setup()

    def setup(self):
        route(self.page)
        # Route initiale déclarative
        self.page.go("/")
        self.page.render(lambda: App(self.page))

# -------------------------------------------------------

# from upu.core.session import Session # * [ ]
# from upu.services.auth_service import AuthService # * [ ]
        # self.page.theme = self.config.theme
        # self.page.window.to_front()
        # self.config = Config()
        # self.session = Session()
        # self.auth_service = AuthService()

# -------------------------------------------------------