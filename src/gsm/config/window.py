from dataclasses import dataclass, field
import flet as ft


from ..helpers.env import get_env, dv, curr_time
from .app_window import AppWindow
import inspect


@dataclass
class WindowSettings:
    """Position de la fenêtre de l'application sur l'écran, ainsi que sa taille et son comportement."""

    sl = "\n" + "-" * 69

    top: int = 0
    left: int = int(
        str(get_env("GSM_WINDOW_LEFT", 1912))  # 1396
    )  # 840 pour vidéo - 1412 pour un seul écran - Default: 1912 pour 2ème écran
    width: int = 516
    height: int | None = None

    need_cli_below: bool = bool(
        str(get_env("GSM_WINDOW_CLI", False))
    )  # 0 ('défaut) pas de CLI sous la fenêtre - 1 → 300 px de place dessous pour la CLI

    print(f"{curr_time()}", end=" > ")

    print(sl + f"\n{dv(left)} | {dv(width)} | {dv(height)} | {dv(need_cli_below)}" + sl)

    resizable: bool = True

    def __post_init__(self):
        print(dv(self.height))
        if not bool(self.height):
            self.height = 1088 if self.left >= 1912 else 1040

    def apply(self, page: ft.Page):

        page.title = AppWindow.title
        print(dv(self.height))

        if self.left < 1912:
            print("Focus à l'App !")
            self.height = 808
            page.run_task(page.window.to_front)  # ← Pour donner le focus à l'App

        # page.window.height = (
        #     self.height - 300 if not self.need_cli_below else self.height - 300
        # )
        # print(f"{self.height = }")

        if self.height and self.left >= 1912 and self.need_cli_below:
            print("test ok")
            self.width = 540
            self.height = self.height - 300 if self.need_cli_below else self.height
            # print(
            #     f"{self.height - 300} if {str(self.need_cli_below)} else {str(self.height)}"
            # )

        page.window.width = self.width

        # h = self.height-300 if not self.no_need_cli else self.height
        # page.window.height = h

        page.window.top = self.top
        page.window.left = self.left
        page.window.height = self.height

        page.window.resizable = self.resizable

        # print(
        #     self.sl
        #     + f"\nleft = {self.left} | width = {self.width} | height = {self.height} | need_cli_below = {self.need_cli_below}"
        #     + self.sl
        # )
    
        # import inspect
        # print(inspect.iscoroutinefunction(ft.Window.to_front))
        # print(inspect.signature(ft.Window.to_front))

        print(
            {
                "left": page.window.left,
                "width": page.window.width,
                "height": page.window.height,
            }
        )

        page.update()
