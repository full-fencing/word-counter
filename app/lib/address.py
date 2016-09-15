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
        result= result["results"]
        
        return result

       
