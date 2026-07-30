from dataclasses import dataclass, field
import flet as ft
import os, platform

@dataclass
class AppWindow:
    """Configuration de la fenêtre de l'application."""

    # On définit le titre de base
    title: str = "GSM App"

    # field(init=False) permet de ne pas demander ces variables lors du AppWindow()
    is_dev: bool = field(init=False)

    # * [ ] use platform
    
    # XXX L_ marcha pas :-(
    print('Oki')
    
    def __post_init__(self):
        """S'exécute automatiquement JUSTE APRÈS la création de l'objet."""
        # 1. Détection de l'environnement au moment de l'instanciation
        self.is_dev = os.getenv("DEV") == "1"
        print(f"{self.is_dev = } (__post_init__ app_window)")

        # 2. Modification du titre de cette instance précise
        if self.is_dev:
            self.title = f"L_{self.title}"

    def apply(self, page: ft.Page):
        """Applique la configuration à la page Flet (À APPELER DANS MAIN)."""
        page.title = self.title
        print(f"{self.is_dev = } (apply app_window)")
        
