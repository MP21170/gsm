"""
Configuration de l'application.

NOTE : ce fichier n'était pas fourni dans le code d'origine (seul son usage
`settings.window.apply(page)` l'était). Ce qui suit est une implémentation
minimale et fonctionnelle pour que le projet tourne tel quel. Si vous avez
déjà votre propre `core/config.py`, gardez-le : seule la méthode
`apply(page)` doit exister sur l'objet exposé par `settings.window`.
"""

from __future__ import annotations

from dataclasses import dataclass

import flet as ft


@dataclass(frozen=True)
class WindowSettings:
    """Paramètres de la fenêtre applicative (desktop)."""

    title: str = "gsm"
    width: int = 900
    height: int = 650
    resizable: bool = True
    theme_mode: ft.ThemeMode = ft.ThemeMode.LIGHT

    def apply(self, page: ft.Page) -> None:
        """Applique ces paramètres à la Page Flet fournie."""
        page.title = self.title
        page.theme_mode = self.theme_mode
        # page.window n'a d'effet que sur les cibles desktop ; il est
        # silencieusement ignoré sur le web, donc aucun test de plateforme
        # n'est nécessaire ici.
        page.window.width = self.width
        page.window.height = self.height
        page.window.resizable = self.resizable


@dataclass(frozen=True)
class Settings:
    """Point d'entrée unique pour toute la configuration de l'app."""

    window: WindowSettings = WindowSettings()


settings = Settings()
