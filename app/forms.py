from wtforms import Form, StringField, validators, ValidationError


class WordCount(Form):
    user_input = StringField(
        "Type some words.", validators=[validators.DataRequired()]
    )
