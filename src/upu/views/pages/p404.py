# src/upu/views/pages/p404.py
import flet as ft

@ft.component
def NotFoundView():
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text("404", size=30),
            ft.Text("Page not found", size=20),
        ],
    )
