# 1. O'quvchi va o'qituvchi
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Salom")

class Pupil(Person):
    pass

class Teacher(Person):
    pass

pupil = Pupil("Ali", 12)
teacher = Teacher("Mr. Smith", 35)
pupil.greet()
teacher.greet()


# 2. Avtomobil va velosiped
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("Harakatlanmoqda")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

car = Car("BMW")
bike = Bike("Giant")
car.move()
bike.move()


# 3. Kitoblar va jurnallar
class Publication:
    def __init__(self, title):
        self.title = title

    def read(self):
        print("O'qilyapti")

class Book(Publication):
    pass

class Magazine(Publication):
    pass

book = Book("Python Programming")
magazine = Magazine("Tech News")
book.read()
magazine.read()


# 4. Hayvonlar
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Tovush chiqardi")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog("Bobik")
cat = Cat("Murka")
dog.make_sound()
cat.make_sound()


# 5. Xodimlar
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        print("Ishlayapman")

class Manager(Employee):
    pass

class Worker(Employee):
    pass

manager = Manager("John", "Manager")
worker = Worker("Alice", "Worker")
manager.work()
worker.work()


# 6. Sportchilar
class Athlete:
    def __init__(self, name):
        self.name = name

    def compete(self):
        print("Musobaqada ishtirok etyapman")

class FootballPlayer(Athlete):
    pass

class BasketballPlayer(Athlete):
    pass

football_player = FootballPlayer("Ronaldo")
basketball_player = BasketballPlayer("LeBron")
football_player.compete()
basketball_player.compete()


# 7. Dasturlash tillari
class Language:
    def __init__(self, name):
        self.name = name

    def code(self):
        print(f"{self.name} bilan kod yozilyapti")

class Python(Language):
    pass

class Java(Language):
    pass

python = Python("Python")
java = Java("Java")
python.code()
java.code()


# 8. Kompyuter qurilmalari
class Device:
    def __init__(self, name):
        self.name = name

    def operate(self):
        print(f"{self.name} ishlayapti")

class Laptop(Device):
    pass

class Smartphone(Device):
    pass

laptop = Laptop("MacBook")
smartphone = Smartphone("iPhone")
laptop.operate()
smartphone.operate()


# 9. O'qituvchilar va talabalar
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Salom, mening ismim {self.name}")

class Student(Person):
    pass

class Teacher(Person):
    pass

student = Student("Ali")
teacher = Teacher("Mr. Smith")
student.introduce()
teacher.introduce()


# 10. Mevalar va sabzavotlar
class Food:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} yeyapman")

class Fruit(Food):
    pass

class Vegetable(Food):
    pass

fruit = Fruit("Olma")
vegetable = Vegetable("Sabzi")
fruit.eat()
vegetable.eat()
