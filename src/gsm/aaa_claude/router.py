from __future__ import annotations

import flet as ft

from gsm.layouts.main_layout import MainLayout
from gsm.views.pages.counter import CounterPage
from gsm.views.pages.p404 import NotFoundPage


class AppRouter:
    """
    Table de routes centralisée.

    Depuis Flet 0.85, le routage déclaratif se fait avec `ft.Router` +
    `ft.Route` (inspiré de React Router) : plus besoin de gérer
    `page.on_route_change` / `page.views` à la main comme dans la version
    d'origine, qui mélangeait routage impératif et composants déclaratifs
    (c'était la cause principale du plantage).

    Pour ajouter une page :
        1. Créez sa classe dans `gsm/views/pages/`, avec une `view`
           en `@staticmethod @ft.component`.
        2. Ajoutez une `ft.Route(path="...", component=MaPage.view)`
           dans `routes()` ci-dessous, avant la route "catch-all".
    """

    @staticmethod
    def routes() -> list[ft.Route]:
        return [
            ft.Route(
                # Route "layout" sans `path` : elle englobe toutes les
                # routes filles avec le même MainLayout (header, footer...).
                component=MainLayout.view,
                children=[
                    ft.Route(index=True, component=CounterPage.view),
                    # Ajoutez vos futures routes ici, par exemple :
                    # ft.Route(path="about", component=AboutPage.view),
                    #
                    # Route "catch-all" : doit rester en dernier, elle
                    # capture tout ce qui n'a matché aucune route au-dessus
                    # et reste englobée dans MainLayout (contrairement à
                    # `not_found=` du Router, qui s'affiche hors layout).
                    ft.Route(path=":path*", component=NotFoundPage.view),
                ],
            ),
        ]

    @staticmethod
    @ft.component
    def view() -> ft.Control:
        return ft.SafeArea(content=ft.Router(AppRouter.routes()))
