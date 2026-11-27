import random

class Item:
    def __init__(self, name: str, description: str, dropRate: int, rarity: str, item_type: str, stats: dict = None):
        self.name = name
        self.description = description
        self.dropRate = dropRate
        self.rarity = rarity
        self.item_type = item_type
        self.stats = stats if stats is not None else {}  

    def Use(self, target):
        print(f"{self.name} est utilisé sur {target.name}.")

    def GetStats(self):
        return self.stats


