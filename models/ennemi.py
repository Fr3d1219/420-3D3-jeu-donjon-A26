from random import random
from models.comportement import Comportement

class Ennemi:
    def __init__(self, nom: str, hp: int, attaque: int, comportement: Comportement):
        self.nom = nom
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque
        self._comportement = comportement  # Objet qui hérite de Comportement
                                          # Objet de type Comportement

    def agir(self):
       return self.comportement.agir() # <- Délégation

    def recevoir_degats(self, degats):
        self.hp = max(0, self.hp - degats)

    def est_vivant(self):
        return self.hp > 0

    def set_comportement(self, comportement: Comportement) -> None:
        self._comportement = comportement       # ← remplacement

    def get_comportement(self) -> Comportement:
        return self._comportement 