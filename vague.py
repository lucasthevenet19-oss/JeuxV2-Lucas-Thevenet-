class vague:
    def __init__(self, vague_actuel):
        self.vague_actuel = vague_actuel
        self.monsters = []  # <--- Le point manquait ici

    def pick_enemies(self, monsters_list: list):
        self.monsters = monsters_list

    def jouer_vague(self):
        print(f"Starting wave {self.vague_actuel} with {len(self.monsters)} monsters.")

    def difficulté(self):
        return sum(monster.difficulty for monster in self.monsters)

    def __str__(self):
        return f"Wave {self.vague_actuel} with {len(self.monsters)} monsters."


