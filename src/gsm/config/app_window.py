from dataclasses import dataclass, field
import flet as ft


@dataclass
class AppWindow:
    """Configuration de la fenêtre de l'application."""

    title: str = "GSM App"

    local = 1
    print(f"{local = } (app_window)")

    def apply(self, page: ft.Page):
        page.title = self.title
