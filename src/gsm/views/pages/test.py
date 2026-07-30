# src/gsm/views/pages/about.py
import flet as ft


class TestPage:
    """Page 4 'Test'."""

    @staticmethod
    @ft.component
    def view() -> ft.Control:
        return ft.Column(
            controls=[
                ft.Text("Test ready.", size=28, weight=ft.FontWeight.BOLD),
            ],
        )
