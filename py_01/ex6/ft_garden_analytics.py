
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def add_height(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points


class GardenManager:
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


def main():
    print("=== Garden Management System Demo ===")
    print()
    my_garden1 = GardenManager("Alice")
    my_garden2 = GardenManager("hamid")
    my_garden1.add_Plant(Plant("Oak Tree", 100))
    my_garden2.add_Plant(Plant("Oak Tree", 100))
    my_garden1.add_Plant(FloweringPlant("Rose", 25, "red"))
    my_garden1.add_Plant(PrizeFlower("Sunflower", 50, "Yellow", 10))
    print()
    my_garden1.All_Plants_Grow()


if __name__ == "__main__":
    main()
