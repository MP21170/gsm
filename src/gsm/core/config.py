# src/gsm/core/config.py

# * clés API
# * constantes métier
# * options de services
# * paramètres de scraping
# * chemins personnalisés
# * règles internes

from dataclasses import dataclass, field
import flet as ft

from ..helpers.env import get_env


@dataclass
class WindowSettings:
    
    
    
    title: str = "gsm"

    top: int = 0
    left: int = int(
        str(get_env("gsm_WINDOW_LEFT", 1412))
    )  # 840 pour vidéo - 1412 pour un seul écran - Default: 1912 pour 2ème écran

    need_cli_below: int = int(
        get_env("GSM_WINDOW_CLI", 1) or 1
    )  # 0 ('défaut) pas de CLI sous la fenêtre - 1 → 300 px de place dessous pour la CLI

    # print(f"{need_cli_below= }")

    width: int = 516
    height: int | None = None

    resizable: bool = True

    def __post_init__(self):
        if self.height is None:
            self.height = 1088 if self.left >= 1912 else 1040

    def apply(self, page: ft.Page):
        page.title = self.title

        if self.left < 1912:
            print("Focus à l'App !")
            self.height = 808
            page.run_task(page.window.to_front)  # ← Pour donner le focus à l'App

        page.window.top = self.top
        page.window.left = self.left

        page.window.width = self.width

        # page.window.height = (
        #     self.height - 300 if not self.need_cli_below else self.height - 300
        # )
        # print(f"{self.height = }")

        print(
            f"{self.height-300} if {str(self.need_cli_below)} else {str(self.height)}"
        )
        page.window.height = self.height - 300 if self.need_cli_below else self.height
        # print("WINDOW INIT STATE:", page.window.height)

        # h = self.height-300 if not self.no_need_cli else self.height
        # page.window.height = h

        page.window.resizable = self.resizable

        page.update()

        # import inspect
        # print(inspect.iscoroutinefunction(ft.Window.to_front))
        # print(inspect.signature(ft.Window.to_front))

        print(
            {
                "left": page.window.left,
                "width": page.window.width,
                "top": page.window.top,
                "height": page.window.height,
            }
        )


@dataclass
class AppSettings:

    name: str = "gsm"
    window: WindowSettings = field(default_factory=WindowSettings)


settings = AppSettings()


if __name__ == "__main__":
    import flet as ft

    def main(page: ft.Page):
        settings.window.apply(page)

    # import subprocess
    # subprocess.run(["flet", "run", "src/gsm/helpers/uuu.py"])
