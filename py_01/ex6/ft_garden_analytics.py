
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points


class GardenManager:
    def __init__(self, name_garden):
        self.name_garden = name_garden
        self.Plants = []

    def add_Plant(self, plant):
        self.Plants.append(plant)
        print(f"Added {plant.name} to {self.name_garden} garden")


if __name__ == "__main__":
    my_garden = GardenManager("Alice's")
    my_garden.add_Plant(Plant("Oak Tree", 25))
    my_garden.add_Plant(FloweringPlant("Rose", 25, "red"))
