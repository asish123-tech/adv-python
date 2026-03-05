# track vehicle, manage parking spaces, and enforce parking rules
# Parent Class
class Vehicle:
    def __init__(self, number):
        self.number = number


# Child Classes
class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


# Parking Lot Class
class ParkingLot:
    def __init__(self, spaces):
        self.total_spaces = spaces
        self.available_spaces = spaces

    def park(self, vehicle):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            print(vehicle.number, "Parked Successfully")
            print("Spaces left:", self.available_spaces)
        else:
            print("Parking Full")

    def remove(self):
        if self.available_spaces < self.total_spaces:
            self.available_spaces += 1
            print("Vehicle Removed")
            print("Spaces left:", self.available_spaces)
        else:
            print("Parking already empty")


# -------- Main Program --------

spaces = int(input("Enter total parking spaces: "))
lot = ParkingLot(spaces)

while True:
    print("\n1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        v_type = input("Enter vehicle type (car/bike): ")
        number = input("Enter vehicle number: ")

        if v_type.lower() == "car":
            vehicle = Car(number)
        elif v_type.lower() == "bike":
            vehicle = Bike(number)
        else:
            print("Invalid vehicle type")
            continue

        lot.park(vehicle)

    elif choice == 2:
        lot.remove()

    elif choice == 3:
        
        print("Exiting...")
        break

    else:
        print("Invalid choice")
    