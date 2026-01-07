

class Plant():
    def __init__(self, name):
        self.__name = name
        self.__age = 0
        self.__height = 0
        print(f"Plant created: {self.__name}")

    def set_age(self, age): 
        if (0 <= age):
            if (self.__age < age):
                self.__age = age
                print(f"Age updated: {age} days [OK]")
            else:
                print(f"The plant’s age is {self.__age} days")
                print(
                    "Security: The plant is older than, or the same age as, "
                    "the age I entered"
                )
        else:
            print(f"Invalid operation attempted: age {age} [REJECTED]")
            print("Security: Negative age rejected")

    def set_height(self, height):
        if (0 <= height):
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def get_height(self):
        return f"Plant: {self.__name} ==> height {self.__height}cm"

    def get_age(self):
        return f"Plant: {self.__name} ==> age {self.__age}"

    def statu(self):
        print(f"Current plant: {self.__name} ({self.__height}cm, "
              f"{self.__age})")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    data1 = Plant("Rose")
    data1.set_height(25)
    data1.set_age(30)
    print()
    data1.set_height(-5)
    print()
    data1.statu()