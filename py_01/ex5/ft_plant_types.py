

class Plant():
    def __init__(self, name, height, age):
        self._name = name
        if 0 <= height:
            self._height = height
        else:
            print(f"Invalid operation attempted: height {hright}cm [REJECTED]")
            print("Security: Negative height rejected")
        if 0 <= age:
            self._age = age
        else:
            print(f"Invalid operation attempted: height {age}cm [REJECTED]")
            print("Security: Negative age rejected")
        
class Plants(Plant):
    def __init__(self, name, height, age , color, ):
        super().__init__(name, height, age)
        self._color = color

    def bloom(self):
        print (f"{self._name} (Flower): {self._height}cm, {self._age} dyas, {self._color} color")
        if self._age >= 20 and self._height >= 20:
            print ("Rose is blooming beautifully!")
        else:
            print("Rose is too young to bloom.")
    # def produce_shade(self):
    #     self.__trunk_diameter = (self.__age // 365) * 10
    # def Vagetable(self):



if __name__ == "__main__":
    print ("=== Garden Plant Types ===")
    print()
    data1 = Plants("Rose", 25, 30, "red")

    data1.bloom()



   