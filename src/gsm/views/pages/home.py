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
                ft.Text("Squelette d'application Flet déclarative (Projet francophone collaboratif 'gsm' basé sur Python et Glet (declarative - React & Flutter-like))."),
            ],
        )
