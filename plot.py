import pandas as pd
import os
import json
import plotly
import plotly.graph_objects as go


def load_agg_data():

    csv_path = os.path.join("static", "hawaii_measurements.csv")
    df = pd.read_csv(csv_path)
    df = df.assign(date=pd.to_datetime(df["date"]))

    s = df.groupby(df["date"].dt.year)["prcp"].mean()

    return s


def plot():

    s = load_agg_data()

    data = [go.Scatter(x=s.index, y=s.values)]

    return json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)


def plot_new():

    s = load_agg_data()

    data = [go.Bar(x=s.index, y=s.values)]

    return json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)



if __name__ == "__main__":
    print(plot())
