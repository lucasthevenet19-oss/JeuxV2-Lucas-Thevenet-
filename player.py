class Player:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.maxHp = hp
        self.attack = attack
        self.defense = defense

    def est_en_vie(self):
        return self.hp > 0

    def est_ko(self):
        return self.hp <= 0

    def prendre_degats(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def soigner(self, amount):
        self.hp += amount
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def attaquer(self, target):
        target.prendre_degats(self.attack)

    def jouer_tour(self):
        pass
        

    def item(self, item):
        if item == "potion":
            self.soigner(20)
            print(f"{self.name} a utilisé une potion et a récupéré 20 points de vie.")
        else:
            print(f"{self.name} n'a pas d'objet utilisable.")

    def __str__(self):
        return f"Player {self.name}: HP={self.hp}/{self.maxHp}, Attack={self.attack}, Defense={self.defense}"

