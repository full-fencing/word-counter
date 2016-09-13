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
        character = list(user)
        character = [ x for x in character if x != " "]
        character_count=len(character)
        most_common_words = Counter(words).most_common()
        most_common_character = Counter(character).most_common()

        return render_template(
            "index.html",
            wordcount_form=wordcount_form,
            words=words, word_count=word_count, character=character,
            character_count=character_count, most_common_words=most_common_words,
            most_common_character=most_common_character
        )

    else:
        return render_template("index.html", wordcount_form=wordcount_form)

