# src/gsm/core/config.py

# * clés API
# * constantes métier
# * options de services
# * paramètres de scraping
# * chemins personnalisés
# * règles internes

import flet as ft
from dataclasses import dataclass, field
from gsm.config.window import WindowSettings


@dataclass
class AppSettings:
    name: str = "GSM"
    window: WindowSettings = field(default_factory=WindowSettings)

settings = AppSettings()

if __name__ == "__main__":
    import flet as ft

    def main(page: ft.Page):
                
        settings.window.apply(page)

    # import subprocess
    # subprocess.run(["flet", "run", "src/gsm/helpers/uuu.py"])
