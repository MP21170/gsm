# src/upu/core/router.py
import flet as ft
from upu.views.pages.counter import Counter
from upu.views.pages.p404 import NotFoundView

# Routes déclaratives
ROUTES = {
    "/": Counter,
}

def resolve_route(route: str):
    view = ROUTES.get(route)

    if view is None:
        view = NotFoundView

    if callable(view):
        return ft.Container(content=view())
    else:
        return view

def route(page: ft.Page):
    def on_route_change(e):
        page.views.clear()
        page.views.append(resolve_route(page.route))
        page.update()

    page.on_route_change = on_route_change


# ---------------------------------------------

# from upu.views.home import HomeView
# from upu.views.login import LoginView
# from upu.views.settings import SettingsView


# "/", HomeView,
# "/login", LoginView,
# "/settings", SettingsView, auth_required=True,
# "/user/:id", UserView, auth_required=True,
    
    # IMPORTANT :
    # Si la vue est un composant décoré (fonction),
    # on l’instancie et on l’enveloppe dans un contrôle simple.

# ---------------------------------------------

# from dataclasses import dataclass


# @dataclass
# class Route:
#     path: str
#     view: type
#     auth_required: bool = False
#     transition: str = "fade"


# ROUTES = [
#     Route("/", CounterView),
# ]

# import re


# def match_route(route: str):
#     for r in ROUTES:
#         pattern = "^" + re.sub(r":(\w+)", r"(?P<\1>[^/]+)", r.path) + "$"
#         m = re.match(pattern, route)
#         if m:
#             return r, m.groupdict()
#     return None, {}


# def resolve_route(route: str):
#     r, params = match_route(route)

#     if not r:
#         from upu.views.pages.p404 import NotFoundView

#         return NotFoundView()

#     # Instanciation déclarative
#     return r.view(**params) if params else r.view()


# def attach_router(page):

#     def on_route_change(e):
#         page.views.clear()
#         page.views.append(resolve_route(page.route))
#         page.update()

#     page.on_route_change = on_route_change
