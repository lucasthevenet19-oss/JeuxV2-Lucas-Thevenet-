class Entity:
    def __init__(self, name, hp, maxHp, attack, defense):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.attack = attack
        self.defense = defense


    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def attack(self, target):
        target.take_damage(self.attack)

    def play_turn(self):
        pass

    def __str__(self):
        return f"{self.name} [PV: {self.hp}/{self.maxHp}]"

    

    