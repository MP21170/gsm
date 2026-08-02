# src/gsm/views/pages/about.py
import flet as ft
import os
from ...config.app_env import app_env

class TestPage:
    """Page 4 'Test'."""

    @staticmethod
    @ft.component
    def view() -> ft.Control:
        is_local = app_env.is_local()
        platform = app_env.plateform()
        return ft.Column(
            controls=[
                ft.Text("Test ready.", size=28, weight=ft.FontWeight.BOLD),
                ft.Text(f"{is_local = }", size=16),
                ft.Text(f"{platform = }", size=16),
            ],
        )
