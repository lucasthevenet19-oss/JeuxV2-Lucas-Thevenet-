class Entity:
    def __init__(self, name, hp, maxHp, attack, defense):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.attack = attack
        self.defense = defense

    def est_en_vie(self):
        return self.hp > 0

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

    def __str__(self):
        return f"{self.name} [PV: {self.hp}/{self.maxHp}]"

    