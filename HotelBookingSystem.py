# HotelBookingSystem is a class that represents a basic hotel reservation system.
from unittest.mock import MagicMock
from Item_Database import ItemDatabase
class HotelBookingSystem:

    # Constructor to initialize the class with hotel's name and total number of rooms
    def __init__(self, total_rooms):
        self.booked_rooms = {}
        self.available_rooms = total_rooms

    # Method to book rooms for a guest
    def book_room(self, guest_name, num_rooms):
        if num_rooms <= self.available_rooms:
            if guest_name not in self.booked_rooms:
                self.booked_rooms[guest_name] = num_rooms
            else:
                self.booked_rooms[guest_name] += num_rooms
            self.available_rooms -= num_rooms
        else:
            raise OverflowError(f"Rooms available are: {self.available_rooms}")

    # Method to cancel a booking
    def cancel_booking(self, guest_name, num_rooms):
            self.booked_rooms[guest_name] -= num_rooms

    def total_booked_rooms(self):
        tot = 0
        for guest in self.booked_rooms:
            tot += self.booked_rooms[guest]
        return tot

    def get_room_price(self):
        itemdb = ItemDatabase()
        mock_obj = MagicMock()
        itemdb.get = mock_obj.return_value = 250.0
        print("\nThis room cost:",float(itemdb.get),"€/night")

    def get_service_price(self, service):
        itemdb = ItemDatabase()
        def service_price_list(service):
            if service == "gym":
                return 10.00
            elif service == "pool":
                return 25.00
        mock_obj = MagicMock()
        itemdb.get = mock_obj.side_effect = service_price_list(service)
        print(f"\nThe {service} service costs: {float(itemdb.get)}€")