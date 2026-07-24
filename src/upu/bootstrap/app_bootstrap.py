# src/upu/bootstrap/app_bootstrap.py

import flet as ft

from upu.app import App

from upu.core.config import settings
# from upu.core.session import Session # * [ ]
# from upu.services.auth_service import AuthService # * [ ]


class AppBootstrap:

    def __init__(self, page: ft.Page):

        self.page=page
        
        settings.window.apply(page)
        
        # self.config = Config()
        # self.session = Session()
        # self.auth_service = AuthService()
    
        self.setup()

    def setup(self):
        
        # self.page.theme = self.config.theme
        # self.page.window.to_front()

        self.page.render(App)
