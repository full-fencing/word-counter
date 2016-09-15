from flask import render_template, request
import requests

from app import app
from app.forms import WordCount, NumberOfUsers
from app.lib.calculator import Calculator
from app.lib.timestable import *
from collections import Counter
from app.lib.address import AddressBook

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/wordcounter", methods=["GET", "POST"])
def wordcounter():
    wordcount_form = WordCount(request.form)
    if request.method == "POST" and wordcount_form.validate():
        user = wordcount_form.user_input.data
        words = user.split(" ")
        word_count=len(words)
        character = list(user)
        character = [ x for x in character if x != " "]
        character_count=len(character)
        most_common_words = Counter(words).most_common()
        most_common_character = Counter(character).most_common()

        return render_template(
            "wordcounter.html",
            wordcount_form=wordcount_form,
            words=words, word_count=word_count, character=character,
            character_count=character_count, most_common_words=most_common_words,
            most_common_character=most_common_character
        )

    else:
        return render_template("wordcounter.html", wordcount_form=wordcount_form)

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    cal = Calculator(request.form)
    result = None
    if request.method == "POST" and cal.validate():
        result = cal.action()

    return render_template("calculator.html",calculator=cal, result=result)

@app.route("/timestable", methods=["GET", "POST"])
def timestable():
    table = TimesTable()
    return render_template("timestable.html", times_table=table)


@app.route("/address", methods=["GET", "POST"])
def addressbook():

    number_of_users_form = NumberOfUsers(request.form)
    if number_of_users_form.how_many_users.data:
        result = AddressBook(number_of_users_form.how_many_users.data)
    else:
        result = AddressBook()
    r = result.get_address()
    return render_template("address.html",
                           userdata=r,
                           number_of_users_form=number_of_users_form)






