from flask import Flask, render_template

app = Flask(__name__)


@app.route("/play")
@app.route("/play/<int:count>")
@app.route("/play/<int:count>/<string:color>")
def play_boxes(count=1, color="grey"):
    return render_template("index.html", count=count, color=color)


if __name__ == "__main__":
    app.run(debug=True)
