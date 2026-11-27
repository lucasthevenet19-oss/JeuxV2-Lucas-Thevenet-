class Player:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.maxHp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def is_ko(self):
        return self.hp <= 0

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

    def check_inventaire(self):
        pass

    def play_turn(self):
        pass


    def item(self, item):
        if item == "potion":
            self.soigner(20)
            print(f"{self.name} a utilisé une potion et a récupéré 20 points de vie.")
        else:
            print(f"{self.name} n'a pas d'objet utilisable.")

    def __str__(self):
        return f"Player {self.name}: HP={self.hp}/{self.maxHp}, Attack={self.attack}, Defense={self.defense}"

