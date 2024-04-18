from HotelBookingSystem import HotelBookingSystem
import pytest
import Item_Database

@pytest.fixture
def hotel():
    hotel = HotelBookingSystem(8)
    hotel.book_room("Andy",1)
    hotel.book_room("Jenny", 1)
    hotel.book_room("Mark", 3)
    hotel.book_room("Paul",2)
    hotel.book_room("Andy",1)
    return hotel

def test_booked_room(hotel):
    assert hotel.booked_rooms == {"Andy":2,"Paul":2,"Jenny":1,"Mark":3}

def test_cancel_booking(hotel):
    hotel.cancel_booking("Andy", 1)
    assert hotel.booked_rooms == {"Andy":1,"Paul":2,"Jenny":1,"Mark":3}

def test_total_booked_room(hotel):
    assert hotel.total_booked_rooms() == 8

def test_rooms_overflow(hotel):
    with pytest.raises(OverflowError):
        hotel.book_room("Paula",1)

def test_get_room_price(hotel):
    hotel.get_room_price()

def test_get_service_price(hotel):
    hotel.get_service_price("gym")
    hotel.get_service_price("pool")
