class Flight:
    def __init__(self, flightNumber="", departureCity="", arrivalCity="", departureTime="", arrivalTime="", flightStatus="", seatsAvailable=0):
        self.flightNumber = flightNumber
        self.departureCity = departureCity
        self.arrivalCity = arrivalCity
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.flightStatus = flightStatus
        self.seatsAvailable = seatsAvailable

class Passenger:
    def __init__(self, name="", bookingStatus="", seatNumber=""):
        self.name = name
        self.bookingStatus = bookingStatus
        self.seatNumber = seatNumber

class Booking:
    def __init__(self, bookingNumber="", passenger=None, flight=None, paymentDetails=""):
        self.bookingNumber = bookingNumber
        self.passenger = passenger
        self.flight = flight
        self.paymentDetails = paymentDetails

class Staff:
    def __init__(self, name="", staffID=""):
        self.name = name
        self.staffID = staffID

if __name__ == "__main__":
    # Creating objects of classes
    flight = Flight("AI101", "Delhi", "London", "10:00", "15:00", "On-time", 200)
    passenger = Passenger("John Doe", "Confirmed", "A1")
    booking = Booking("B001", passenger, flight, "Credit Card")
    staff = Staff("Jane Doe", "S001")

    # Accessing class data through objects
    print("Flight Number:", flight.flightNumber)
    print("Departure City:", flight.departureCity)
    print("Arrival City:", flight.arrivalCity)
    print("Departure Time:", flight.departureTime)
    print("Arrival Time:", flight.arrivalTime)
    print("Flight Status:", flight.flightStatus)
    print("Seats Available:", flight.seatsAvailable)
    print()

    print("Passenger Name:", passenger.name)
    print("Booking Status:", passenger.bookingStatus)
    print("Seat Number:", passenger.seatNumber)
    print()

    print("Booking Number:", booking.bookingNumber)
    print("Passenger Name:", booking.passenger.name)
    print("Flight Number:", booking.flight.flightNumber)
    print("Payment Details:", booking.paymentDetails)
    print()

    print("Staff Name:", staff.name)
    print("Staff ID:", staff.staffID)
    print()
