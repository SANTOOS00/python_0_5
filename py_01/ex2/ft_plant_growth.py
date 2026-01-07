

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        if self.age <= 60:
            self.height += 1
        else:
            self.height += 0.5

    def age_hani(self):
        self.age += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def simulate_week(self):
        tmp = self.height
        print("== Day 1 ==")
        print(self.get_info())
        i = 6
        while i:
            self.age_hani()
            self.grow()
            i -= 1
        print("== Day 7 ==")
        print(self.get_info())
        print(f"Growth this week: +{self.height - tmp}cm")


if __name__ == "__main__":
    data1 = Plant("Rose", 25, 30)
    data1.simulate_week()
