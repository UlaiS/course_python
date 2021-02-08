class Animal:
    def __init__(self, name, onomatopoeia):
        self.name = name
        self.onomatopoeia = onomatopoeia

    def greeting(self):
        print("My name is ", self.name, " I'am a ", self.type, " and the sound it produces is a ", self.onomatopoeia)


class Dog(Animal):
    type = "Dog"

    def __init__(self, name, onomatopoeia):
        Animal.__init__(self, name, onomatopoeia)
        print("I am an extended dog")


class Cat(Animal):
    type = "Cat"

    def __init__(self, name, onomatopoeia):
        super().__init__(name, onomatopoeia)
        print("I'm an instantiated cat")


class Bird(Animal):
    type = "Bird"


