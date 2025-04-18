# Assignment 1
# Base class
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self._strength_level = strength_level  # Encapsulated attribute

    def show_identity(self):
        print(f"I am {self.name}, and my superpower is {self.power}!")

    def get_strength(self):
        return self._strength_level

    def set_strength(self, level):
        if level >= 0:
            self._strength_level = level
        else:
            print("Strength level must be positive!")

# Subclass
class FlyingHero(Superhero):
    def __init__(self, name, strength_level, flight_speed):
        super().__init__(name, "Flying", strength_level)
        self.flight_speed = flight_speed

    def show_identity(self):
        print(f"I am {self.name}, I fly at {self.flight_speed} km/h and I’m super strong!")

# Creating objects
hero1 = Superhero("ShadowStrike", "Invisibility", 80)
hero2 = FlyingHero("SkyBlazer", 90, 300)

# Using methods
hero1.show_identity()
hero2.show_identity()

print(f"{hero1.name}'s Strength: {hero1.get_strength()}")
hero1.set_strength(100)
print(f"{hero1.name}'s New Strength: {hero1.get_strength()}")


#Activity 2
class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")

# Function using polymorphism
def move_vehicle(vehicle):
    vehicle.move()

# Creating different vehicles
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    move_vehicle(v)
