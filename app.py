from flask import Flask, render_template, url_for
import random
app = Flask(__name__)

r = ["r1.png","r2.png","r3.png","r4.png","r5.png","r6.png","r7.png","r8.png","r9.png","r10.png","r11.png","r12.png","r13.png","r14.png","r15.png","r16.png","r17.png","r18.png","r19.png","r20.png"]
m = ["m1.png","m2.png","m3.png","m4.png","m5.png","m6.png","m7.png","m8.png","m9.png","m10.png","m11.png","m12.png","m13.png","m14.png","m15.png","m16.png","m17.png","m18.png","m19.png","m20.png"]
d = ["1.png","2.png","3.png","4.png","5.png","6.png"]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pickr")
def pickr():
    return render_template("result.html", file = r[random.randint(0,19)])

@app.route("/pickm")
def pickm():
    return render_template("result.html", file = m[random.randint(0,19)])

@app.route("/roll")
def roll():
    return render_template("index.html", die = d[random.randint(0,5)])

if __name__ == "__main__":
    app.run(debug=True)
