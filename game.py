class Game:
    def __init__(self, player, vague, mongoClient=None):
        self.player = player
        self.vague = vague
        self.mongoClient = mongoClient

    def game_save(self):
        print("Sauvegarde de la game...")

    def game_load(self):
        print("Chargement de la game...")

    def game_lunch (self):
        print("Lancement de la game...")
        self.vague.play_vague()
        print(f"Player {self.player.name} is ready to fight!")


    def game_end(self):
        print("Fin de la game...")
        self.game_save()

    def game_restart(self):
        print("Redémarrage de la game...")
        self.game_load()
        self.game_lunch()   