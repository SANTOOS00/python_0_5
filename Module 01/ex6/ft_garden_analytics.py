
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.type = 1

    def add_height(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def info_plant(self):
        return f"- {self.name}: {self.height}cm"

class FloweringPlant(Plant):
    def __init__(self, name, height, color, bloom):
        super().__init__(name, height)
        self.color = color
        self.type = 2
        self.bloom = bloom

    def info_flower(self):
        return f"- {self.name}: {self.height}cm, {self.color} flowers ({self.bloom})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, bloom, points):
        super().__init__(name, height, color, bloom)
        self.points = points
        self.type = 3
    
    def info_prize(self):
        return f"- {self.name}: {self.height}cm, {self.color} flowers ({self.bloom}), Prize points: {self.points}"


class GardenManager:
    class GardenStats:
    
    def __init__(self, owner):
        self.owner = owner
        self.Plants = []

    def add_Plant(self, plant):
        self.Plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def All_Plants_Grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for Plant in self.Plants:
            Plant.add_height()

    def Report(self):
        print(f"=== {self.owner}'s Garden Report ===")

def main():
    print("=== Garden Management System Demo ===")
    print()
    my_garden1 = GardenManager("Alice")
    my_garden1.add_Plant(Plant("Oak Tree", 100))
    my_garden1.add_Plant(FloweringPlant("Rose", 25, "red", "blooming"))
    my_garden1.add_Plant(PrizeFlower("Sunflower", 50, "Yellow", "blooming", 10))
    print()
    my_garden1.All_Plants_Grow()
    # my_garden1.All_Plants_Grow1()
    my_garden1.Report()


if __name__ == "__main__":
    main()
