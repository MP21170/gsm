# src/gsm/bootstrap/setup.py
import flet as ft

from gsm.core.config import settings
from gsm.app import App


class Setup:
    """
    Point d'amorçage de la session Flet.

    `ft.run(Setup)` fonctionne car une classe est un *callable* en Python :
    `Setup(page)` est équivalent à `Setup.__init__(instance, page)`, ce qui
    respecte exactement le contrat attendu par `ft.run` (une fonction
    `(page: ft.Page) -> None`, sync ou async).

    Toute la configuration impérative (fenêtre, thème...) se fait ici, une
    seule fois par session ; le reste de l'app est 100% déclaratif.
    """

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        settings.window.apply(page)

        # Rendu déclaratif de l'arbre de composants. `App.view` est passé
        # par référence (pas appelé : pas de parenthèses) — c'est Flet qui
        # se charge de l'invoquer et de le ré-invoquer à chaque changement
        # d'état. Le routeur interne lit `page.route` tout seul : plus
        # besoin d'un `page.go("/")` explicite ni de `page.on_route_change`.
        page.render(App.view)


# -------------------------------------------------------

# from gsm.core.session import Session # * [ ]
# from gsm.services.auth_service import AuthService # * [ ]
# self.page.theme = self.config.theme
# self.page.window.to_front()
# self.config = Config()
# self.session = Session()
# self.auth_service = AuthService()

# -------------------------------------------------------
