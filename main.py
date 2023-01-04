from flask import Flask, render_template
import pandas
app = Flask(__name__)

@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # df = pandas.read_csv("", "r")
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main))":
    app.run(debug=True)

