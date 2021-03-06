import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title = "About", company = data)

@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member = member)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form.get("name")))
    return render_template("contact.html", page_title = "Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title = "Careers")


if __name__ == "__main__": #references built-in variable
    app.run( #if statement above is true we run the app with the following arguments
        host = os.environ.get("IP", "0.0.0.0"), #using os module from standard library to get the 'IP' environment variable if it exists but return a default value if it isn't found
        port = int(os.environ.get("PORT", "5000")), #cast port as integer using int(), default is set to 5000 (common port used by Flask)
        debug = True #lets us debug code easier during devleopment stage
    )
    #__main__ is the name of default module in PY, so if not imported will be run directly (main will not be imported so app will run using arguments passed inside of statement)