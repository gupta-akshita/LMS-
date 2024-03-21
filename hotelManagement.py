# Hotel and HotelLocation class
class HotelLocation:
    def __init__(self, location, address, phone_number):
        self.location = location
        self.address = address
        self.phone_number = phone_number

class Hotel:
    def __init__(self, name):
        self.name = name
        self.locations = []

    def add_location(self, location):
        self.locations.append(location)

# Room class
class Room:
    def __init__(self, room_number, room_style, booking_price):
        self.room_number = room_number
        self.room_style = room_style
        self.booking_price = booking_price

# Account class
class Account:
    def __init__(self, username, password, account_type):
        self.username = username
        self.password = password
        self.account_type = account_type

# RoomBooking class
class RoomBooking:
    def __init__(self, room, guest_name, number_of_nights):
        self.room = room
        self.guest_name = guest_name
        self.number_of_nights = number_of_nights

# Notification class
class Notification:
    def __init__(self, message, recipient):
        self.message = message
        self.recipient = recipient

# RoomHouseKeeping class
class RoomHouseKeeping:
    def __init__(self, room, date, status):
        self.room = room
        self.date = date
        self.status = status

# RoomCharge class
class RoomCharge:
    def __init__(self, room, charge_name, charge_amount):
        self.room = room
        self.charge_name = charge_name
        self.charge_amount = charge_amount

# Invoice class
class Invoice:
    def __init__(self, room, charges):
        self.room = room
        self.charges = charges

# RoomKey class
class RoomKey:
    def __init__(self, room, key_id, barcode):
        self.room = room
        self.key_id = key_id
        self.barcode = barcode

# Main code
if __name__ == "__main__":
    # Create a Hotel object
    my_hotel = Hotel("The Sun Palace")

    # Add some locations to the hotel
    location1 = HotelLocation("Udaipur", "Street 1", 9876543)
    location2 = HotelLocation("Jaipur", "Street 5", 7654321)
    my_hotel.add_location(location1)
    my_hotel.add_location(location2)

    # Get the name and locations of the hotel
    print("Hotel Name:", my_hotel.name)
    print("Hotel Locations:")
    for location in my_hotel.locations:
        print("Location:", location.location)
        print("Address:", location.address)
        print("Phone Number:", location.phone_number)
        print()

    # Create a Room object
    room1 = Room(101, "Deluxe", 2500)

    # Create a RoomBooking object
    booking1 = RoomBooking(room1, "Suraj Pandey", 3)

    # Get the details of the RoomBooking
    print("Guest Name:", booking1.guest_name)
    print("Room Number:", booking1.room.room_number)
    print("Room Style:", booking1.room.room_style)
    print("Booking Price:", booking1.room.booking_price)
    print("Number of Nights:", booking1.number_of_nights)

    # Create a Notification object
    notification1 = Notification("Your booking has been confirmed.", "Suraj Pandey")

    # Get the details of the Notification
    print("Message:", notification1.message)
    print("Recipient:", notification1.recipient)
