from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Motorcycle(Vehicle):
    def drive(self):
        return "Riding a motorcycle"

class Bicycle(Vehicle):
    def drive(self):
        return "Riding a bicycle"

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()

class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Motorcycle()

class BicycleFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Bicycle()
    
def get_factory(vehicle_type):
    if vehicle_type == "car":
        return CarFactory()
    elif vehicle_type == "motorcycle":
        return MotorcycleFactory()
    elif vehicle_type == "bicycle":
        return BicycleFactory()

if __name__ == "__main__":
    vehicle_type = "car"
    factory = get_factory(vehicle_type)
    vehicle = factory.create_vehicle()
    print(vehicle.drive())