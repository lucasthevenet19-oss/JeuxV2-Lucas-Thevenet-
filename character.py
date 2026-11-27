class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.maxHp = hp  # Utile pour les soins
        self.attack = attack
        self.defense = defense

    def attack_target(self, target):
        # Utilise la formule de dégâts de ton main.py en tenant compte de la défense
        damage = max(self.attack - target.defense, 1)
        target.take_damage(damage)
        print(f"{self.name} attaque {target.name} et inflige {damage} dégâts !")

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} prend {amount} dégâts ! PV restants : {self.hp}")

    def __str__(self):
        return f"{self.name} [HP: {self.hp}/{self.maxHp}, ATK: {self.attack}, DEF: {self.defense}]"

