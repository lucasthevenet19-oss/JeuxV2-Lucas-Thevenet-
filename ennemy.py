class Enemy: 
    def __init__(self, name, health, attack_power, difficulty):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.difficulty = difficulty

    def attack(self, target):
        print(f"{self.name} attaque {target.name} avec une puissance de {self.attack_power}.")
      

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} a subi {damage} points de dégâts. Santé restante : {self.health}.")

    def is_alive(self):
        return self.health > 0

    def is_ko(self):
        return self.health <= 0