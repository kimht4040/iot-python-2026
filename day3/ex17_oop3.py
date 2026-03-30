# 상속

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("fjfkdjf")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} 멍멍")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} 냐옹")


poppy = Dog("뽀삐")

kitty = Cat("나비")

poppy.speak()
kitty.speak()