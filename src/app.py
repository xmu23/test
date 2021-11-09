from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, World!"

@app.route("/about")
def about():
    return "Xiangxi Mu"

if __name__ == "__main__":
    app.run(debug = True)