class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, colo):
        super().__init__(name, height, age)
        self.colo = colo
        # Rose (Flower): 25cm, 30 days, red color
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.colo} color")

    def bloom(self):
        if self.age > 10 and self.height > 10:
            print("Rose is blooming beautifully!")
        else:
            print("Rose is not blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, diameter):
        super().__init__(name, height, age)
        self.diameter = diameter
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.diameter} diameter")

    def produce_shade(self):
        self.res = self.height * self.diameter // 320
        print(f"{self.name} provides {self.res} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} {self.nutritional_value}")


def main():
    print("=== Garden Plant Types ===")
    print()
    rose = Flower("Rose", 25, 30, "Red")
    rose.bloom()
    print()
    tulip = Flower("Tulip", 35, 1, "Yellow")
    tulip.bloom()
    print()
    maple = Tree("Maple", 500, 1825, 80)
    maple.produce_shade()
    print()
    oak = Tree("Oak", 500, 50, 120)
    oak.produce_shade()
    print()
    Vegetable("Tomato", 80, 90, "Spring", "rich in Vitamin A")
    print()
    Vegetable("Carrot", 60, 1, "Summer", "high in Vitamin C")


if __name__ == "__main__":
    main()
