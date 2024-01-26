"""

format_string, /, *args, **kwargs)

"""

class Vehicle:
    def __init__(self, wheels, max_speed):
        self.wheels = wheels
        self.max_speed = max_speed

    def move(self):
        pass

class Car(Vehicle):
    def __init__(self, wheels, max_speed, num_of_doors, fuel_type):
        super().__init__(wheels, max_speed)
        self.num_of_doors = num_of_doors
        self.fuel_type = fuel_type
    
    def honk(self):
        pass