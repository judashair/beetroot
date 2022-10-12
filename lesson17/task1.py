class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("You have to choose subclass at first!")


class Dog(Animal):
    def talk(self):
        print("Woof")


class Cat(Animal):
    def talk(self):
        print("Meow")


pets = [Dog("Jack"), Cat("Milla"), Dog("Mike")]
for pet in pets:
    pet.talk()

    
