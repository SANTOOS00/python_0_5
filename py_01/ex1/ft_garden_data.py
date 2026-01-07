

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_data(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    data1 = Plant("Rose", 25, 30)
    data2 = Plant("Sunflower", 80, 45)
    data3 = Plant("Cactus", 15, 120)

    data1.print_data()
    data2.print_data()
    data3.print_data()
