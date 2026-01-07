
class Plant():
    def __init__(self, name, height, age):
        self.__name = name
        if 0 <= height:
            self.__height = height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            self.__height = -1
        if 0 <= age:
            self.__age = age
        else:
            print(f"Invalid operation attempted: height {age}cm [REJECTED]")
            print("Security: Negative age rejected")
            self.__age = -1

    def get_m(self):
        return self.__name

    def get_g(self):
        return self.__age
    
    def get_h(self):
        return self.__height


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.__color = color
        if self.get_h() == -1 or self.get_g() == -1:
            return
        print(
            f"{self.get_m()} (Flower): {self.get_h()}cm," 
            f"{self.get_g()} dyas, {self.__color} color"
        )
        if self.get_g() >= 20 and self.get_h() >= 20:
            print("Rose is blooming beautifully!")
        else:
            print("Rose is too young to bloom.")


class Tree(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
        if self.get_h() == -1 or self.get_g() == -1:
            return
        self.__trunk = (self.get_g() // 365) * 10
        res = (self.get_h() * self.__trunk) // 320
        print(
            f"{self.get_m()} (Tree): {self.get_h()}cm," 
            f"{self.get_g()} dyas, {self.__trunk} diameter"
        )
        print(f"{self.get_m()} provides {res} square meters of shade")

        
class Vegetable(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
        if self.get_h() == -1 or self.get_g() == -1:
            return
        if (age >= 60 and age <= 120):
            self.__harvest = "summer harvest"
        else:
            self.__harvest = "not ready"
        print(
            f"{self.get_m()} (Vagetable): {self.get_h()}cm, "
            f"{self.get_g()} dyas, {self.__harvest}"
        )
        if self.get_g() >= 60 and self.get_g() <= 120 and self.get_h() >= 50:
            print(f"{name} is rich in vitamin C")
        elif (self.get_g() > 120):
            print(f"{name} harvest season has passed")
        elif (self.get_g() < 60):
            print(f"{name} is too young to harvest")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    Flower("Rose", 25, 30, "red")
    print()
    Tree("Oak", 500, 1825)
    print()
    Vegetable("Tomato", 80, 90)
