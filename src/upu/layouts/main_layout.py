# src/upu/layouts/main_layout.py
import flet as ft

class MainLayout:
    def __call__(self, content):
        return ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Text("UPU — Minimal Layout", size=20, weight="bold"),
                    ft.Divider(),
                    # ft.Container(content=content),
                ],
            ),
        )
