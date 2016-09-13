from flask import render_template, request

from app import app
from app.forms import WordCount
from collections import Counter


@app.route("/", methods=["GET", "POST"])
def index():
    wordcount_form = WordCount(request.form)
    if request.method == "POST" and wordcount_form.validate():
        user = wordcount_form.user_input.data
        words = user.split(" ")
        word_count=len(words)
        character= list(user)
        character_count=len(character)
        character = [ x for x in character if x != " "]
        (Counter(words).most_common(2))
        (Counter(character).most_common(2))
        
    return render_template("index.html", wordcount_form=wordcount_form)
