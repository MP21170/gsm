from dataclasses import dataclass

import flet as ft


@ft.observable
@dataclass
class CounterState:
    """
    État + logique métier du compteur, dans une vraie classe.

    Contrairement à `ft.use_state`, ceci reste un objet mutable normal :
    on appelle ses méthodes directement (`state.increment()`), sans
    setter séparé. `@ft.observable` détecte la mutation d'un attribut et
    déclenche lui-même le re-rendu de tout composant qui l'a lu au
    rendu précédent.

    Avantage POO concret : `CounterState` se teste unitairement, sans
    aucune UI :

        state = CounterState()
        state.increment()
        assert state.value == 1
    """

    value: int = 0

    def increment(self) -> None:
        self.value += 1

    def decrement(self) -> None:
        self.value -= 1

    def set_value(self, value: int) -> None:
        self.value = value
