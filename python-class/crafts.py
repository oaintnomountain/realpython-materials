class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("Starting the engine...")

    def stop(self):
        print("Stopping the engine...")

    def technical_specs(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")


class Car(Vehicle):
    def drive(self):
        print("Driving on the road...")


class Aircraft(Vehicle):
    def fly(self):
        print("Flying on the sky...")


class FlyingCar(Car, Aircraft):
    pass
