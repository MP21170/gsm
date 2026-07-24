# src/upu/views/simple_declarative_counter.py
import flet as ft

@ft.component
def Counter():
    count, set_count = ft.use_state(0)

    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.IconButton(
                ft.Icons.REMOVE,
                on_click=lambda e: set_count(count - 1),
            ),
            ft.TextField(
                value=str(count),
                width=100,
                text_align=ft.TextAlign.CENTER,
                on_change=lambda e: set_count(int(e.control.value)),
            ),
            ft.IconButton(
                ft.Icons.ADD,
                on_click=lambda e: set_count(count + 1),
            ),
        ],
    )

if __name__ == "__main__":

    def main(page: ft.Page):
        page.title = "Flet counter example"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.render(Counter)

    ft.run(main)
