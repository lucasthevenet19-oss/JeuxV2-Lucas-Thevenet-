import random
from entity import Entity


class Enemy(Entity):
    def __init__(self, name, health, attack_power, difficulty):
        super().__init__(name, health, health, attack_power, 0)  # defense is set to 0 for enemies
        self.difficulty = difficulty

    def attack(self, target):
        pv_avant = target.hp
        super().attack(target)
        degats = pv_avant - target.hp
        print(f"{self.name} attaque {target.name} et inflige {degats} dégâts.")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} a subi {damage} points de dégâts. Santé restante : {self.hp}.")

    def is_alive(self):
        return self.hp > 0

    def is_ko(self):
        return self.hp <= 0

    def drop_lot(self):
        pass

