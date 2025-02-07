
# ////////////  1   /////////////////////////////////////////////////////////////////////////////////////////////////////

class Dog:
    def sound(self):
        print("Hav-hav")

class Cat:
    def sound(self):
        print("Miyav")

class Animal(Dog, Cat):
    pass

a = Animal()
a.sound()

# ////////    2   /////////////////////////////////////////////////////////////////////////////////////////////////////////


class Car:
    def drive(self):
        print("Avtomobil harakatlanadi")

class Bike:
    def ride(self):
        print("Velosiped minib boriladi")

class Transport(Car, Bike):
    pass

t = Transport()
t.drive()
t.ride()


# //////////////////////   3   ///////////////////////////////////////////////////////////////////////////////////////////


class Email:
    def send(self):
        print("Xat yuborildi")

class SMS:
    def send(self):
        print("SMS yuborildi")

class Message(Email, SMS):
    pass

m = Message()
m.send()

# //////////////////////  4   //////////////////////////////////////////////////////////////////////////////////////////


class Discount:
    def apply_discount(self):
        print("Chegirma qo'llanildi")

class Coupon:
    def apply_coupon(self):
        print("Kupon ishlatildi")

class Payment(Discount, Coupon):
    pass

p = Payment()
p.apply_discount()
p.apply_coupon()


# ////////////////////   5  /////////////////////////////////////////////////////////////////////////////////////////////

class Football:
    def play(self):
        print("Futbol o'ynash")

class Tennis:
    def play(self):
        print("Tennis o'ynash")

class Sport(Football, Tennis):
    pass

s = Sport()
s.play()


#////////////////////   6   ////////////////////////////////////////////////////////////////////////////////////////

class Read:
    def study(self):
        print("O'qish")

class Teach:
    def teach(self):
        print("Dars berish")

class Education(Read, Teach):
    pass

e = Education()
e.study()
e.teach()


#/////////////////////////////  7   ///////////////////////////////////////////////////////////////////////////////////

class Python:
    def code(self):
        print("Python kod yozish")

class JavaScript:
    def code(self):
        print("JavaScript kod yozish")

class ProgrammingLanguage(Python, JavaScript):
    pass

p = ProgrammingLanguage()
p.code()


#////////////////////////////   8   ///////////////////////////////////////////////////////////////////////////////////

class Pizza:
    def eat(self):
        print("Pizza yeyayapman")

class Sushi:
    def eat(self):
        print("Sushi yeyayapm")

class  Restuarant(Pizza, Sushi):
    pass

r = Restuarant()
e.eat


#///////////////////////    9   ///////////////////////////////////////////////////////////////////////////////////////


class Artist:
    def draw(self):
        print("San'atkor rasm chizadi")

class Writer:
    def write(self):
        print("Yozuvchi kitob yozadi")

class Creator(Artist, Writer):
    pass

c = Creator()
c.draw()
c.write()





























