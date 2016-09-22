from wtforms import Form,StringField,validators, ValidationError
import requests

class Repository():

    def __init__(self,user):

        self.user = user


    def get_repos(self):

        r = requests.get('https://api.github.com/users/{}/repos'.format(self.user))

        result = r.json()

        return result

class RepoForm(Form):

    user_input= StringField("Give the user name", validators = [validators.DataRequired()])