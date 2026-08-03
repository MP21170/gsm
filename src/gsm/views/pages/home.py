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
                ft.Text("Squelette d'application Flet déclarative\n\n(Projet francophone collaboratif 'gsm' basé sur Python et Flet (declarative mode - React & Flutter-like)."),
                ft.Text("GH : http://GitHub.com/GrCOTE7/GSM", weight=ft.FontWeight.BOLD),
            ],
        )
