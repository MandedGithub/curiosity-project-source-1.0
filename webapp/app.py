from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("mainpage.html")

@app.route("/keyboardcrusher")
def keyboardcrusher():
    return render_template("kbcmp.html")

@app.route("/beginner")
def beginner():
    return render_template("kbcb.html")

@app.route("/intermediate")
def intermediate():
    return render_template("kbci.html")

@app.route("/advanced")
def advanced():
    return render_template("kbca.html")

@app.route("/socialmedia")
def mybio():
    return render_template("socialmedia.html")

app.run()





