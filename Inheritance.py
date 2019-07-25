class Animal:

    def __init__(self, color, is_pet):
        self.color = color
        self.is_pet = is_pet

    def eat(self):
        print("Animal is eating...")
    
    def speak(self):
        print("Animal is speaking")


class Dog(Animal):
    
    def __init__(self, color, name):
        print("Dog __init__")
        Animal.__init__(self, color, True)
        self.name = name

    def bark(self):
        print("Dog is barking")

    def display(self):
        print("Name: {}".format(self.name))
        print("Color: {}".format(self.color))
        print("Is pet: {}".format(self.is_pet))


class Lion(Animal):

    def __init__(self, color, place):
        Animal.__init__(self, color, False)
        self.place = place

    def display(self):
        print("Place: {}".format(self.place))
        print("Color: {}".format(self.color))
        print("Is pet: {}".format(self.is_pet))

    def roar(self):
        print("Lion is roaring...")
    

tommy = Dog("Brown", "Tommy")
tommy.display()

tommy.eat()
tommy.bark()

lion = Lion("Yellow", "Africa")
lion.display()
lion.eat()
lion.roar()
