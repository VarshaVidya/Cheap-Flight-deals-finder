import requests
from pprint import pprint
Sheety_endpoint = "https://api.sheety.co/10c8b4608cf98731e59f63baecb26874/flightDeals/sheet1"
class DataManager:
    def __init__(self):
        self.datum ={}
    # sheety request to connect to the flight deals excel sheet
    def sheety(self):
        response = requests.get(url = Sheety_endpoint)
        data = response.json()
        self.datum = data["sheet1"]
        # pprint(self.datum)
        return self.datum
    # print(response.text)

# put request to add to the excel sheet the iata code
    def code_update(self):
        for city in self.datum:
            new_datum = {
                "sheet1":{
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(url =f"{Sheety_endpoint}/{city['id']}",
                                    json = new_datum)
            print(response.text)

    #This class is responsible for talking to the Google Sheet.
