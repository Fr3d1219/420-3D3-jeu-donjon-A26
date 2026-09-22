from models.ennemi import Ennemi


class EnnemiAgressif(Ennemi):
    """Attaque à chaque tour, sans exception."""

    def agir(self) -> str:
        return "attaque"
# models/ennemi_defensif.py
from models.ennemi import Ennemi


class EnnemiDefensif(Ennemi):
    """Attaque si ses HP sont au-dessus de 50%, défend sinon."""

    def agir(self) -> str:
        if self.hp < self.hp_max * 0.5:
            return "defend"
        return "attaque"