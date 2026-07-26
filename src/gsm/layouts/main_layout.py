# src/gsm/layouts/main_layout.py
import flet as ft
from gsm.components.nav_bar import NavBar


class MainLayout:
    """
    Coquille persistante de l'application (header + zone de contenu).

    C'est une "layout route" au sens du Router déclaratif de Flet : elle
    est déclarée comme `component` d'une `ft.Route` qui a des `children`,
    et elle place ses enfants via `ft.use_route_outlet()` — l'équivalent
    exact d'un `<Outlet />` en React Router.
    """

    @staticmethod
    @ft.component
    def view() -> ft.Control:
        outlet = ft.use_route_outlet()

        return ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("gsm", size=20, weight=ft.FontWeight.BOLD),
                            NavBar.view(),
                        ],
                    ),
                    ft.Divider(),
                    ft.Container(content=outlet, expand=True),
                ],
            ),
        )
