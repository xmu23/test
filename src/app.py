from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user = {'username' : 'Tom' }
    return render_template("base.html", title="home", user=user)
    
@app.route("/about")
def about():
    return "About us: Naser and the cool kids from CS321"

if __name__ == "__main__":
    app.run(debug = True)