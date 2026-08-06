# src/gsm/views/pages/about.py
import flet as ft

from gsm.helpers.separators import sepa
from gsm.helpers.refs import gh_link, gh_url


class HomePage:
    """Page 'À propos'."""

    @staticmethod
    @ft.component
    def view() -> ft.Control:

        return ft.Column(
            controls=[
                ft.Text("Accueil", size=28, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Application Flet déclarative\n\n'GSM', projet collaboratif francophone basé sur Python et Flet (Declarative mode - React & Flutter-like)."
                ),
                sepa(),
                ft.Text(
                    f"Pour participer au projet : GH ! {gh_url}",
                    weight=ft.FontWeight.BOLD,
                ),
                gh_link(),
            ],
        )
