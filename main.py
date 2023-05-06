#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
data_manager = DataManager()
data = data_manager.sheety()
# print(data)
flight_search = FlightSearch()
notification_manager = NotificationManager()
ORIGIN_CITY = "LON"

if data[0]["iataCode"]=="":
    for row in data:
        row["iataCode"] = flight_search.iatacodes(row["city"])
    print(data)
    data_manager.sheety = data
    data_manager.code_update()

# tomorrow so timedelta day+1
tomorrow = datetime.now() + timedelta(days=1)

# tomorrow so timedelta day+6*3-
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in data:
    flight = flight_search.flight_check(
        ORIGIN_CITY,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
