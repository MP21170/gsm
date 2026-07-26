# src/gsm/app.py
import flet as ft

from gsm.core.router import AppRouter


class App:
    """
    Composant racine de l'application.

    Volontairement fin pour l'instant : il délègue tout au routeur. C'est
    l'endroit où brancher plus tard des providers globaux (thème,
    contexte d'authentification via `ft.create_context`, etc.) sans
    toucher au reste de l'arborescence.
    """

    @staticmethod
    @ft.component
    def view() -> ft.Control:
        return AppRouter.view()
