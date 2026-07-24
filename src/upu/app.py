# src/upu/app.py

import flet as ft

# from upu.layouts.main_layout import MainLayout
from upu.views.simple_declarative_counter import Counter

@ft.component
def App():

    return Counter()
