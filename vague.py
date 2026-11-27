import random
from ennemy import Enemy


class Vague:

  def __init__(self, vague_actuel):
    self.vague_actuel = vague_actuel
    self.monsters = []

  def pick_enemies(self, monsters_list: list):
    self.monsters = monsters_list

  def play_vague(self):  # Corrigé pour correspondre à game.py
    print(f"Starting wave {self.vague_actuel} with {len(self.monsters)} monsters.")
    
    # Sécurité anti-plantage si aucun monstre n'est présent
    if not self.monsters:
      print("Aucun monstre dans cette vague !")
      return

  def get_difficulty(self):
    return sum(monster.difficulty for monster in self.monsters)