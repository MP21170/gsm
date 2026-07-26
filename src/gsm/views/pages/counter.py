# src/gsm/views/pages/counter.py
import flet as ft

from gsm.state.counter_state import CounterState


class CounterPage:
    """Page 'Compteur'."""

    @staticmethod
    @ft.component
    def view() -> ft.Control:
        state, _ = ft.use_state(lambda: CounterState())

        def handle_change(e: ft.Event[ft.TextField]) -> None:
            try:
                state.set_value(int(e.control.value))
            except ValueError:
                pass

        # Annotation explicite indispensable : sans elle, Pylance infère
        # list[IconButton | TextField] à partir des littéraux, non
        # assignable à list[Control] (reportArgumentType).
        controls: list[ft.Control] = [
            ft.IconButton(
                ft.Icons.REMOVE,
                tooltip="Décrémenter",
                on_click=lambda _: state.decrement(),
            ),
            ft.TextField(
                value=str(state.value),
                width=100,
                text_align=ft.TextAlign.CENTER,
                on_change=handle_change,
            ),
            ft.IconButton(
                ft.Icons.ADD,
                tooltip="Incrémenter",
                on_click=lambda _: state.increment(),
            ),
        ]
        return ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=controls)

        # À retenir :
        # list[ft.Control] explicite dès qu'une liste de contrôles mélange plusieurs types concrets.
        # ft.Event[TonControlPrécis] (pas ft.ControlEvent) dès que tu écris une fonction nommée pour un handler, plutôt qu'une lambda.

if __name__ == "__main__":

    def main(page: ft.Page):
        page.title = "Flet counter example"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.render(CounterPage.view)

    ft.run(main)
