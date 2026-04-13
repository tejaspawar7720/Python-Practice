class Car:

    def __init__(self,brand2):
        self.brand2 = brand2
        print(brand2)

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

class models():
    @staticmethod
    def model1():
        print("This is a 2025 Year Model.. ")


    @staticmethod
    def type():
        print("This is a disel Cars...")

class Allinfo(Car,models,brand):
    def __init__(self, brand2, name):
        super().model1()
        super().type()
        super().start()
        super().Stp()
        super().__init__(brand2)
        super().__init__(name)
        self.brand2  =  brand2
        self.name =  name

cr1 = Allinfo("Mclaren","senna")

