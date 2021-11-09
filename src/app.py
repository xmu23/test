from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user = {'username' : 'Tom' }
    return render_template("base.html", title="home", user=user)

@app.route("/about")
def about():
    return "TOM's Website"

if __name__ == "__main__":
    app.run(debug = True)