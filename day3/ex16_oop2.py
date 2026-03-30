# 객체지향 클래스



class Dog:
    def __init__(self, name): # 생성자
        self.name = name
    def bark(self):
        print(self.name)


poppy = Dog('뽀삐')

poppy.bark()

