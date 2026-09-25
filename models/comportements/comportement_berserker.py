from models.comportement import Comportement

class ComportementBerserker(Comportement):

    def agir(self, ennemi) -> str:
        def agir(self, ennemi) -> str:
            if ennemi.hp < ennemi.hp_max * 0.5:
                return "attaque_double"
            return "attaque"