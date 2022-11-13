class CarNotEnoughFuel(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class Car:
    fuel = 20
    rate = 0.1
    traveled = 0

    def __init__(self, fuel=20, rate=0.1):
        self.fuel = fuel
        self.rate = rate

    def drive(self, distance):
        possible_to_travel = self.fuel / self.rate

        if possible_to_travel >= distance:
            self.traveled += distance
            self.fuel -= distance * self.rate
        else:
            self.traveled += possible_to_travel
            self.fuel = 0
            raise CarNotEnoughFuel('Закончился бензин!')

car1 = Car()
car1.drive(201)