class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.cityFrom = data['cityFrom']
        self.flyFrom = data['flyFrom']
        self.cityTo = data['cityTo']
        self.flyTo = data['flyTo']
        self.price = data['price']
        self.dep_date = (data['route'][0]['local_departure']).split("T")[0]
        self.ret_date = (data['route'][1]['local_arrival']).split("T")[0]
        
    def get_details(self):
        message = f"""
        Low price alert! Only ${self.price} to fly from {self.cityFrom}-{self.flyFrom} to {self.cityTo}-{self.flyTo}, from {self.dep_date} to {self.ret_date}.
        
        https://www.google.com/travel/flights?q=Flights%20to%20{self.flyTo}%20from%20{self.flyFrom}%20on%20{self.dep_date}%20through%20{self.ret_date}
        """
        return message