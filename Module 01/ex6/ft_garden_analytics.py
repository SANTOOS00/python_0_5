
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
        if self.bloom:
            return f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)"
        else:
            return f"- {self.name}: {self.height}cm, {self.color} flowers (not blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, bloom, points):
        super().__init__(name, height, color, bloom)
        self.points = points
        self.type = 3
    
    def info_prize(self):
        if self.bloom:
            return f"- {self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.points}"
        else:
            return f"- {self.name}: {self.height}cm, {self.color} flowers (not blooming), Prize points: {self.points}"


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

    def Report_garden(self):
        for plant in self.Plants:
            if plant.type == 1:
                print(plant.info_plant())
            elif plant.type == 2:
                print(plant.info_flower())
            else:
                print(plant.info_prize())


def main():
    print("=== Garden Management System Demo ===")
    print()
    my_garden1 = GardenManager("Alice")
    my_garden1.add_Plant(Plant("Oak Tree", 100))
    my_garden1.add_Plant(FloweringPlant("Rose", 25, "red", True))
    my_garden1.add_Plant(PrizeFlower("Sunflower", 50, "Yellow", True, 10))
    print()
    my_garden1.All_Plants_Grow()
    # my_garden1.All_Plants_Grow1()
    my_garden1.Report_garden()


if __name__ == "__main__":
    main()
