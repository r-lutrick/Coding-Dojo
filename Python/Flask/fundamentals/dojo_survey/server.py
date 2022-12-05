from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "No Secrets Here..."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/user_dict", methods=["POST"])
def users():
    session["name"] = request.form["user_name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect("/result")


@app.route("/result")
def results():
    return render_template("results.html")


##########################
if __name__ == "__main__":
    app.run(debug=True)
