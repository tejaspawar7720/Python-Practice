class Car:
    
    @staticmethod
    def Carrepaired():
        print("Car has been fully repaired.....")
    
    @staticmethod
    def Carisdamaged():
        print("Your Car is fully damaged")

class MClarenCars(Car):
    def __init__(self, brand):
        self.brand = brand
        print(brand)

class Cr(MClarenCars):

    @staticmethod
    def Carcolor():
        print("Your car is Red color...")

    @staticmethod
    def carinfo():
        print("Your car has 720 hosre power...\n1000nm torque \nand its a 4 Wheel Drive... ")

cr1 = Cr("Mclaren")
cr1.Carcolor()
cr1.carinfo()
cr1.Carrepaired()



