from wtforms import Form, DecimalField,RadioField, validators, ValidationError

import requests



class AddressBook():
    """docstring for OpenWeatherAPI"""
    # data = requests.get('http://api.randomuser.me/')
    # userdata = data.json()


    def get_payload(self,results=10):

        payload={"results":results}

        return payload


    def get_address(self):



        payload = self.get_payload()
        r = requests.get('http://api.randomuser.me/', params=payload)

        result = r.json()
        return result["results"]
        # return DailyWeather(description=result['weather'][0]['description'],
        #     icon = result['weather'][0]['icon'],
        #     temp = result['main']['temp'],
        #     dt = result['dt'],
        #     wind = result['wind']['speed'],
        #     pressure= result['main']['pressure'],
        #     humidity = result['main']['humidity'],
        #     sunrise = result['sys']['sunrise'],
        #     sunset = result['sys']['sunset'],
        #     )

# class UserClass():
    
#     def __init__(self,name=None,):
        
#         self.description=description
#         self.icon=icon
#         self.dt=dt
#         self.temp =temp
#         self.temp_night=temp_night
#         self.wind = wind
#         self.pressure=pressure
#         self.humidity=humidity
#         self.sunrise=sunrise
#         self.sunset=sunset

#     def __str__(self):
#         return "Description:{}, Temp: {}".format(self.description.
#             self.temp)        
