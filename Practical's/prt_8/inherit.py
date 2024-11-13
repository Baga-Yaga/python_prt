# Base class
class Vehicle:
    def set_attributes(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.year} {self.make} {self.model}'s engine is starting."

    def stop_engine(self):
        return f"{self.year} {self.make} {self.model}'s engine is stopping."


class Car(Vehicle):
    def set_attributes(self, make, model, year, doors):
        super().set_attributes(make, model, year)
        self.doors = doors

    def honk(self):
        return f"{self.year} {self.make} {self.model} honks!"


class Motorcycle(Vehicle):
    def set_attributes(self, make, model, year, type_of_motorcycle):
        super().set_attributes(make, model, year)
        self.type_of_motorcycle = type_of_motorcycle

    def rev(self):
        return f"{self.year} {self.make} {self.model} revs its engine!"


my_car = Car()
my_car.set_attributes("Toyota", "Camry", 2020, 4)

my_motorcycle = Motorcycle()
my_motorcycle.set_attributes("Yamaha", "MT-09", 2021, "Sport")

print(my_car.start_engine())
print(my_car.honk())
print(my_car.stop_engine())

print(my_motorcycle.start_engine())
print(my_motorcycle.rev())
print(my_motorcycle.stop_engine())
