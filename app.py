from flask import Flask, render_template, url_for
import random
app = Flask(__name__)

r = ["r2.png","r3.png","r4.png"]
m = ["m1.png","m2.png","m3.png"]

def randomint() -> int:
    return random.randint(0,2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pickr")
def pickr():
    f = r[randomint()]
    return render_template("result.html", file = f)

@app.route("/pickm")
def pickm():
    f = m[randomint()]
    return render_template("result.html", file = f)

if __name__ == "__main__":
    app.run(debug=True)
