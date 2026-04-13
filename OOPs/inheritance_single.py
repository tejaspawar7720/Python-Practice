class Car:
    color = "Red"
    @staticmethod
    def start():
        print("has Started........")

    @staticmethod
    def stop():
        print("has Stopped.....")

class MclarenCars(Car,):
    def __init__(self, name):
        self.name = name


car1 = MclarenCars("Mclaren 720s")
car2 = MclarenCars("Mclaren Senna")
print(MclarenCars.color)
print(car2.name)
MclarenCars.start()
MclarenCars.stop()



