class Entity: 
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def attack(self, other_entity):
        if self.is_alive():
            other_entity.take_damage(self.attack_power)

    def __str__(self):
        return f"{self.name}: Health = {self.health}, Attack Power = {self.attack_power}"

class Player(Entity):
    def __init__(self, name, health, attack_power, level):
        super().__init__(name, health, attack_power)
        self.level = level

    def __str__(self):
        return f"{super().__str__()}, Level = {self.level}"

class Enemy(Entity):
    def __init__(self, name, health, attack_power, difficulty):
        super().__init__(name, health, attack_power)
        self.difficulty = difficulty

    def __str__(self):
        return f"{super().__str__()}, Difficulty = {self.difficulty}"

class Character(Entity):
    def __init__(self, name, health, attack_power, role):
        super().__init__(name, health, attack_power)
        self.role = role

    def __str__(self):
        return f"{super().__str__()}, Role = {self.role}"

class Item(Entity):
    def __init__(self, name, health, attack_power, item_type):
        super().__init__(name, health, attack_power)
        self.item_type = item_type

    def __str__(self):
        return f"{super().__str__()}, Item Type = {self.item_type}"
