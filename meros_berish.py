# vhttps://github.com/Mabinkam/Inheritance_.git (meros olish) – bu obyektga yo‘naltirilgan dasturlash (OOP) dagi asosiy konseptlardan biri bo‘lib,
# bir sinfning (class) xususiyatlari va metodlarini boshqa sinflarga meros qilib o‘tish imkoniyatini beradi.


class Person:
    def __init__(self, name, fam):
        self.name = name
        self.fam = fam

    def say_hi(self):
        print("Hello")


class Pupil(Person):
    pass

class Students(Person):
    pass

class Teacher(Person):
    pass

p = Pupil("p","p")
s = Students("s", "s")
p.say_hi()
s.say_hi()