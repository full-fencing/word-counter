from wtforms import Form, DecimalField,RadioField, validators, ValidationError

import requests



class AddressBook():
    """docstring for OpenWeatherAPI"""
    # data = requests.get('http://api.randomuser.me/')
    # userdata = data.json()
    def __init__(self, results=10):
        self.results = results


    def get_payload(self):

        payload={"results": self.results}

        return payload


    def get_address(self):



        payload = self.get_payload()
        r = requests.get('http://api.randomuser.me/', params=payload)

        result = r.json()
        result= result["results"]

        return result


