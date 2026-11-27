import random
from entity import Entity


class Player(Entity):

  def __init__(self, name, hp, attack_power, defense):
    super().__init__(name, hp, hp, attack_power, defense)

  def is_alive(self):
    return self.hp > 0

  def is_ko(self):
    return self.hp <= 0

  def take_damage(self, amount):
    damage_taken = max(1, amount - self.defense)
    self.hp -= damage_taken
    if self.hp < 0:
      self.hp = 0

  def heal(self, amount):
    self.hp += amount
    if self.hp > self.maxHp:
      self.hp = self.maxHp

  def attack_target(self, target):  
    target.take_damage(self.attack_power)

  def check_inventaire(self):
    pass

  def play_turn(self):
    pass

  def item(self, item_name):
    if item_name == "potion":
      self.heal(20)
      print(f"{self.name} a utilisé une potion et a récupéré 20 points de vie.")
    else:
      print(f"{self.name} n'a pas d'objet utilisable.")