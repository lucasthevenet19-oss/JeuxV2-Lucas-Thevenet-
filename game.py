class Game:
    def __init__(self, player, vague, mongoClient=None):
        self.player = player
        self.vague = vague
        self.mongoClient = mongoClient

    def game_enregistrer(self):
        print("Sauvegarde de la game...")

    def game_charger(self):
        print("Chargement de la game...")

    def game_lancer(self):
        print("Lancement de la game...")
        self.vague.play_vague()
        print(f"Player {self.player.name} is ready to fight!")

    def game_fin(self):
        print("Fin de la game...")
        self.game_save()

    def game_restart(self):
        print("Redémarrage de la game...")
        self.game_load()
        self.game_lancer()

    