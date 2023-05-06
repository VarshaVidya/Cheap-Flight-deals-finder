import requests
from flight_data import FlightData
TEQUILA = "https://tequila-api.kiwi.com"
API_KEY = "_pYWzV69v9QZXt-5kllLr9dtIHVrBY52"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def iatacodes(self,city):
        location = f"{TEQUILA}/locations/query"
        header = {"apikey":API_KEY}
        param = {"term":city,"location_types":"city"}
        response = requests.get(url= location,headers=header,params=param)
        results = response.json()["locations"]

        code = results[0]["code"]
        return code

    def flight_check(self,origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey":API_KEY}
        param={
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url = f"{TEQUILA}/v2/search",
        headers= headers,params = param)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data

