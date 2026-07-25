# src/upu/app.py
import flet as ft
from upu.layouts.main_layout import MainLayout

def App(page):
    current_view = page.views[-1]
    return MainLayout()(current_view)

# class App:
#     def __call__(self, page):
#         # La vue courante est celle que le router a mise dans page.views[-1]
#         current_view = page.views[-1]

#         # On enveloppe la vue dans le layout global
#         return MainLayout(current_view)
