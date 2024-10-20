

class Car :
    def __init__(self,make,model,year):
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        longname = f'{self.year}  {self.make} {self.model} '
        return longname.title()

    def read_odometer(self):
        print(f"car has {self.odometer_reading} miles on it.")

    def odometer_update(self,newMile):
        if newMile>self.odometer_reading:
            self.odometer_reading = newMile
        else:
            print("Sorry we don't have enough odometer reading")
class electricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battry=Battry()

class Battry :
    def __init__(self,battry_size=40):
        self.battry_size = battry_size

    def get_descriptive_battry(self):
        print(f"the car has {self.battry_size} kwh battries.")

    def ger_range(self):
        if self.battry_size == 20:
            range  = 150
        elif self.battry_size == 40:
            range = 200
        print(f"the car has {range} kw range.")