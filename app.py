from flask import Flask, render_template
from plot import plot, plot_new

app = Flask(__name__)


@app.route("/")
def render_plot():
    return render_template("plot.html", plot_data=plot())


@app.route("/bar")
def new_plot():
    return render_template("plot_new.html", plot_data=plot_new())


if __name__ == "__main__":
    app.run(debug=True)
