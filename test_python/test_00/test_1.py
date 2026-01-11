# -----------------------------
# Classes
# -----------------------------
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.owner = None

    def info_plant(self):
        # Plant base info
        return f"- {self.name}: {self.height}cm"

class Flower(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def info_plant(self):
        return f"- {self.name}: {self.height}cm, {self.color} flowers ({'blooming' if self.blooming else 'not blooming'})"

class PrizeFlower(Flower):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def info_plant(self):
        return f"- {self.name}: {self.height}cm, {self.color} flowers ({'blooming' if self.blooming else 'not blooming'}), Prize points: {self.prize_points}"

# -----------------------------
# Owner
# -----------------------------
class Owner:
    all_owners = []

    def __init__(self, name):
        self.name = name
        self.plants = []
        Owner.all_owners.append(self)

    def add_plant(self, plant):
        self.plants.append(plant)
        plant.owner = self

    class Stats:
        @classmethod
        def total_height(cls):
            total = 0
            for owner in Owner.all_owners:
                for plant in owner.plants:
                    total += plant.height
            return total

# -----------------------------
# Main test
# -----------------------------
alice = Owner("Alice")

oak = Plant("Oak Tree", 100)
rose = Flower("Rose", 25, "red")

alice.add_plant(oak)
alice.add_plant(rose)

# -----------------------------
# 1️⃣ Print info for all plants (loop only)
# -----------------------------
for owner in Owner.all_owners:
    for plant in owner.plants:
        print(plant.info_plant())

print("Total height:", Owner.Stats.total_height())
