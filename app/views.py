from flask import render_template, request

from app import app
from app.forms import WordCount


@app.route("/", methods=["GET", "POST"])
def index():
    wordcount_form = WordCount(request.form)
    if request.method == "POST" and wordcount_form.validate():
        user_input = wordcount_form.data
        print(user_input)
    return render_template("index.html", wordcount_form=wordcount_form)
