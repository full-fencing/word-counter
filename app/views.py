from flask import render_template, request

from app import app
from app.forms import WordCount


@app.route("/", methods=["GET", "POST"])
def index():
    wordcount_form = WordCount(request.form)
    if request.method == "POST" and wordcount_form.validate():
        pass
    return render_template("index.html", wordcount_form=wordcount_form)
