

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_data(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main():
    print("=== Garden Plant Registry ===")
    data1 = Plant("Rose", 25, 30)
    data2 = Plant("Sunflower", 80, 45)
    data3 = Plant("Cactus", 15, 120)

    print(data1.print_data())
    print(data2.print_data())
    print(data3.print_data())


if __name__ == "__main__":
    main()
