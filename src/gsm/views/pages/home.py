# src/gsm/views/pages/about.py
import flet as ft


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
                ft.Text(
                    "Pour participer au projet : GH ! http://GitHub.com/GrCOTE7/GSM",
                    weight=ft.FontWeight.BOLD,
                ),
            ],
        )
