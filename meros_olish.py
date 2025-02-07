class Swim:
    def swim(self):
        print("suzishni biladi")

class Engilish:
    def speak(self):
        print("Ingiliz tilida gaplasha oladi")

class Math:
    def solve(self):
        print("Misollar ishlay oladi")


class Student(Engilish,Swim,Math):
 pass


s = Student()
s.solve()
s.swim()
s.speak()