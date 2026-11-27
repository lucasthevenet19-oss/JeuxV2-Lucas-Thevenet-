import random
from player import Player
from vague import Vague


class Game:

    def __init__(self, player, vague, mongoClient=None):
        self.player = player
        self.vague = vague
        self.mongoClient = mongoClient

    def game_save(self):
        print("Sauvegarde de la game...")

    def game_load(self):
        print("Chargement de la game...")

    def game_launch(self):  
        print("Lancement de la game...")

    
    if self.vague and hasattr(self.vague, "monsters") and len(self.vague.monsters) > 0:
        self.vague.play_vague()
        print(f"Player {self.player.name} is ready to fight!")
    else:
        print("Attention : La vague est vide ou non initialisée !")

    def game_end(self):
        print("Fin de la game...")
        self.game_save()

    def game_restart(self):
        print("Redémarrage de la game...")
        self.game_load()
        self.game_launch()

