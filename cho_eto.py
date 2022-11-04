'''
class Human:
    height = 170

class Student(Human):
    height = 180
    satiety = 0

class Worker(Human):
    satiety = 100

nick = Student()
john = Worker()
ann = Human()
print('Nick - ', nick.height)
print('John - ', john.height)
print('Nick_satiety - ', nick.satiety)
print('John_satiety - ', john.satiety)
print('Ann_satiety - ', ann.height)
'''

'''
class Grandparent:
    height = 170
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    def __init__(self):
        print('height - ', self.height)
        print('satiety - ', self.satiety)
        print('age - ', self.age)

nick = Child()
'''


'''
class  Wow:
    def __wow(self):
        print('Wow')

    def _hello(self):
        print('Hello')

some_object = Wow()
some_object._hello()

#some_object.__wow() # bude chyba
some_object._Wow__wow()
'''
'''
class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"
    def __init__(self):
        self.world = "World!"
        self._world = "_World!"
        self.__world = "__World!"
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

class Hi(Hello_world):
    def hi_print(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

print()
hello = Hello_world()
hello.printer()

print('Hi')
hi = Hi()
hi.hi_print()
'''

class Hello:
    def __init__(self):
        print('Hello')

class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print("World!")

hello_world = Hello_World()

class Class1:
    var = 20
    def __init__(self):
        self.var = 10

class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)

class_object = Class2()

class Grandparent():
    def about(self):
        print("i am Grandparent.")
    def about_myself(self):
        print('I am GrandParent.')

class Parent(Grandparent):
    def about_myself(self):
        print('I am Parent')

class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()

nick = Child()

class Computer:
    def calculate(self):
        print('Calculating ...')

class Display:
    def display(self):
        print('I display the image on the screen ...')

class SmartPhone(Display, Computer):
    pass

xiaomi = SmartPhone()
xiaomi.calculate()
xiaomi.display()






class Computer:
    def __init__(self,model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128

class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = '4K'

class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)

xiaomi = SmartPhone(model='HP')
xiaomi.print_info()






