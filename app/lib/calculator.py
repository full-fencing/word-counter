from wtforms import Form, DecimalField,RadioField, validators, ValidationError


class Calculator(Form):
    user_input1 = DecimalField("First Number",validators=[validators.DataRequired()])
    user_input2 = DecimalField("Second Number",validators=[validators.DataRequired()])

    operators = RadioField("operator",
        default = "+",
        choices=[('+','Add'),('-','Subtract'),('*','Multiply'),('/','Divide')])

    def action(self):
        Number1=int(self.user_input1.data)
        Number2 = int(self.user_input2.data)
        if (self.operators.data == "+"):
            return Number1 + Number2
        elif (self.operators.data == "-"):
            return Number1 - Number2
        elif (self.operators.data == "*"):
            return Number1 * Number2
        elif (self.operators.data == "/"):
            return Number1 / Number2
        else:
            return "error"