#A class is like a blueprint of the class that defines the state and behaviour of objects.

#An object is an instance of the class. Its an entity that has state and behaviour.

class Car:
    #The __init__ method is a special method known as the constructor. 
    #It initializes the object's attributes when an object is created. 

    # self refers to the instance of the class.
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def displayinfo(self):
        print(f"Car: {self.brand} - Model: {self.model}")

car1 = Car("BMW","Corolla")
car2 = Car("Tesla","Model S")