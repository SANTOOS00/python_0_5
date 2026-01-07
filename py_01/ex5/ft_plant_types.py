
class Plant():
    def __init__(self, name, height, age):
        self._name = name
        if 0 <= height:
            self._height = height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            self._height = -1
        if 0 <= age:
            self._age = age
        else:
            print(f"Invalid operation attempted: height {age}cm [REJECTED]")
            print("Security: Negative age rejected")
            self._age = -1
class Flower(Plant):
    def __init__(self, name, height, age , color):
        super().__init__(name, height, age)
        self._color = color
        if (self._height == -1):
            return
        if (self._age == -1):
            return
        print (f"{self._name} (Flower): {self._height}cm, {self._age} dyas, {self._color} color")
        if self._age >= 20 and self._height >= 20:
            print ("Rose is blooming beautifully!")
        else:
            print("Rose is too young to bloom.")
class Tree(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
        if (self._height == -1):
            return
        if (self._age == -1):
            return
        self._trunk_diameter = (self._age // 365) * 10
        res = (self._height * self._trunk_diameter) // 320
        print (f"{self._name} (Tree): {self._height}cm, {self._age} dyas, {self._trunk_diameter} diameter")
        print (f"{self._name} provides {res} square meters of shade")

        
class Vegetable(Plant):
    def __init__(self,name ,height, age):
        super().__init__(name, height , age)
        if (self._age == -1):
            return
        if (self._height == -1):
            return
        if (age >= 60 and age <= 120):
            self._harvest = "summer harvest"
        else:
            self._harvest = "not ready"
        print (f"{self._name} (Vagetable): {self._height}cm, {self._age} dyas, {self._harvest}")
        if (self._age >= 60 and self._age <= 120 and self._height >= 50):
            print (f"{name} is rich in vitamin C")
        elif (self._age > 120):
            print(f"{name} harvest season has passed")
        elif (self._age < 60):
            print (f"{name} is too young to harvest")
if __name__ == "__main__":
    print ("=== Garden Plant Types ===")
    print()
    Flower("Rose", 25, 30, "red")
    print ()
    Tree("Oak", 500, 1825)
    print ()
    Vegetable("Tomato", 80, 130)