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

    

class Enemy(Entity):
    def __init__(self, name, hp, maxHp, attack, defense):
        super().__init__(name, hp, maxHp, attack, defense)

    def play_turn(self):
        # Logique de l'ennemi pour jouer son tour
        pass

    def __str__(self):
        return f"Enemy {self.name}: HP={self.hp}/{self.maxHp}, Attack={self.attack}, Defense={self.defense}"


class Player(Entity):
    def __init__(self, name, hp, maxHp, attack, defense):
        super().__init__(name, hp, maxHp, attack, defense)
        self.inventory = []

    def check_inventory(self):
        if not self.inventory:
            print(f"{self.name} n'a aucun objet dans son inventaire.")
        else:
            print(f"Inventaire de {self.name}:")
            for item in self.inventory:
                print(f"- {item}")

    def play_turn(self):
        pass

    def use_item(self, item):
        if item in self.inventory:
            if item == "potion":
                self.heal(20)
                print(f"{self.name} a utilisé une potion et a récupéré 20 points de vie.")
                self.inventory.remove(item)
            else:
                print(f"{self.name} n'a pas d'objet utilisable.")
        else:
            print(f"{self.name} n'a pas l'objet '{item}' dans son inventaire.")

    def __str__(self):
        return f"Player {self.name}: HP={self.hp}/{self.maxHp}, Attack={self.attack}, Defense={self.defense}"