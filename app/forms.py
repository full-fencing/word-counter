from wtforms import Form, DecimalField, TextAreaField, validators, ValidationError


class WordCount(Form):
    user_input = TextAreaField(
        "Type some words.", validators=[validators.DataRequired()]
    )


class NumberOfUsers(Form):
    user_input = DecimalField("How many users do you want?",
                              validators=[validators.DataRequired()])
