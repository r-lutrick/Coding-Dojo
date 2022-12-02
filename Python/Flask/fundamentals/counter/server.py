from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "dont take seriously what the Gods intended as fun"  # set a secret key for security purposes


@app.route("/")
def home():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template("index.html")

@app.route("/counter", methods=['GET'])
def counter():
    return redirect("/")

@app.route("/reset", methods=['GET'])
def reseter():
    session.clear()
    return redirect("/")

##########################
if __name__ == "__main__":
    app.run(debug=True)
