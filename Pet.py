class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cat(Pet):
    def __init__(self, name, age):
       super().__init__(name, age)

def Main():

    thePet = Pet("Alaa", 20)
    jess = Cat("Jess", 3)

    print("Is Jess a cat?" + str)