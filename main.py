from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations["STATION NAME"] = stations["STANAME                                 "]
stations = stations[["STAID","STATION NAME"]]

@app.route("/home/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID"+str(station).zfill(6)+".txt"

    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])

    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return {"station": station,
            "date": date,
            "temperature": temperature}


@app.route("/api/v1/<station>")
def just_station(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"

    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])

    return render_template("station_info.html", data=df.to_html(), title=f"Station {station}")

@app.route("/api/v1/yearly/<station>/<year>")
def just_by_year(year, station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"

    df = pd.read_csv(filename, skiprows=20)

    df['    DATE'] = df['    DATE'].astype(str)

    result = df[df['    DATE'].str.startswith(str(year))]

    return render_template("station_info.html", data=result.to_html(), title=f"Station {station} in {year}")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
