# src/upu/core/config.py

# * clés API
# * constantes métier
# * options de services
# * paramètres de scraping
# * chemins personnalisés
# * règles internes

from dataclasses import dataclass, field
import flet as ft


@dataclass
class WindowSettings:
    title: str = "UPU"

    top: int = 0
    left: int = 1412  # Écran : 1 → 1412 | 2 → 1912

    width: int = 516
    height: int | None = None

    resizable: bool = True

    def __post_init__(self):
        if self.height is None:
            self.height = 1088 if self.left >= 1912 else 1040

    def apply(self, page: ft.Page):
        page.title = self.title

        page.window.top = self.top
        page.window.left = self.left

        page.window.width = self.width
        page.window.height = self.height

        page.window.resizable = self.resizable

        # page.run_task(page.window.to_front) # ← Pour donner le focus à l'App
        # import inspect
        # print(inspect.iscoroutinefunction(ft.Window.to_front))
        # print(inspect.signature(ft.Window.to_front))

        page.update()


@dataclass
class AppSettings:

    name: str = "UPU"
    window: WindowSettings = field(default_factory=WindowSettings)


settings = AppSettings()


if __name__ == "__main__":
    import flet as ft
    import subprocess

    def main(page: ft.Page):
        settings.window.apply(page)

    # subprocess.run(["flet", "run", "src/upu/helpers/uuu.py"])
    print("oki 21")
