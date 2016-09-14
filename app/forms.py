from wtforms import Form, TextAreaField, validators, ValidationError


class WordCount(Form):
    user_input = TextAreaField(
        "Type some words.", validators=[validators.DataRequired()]
    )
