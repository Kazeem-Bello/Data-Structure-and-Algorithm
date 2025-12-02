class Vehicle:
    def __init__(self, make: str, model: str, year: int, mileage: int):
        self.make = make
        self.model = model
        self.year = year
        self._mileage = mileage

    def drive(self, distance):
        return distance + self._mileage
    
    