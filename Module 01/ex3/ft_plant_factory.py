

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_data(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"


def main():
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fren", 15, 120)
    ]
    for data in plants:
        print(f"Created: {data.print_data()}")
    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()
