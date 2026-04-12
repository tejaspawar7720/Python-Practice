class Car:
    #color = "Red"
    #brand = "MClaren"
    def __init__(self, brand, color, modelno):
        self.brand = brand
        self.color = color
        self.modelno = modelno
        print("adding Data to object..... ")   
car1 = Car("Mclaren", "Red", 2025)
print(car1.brand, car1.color, car1.modelno)

car2 = Car("Aston Martin Valhalla" ,"Green ", 2026)
print(car2.brand, car2.color, car2.modelno)