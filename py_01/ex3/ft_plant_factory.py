

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    def print_data(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fren", 15, 120]
    ]
    plants_data = []
    for name, h, a in plants:
        plants_data.append(Plant(name, h, a))
    i = 0
    for _ in plants_data:
        print(f"Created: {plants_data[i].print_data()}")
        i += 1
    print(f"\nTotal plants created: {len(plants_data)}")
