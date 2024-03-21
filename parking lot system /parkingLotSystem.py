import datetime

class Payment:
    def calculate_cost(self, hours):
        raise NotImplementedError

class CarPayment(Payment):
    def calculate_cost(self, hours):
        return hours * 2

class BikePayment(Payment):
    def calculate_cost(self, hours):
        return hours * 1

class HandicappedPayment(Payment):
    def calculate_cost(self, hours):
        return 0

class Vehicle:
    def __init__(self):
        self.payment = None
        self.parked_time = None

    def get_type(self):
        raise NotImplementedError

    def calculate_cost(self, hours):
        return self.payment.calculate_cost(hours)

    def set_parked_time(self):
        self.parked_time = datetime.datetime.now()

    def get_parked_time(self):
        return self.parked_time

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.payment = CarPayment()

    def get_type(self):
        return "Car"

class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.payment = BikePayment()

    def get_type(self):
        return "Bike"

class HandicappedVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        self.payment = HandicappedPayment()

    def get_type(self):
        return "Handicapped"

class ParkingLot:
    def __init__(self, floors, rows, spots_per_row):
        self.floors = floors
        self.rows = rows
        self.spots_per_row = spots_per_row
        self.spots = [[[None for _ in range(spots_per_row)] for _ in range(rows)] for _ in range(floors)]

    def park(self, vehicle, floor, row, spot):
        if self.spots[floor][row][spot] is None:
            self.spots[floor][row][spot] = vehicle
            print(f"{vehicle.get_type()} parked successfully at floor {floor}, row {row}, spot {spot}.")
            return True
        else:
            print("Spot already occupied.")
            return False

    def leave(self, vehicle):
        for i in range(self.floors):
            for j in range(self.rows):
                for k in range(self.spots_per_row):
                    if self.spots[i][j][k] == vehicle:
                        hours = self.calculate_hours_parked(vehicle)
                        cost = vehicle.calculate_cost(hours)
                        self.spots[i][j][k] = None
                        print(f"{vehicle.get_type()} left successfully. Total cost: {cost}")
                        return True
        print(f"{vehicle.get_type()} not found.")
        return False

    def available_spots(self, floor):
        count = 0
        for row in self.spots[floor]:
            for spot in row:
                if spot is None:
                    count += 1
        return count

    def handicapped_spots(self, floor):
        count = 0
        for row in self.spots[floor]:
            for vehicle in row:
                if isinstance(vehicle, HandicappedVehicle):
                    count += 1
        return count

    def calculate_hours_parked(self, vehicle):
        now = datetime.datetime.now()
        parked_time = vehicle.get_parked_time()
        duration = now - parked_time
        hours = duration.total_seconds() / 3600
        return hours

def main():
    lot = ParkingLot(3, 10, 20)
    car1, car2 = Car(), Car()
    bike1, bike2 = Bike(), Bike()
    hv1 = HandicappedVehicle()
    print("Available spots on floor 0:", lot.available_spots(0))
    car1.set_parked_time()
    lot.park(car1, 0, 0, 0)
    car2.set_parked_time()
    lot.park(car2, 0, 0, 1)
    bike1.set_parked_time()
    lot.park(bike1, 0, 0, 2)
    hv1.set_parked_time()
    lot.park(hv1, 2, 9, 19)

    print("Available spots on floor 0:", lot.available_spots(0))
    print("Handicapped spots on floor 2:", lot.handicapped_spots(2))

    lot.leave(car1)
    lot.leave(bike2)

    print("Available spots on floor 0:", lot.available_spots(0))

if __name__ == "__main__":
    main()
