class ClassKbir:
    def __init__(self):
        self.name = "Class kbir"
    
    class ClassSghir:
        def __init__(self):
            self.name = "Class sghir"
        
        def method(self):
            print("Ana men class sghir")

# Kif testekhdem:
obj_kbir = ClassKbir()
obj_sghir = ClassKbir.ClassSghir()
obj_sghir.method()