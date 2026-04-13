class Car:
    @staticmethod
    def Stp():
        print("Your Car has stopped...")

    @staticmethod
    def start():
        print("Your Car has Started....")

class brand():
    def __init__(self, name):
        self.name = name
        print(name)

class models(brand,Car):
    @staticmethod
    def model1():
        print("This is a 2025 Year Model.. ")

    @staticmethod
    def type():
        print("This is a disel Cars...")

cr1 = models("Mclaren")

cr1.name
cr1.start()
cr1.model1()
cr1.type()
cr1.Stp()