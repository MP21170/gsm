# src/upu/core/config.py

# * clés API
# * constantes métier
# * options de services
# * paramètres de scraping
# * chemins personnalisés
# * règles internes

from dataclasses import dataclass, field
import flet as ft

from ..helpers.get_env import get_env


@dataclass
class WindowSettings:
    title: str = "UPU"

    top: int = 0
    left: int = int(
        str(get_env("UPU_WINDOW_LEFT", 1412))
    )  # 840 pour vidéo - 1412 pour un seul écran - Default: 1912 pour 2ème écran

    width: int = 516
    height: int | None = None

    resizable: bool = True

    def __post_init__(self):
        if self.height is None:
            self.height = 1088 if self.left >= 1912 else 1040

    def apply(self, page: ft.Page):
        page.title = self.title

        if self.left == 840:
            print("Focus à l'App !")
            self.height = 808
            page.run_task(page.window.to_front)  # ← Pour donner le focus à l'App

        page.window.top = self.top
        page.window.left = self.left

        page.window.width = self.width
        page.window.height = self.height

        page.window.resizable = self.resizable

        # import inspect
        # print(inspect.iscoroutinefunction(ft.Window.to_front))
        # print(inspect.signature(ft.Window.to_front))

        page.update()

        print(
            {
                "left": self.left,
                "width": self.width,
                "top": self.top,
                "height": self.height,
            }
        )


@dataclass
class AppSettings:

    name: str = "UPU"
    window: WindowSettings = field(default_factory=WindowSettings)


settings = AppSettings()


if __name__ == "__main__":
    import flet as ft

    def main(page: ft.Page):
        settings.window.apply(page)

    # import subprocess
    # subprocess.run(["flet", "run", "src/upu/helpers/uuu.py"])
