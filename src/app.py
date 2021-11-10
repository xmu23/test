from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

visitors = []

@app.route("/")
def index():
    user = {'username' : 'TomMu' }
    return render_template("base.html", title="home", user=user, visitors=visitors)

@app.route("/about")
def about():
    return "TOM's Website"

@app.route("/add", methods=["POST"])
def add():
    visitor = request.form.get("visitor")
    if visitor != "":      
        visitors.append(visitor)
        print(visitors[-1])
    return redirect(url_for("index"))

@app.route("/remove/<string:name>")
def remove(name):
    visitors.remove(name)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)