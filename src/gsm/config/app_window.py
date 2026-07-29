from dataclasses import dataclass, field
import flet as ft


@dataclass
class AppWindow:
    """Configuration de la fenêtre de l'application."""

    title: str = "GSM App"

    local = 1

    print(local)

    def apply(self, page: ft.Page):
        page.title = self.title
