# src/gsm/views/pages/counter.py
from __future__ import annotations

import flet as ft


class CounterPage:
    """
    Page 'Compteur'.

    IMPORTANT : les hooks Flet (`ft.use_state`, `ft.use_effect`, ...) ne
    fonctionnent que sur des fonctions "pures" appelées à chaque rendu —
    exactement comme les Hooks React, qui ne fonctionnent pas non plus dans
    des classes. On ne peut donc pas décorer une méthode liée (`self.xxx`)
    avec `@ft.component` et y utiliser `use_state` de façon fiable.

    Le compromis le plus propre pour rester proche de la POO tout en
    respectant cette contrainte : une classe sert de *namespace* et
    regroupe la logique de la page, mais le composant lui-même est une
    `staticmethod` (donc une fonction "nue" aux yeux de Flet).
    """

    @staticmethod
    @ft.component
    def view() -> ft.Control:
        count, set_count = ft.use_state(0)

        def handle_decrement(_: ft.ControlEvent) -> None:
            set_count(count - 1)

        def handle_increment(_: ft.ControlEvent) -> None:
            set_count(count + 1)

        def handle_change(e: ft.ControlEvent) -> None:
            # L'utilisateur peut taper une valeur invalide/vide pendant la
            # saisie : on ignore simplement ces états intermédiaires au
            # lieu de planter comme dans la version d'origine.
            try:
                set_count(int(e.control.value))
            except ValueError:
                pass

        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(
                    ft.Icons.REMOVE,
                    tooltip="Décrémenter",
                    on_click=handle_decrement,
                ),
                ft.TextField(
                    value=str(count),
                    width=100,
                    text_align=ft.TextAlign.CENTER,
                    on_change=handle_change,
                ),
                ft.IconButton(
                    ft.Icons.ADD,
                    tooltip="Incrémenter",
                    on_click=handle_increment,
                ),
            ],
        )


if __name__ == "__main__":

    def main(page: ft.Page):
        page.title = "Flet counter example"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.render(Counter)

    ft.run(main)
