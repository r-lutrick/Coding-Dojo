from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return f"Hello World!"

@app.route('/dojo')
def dojo():
    return f"Dojo!"

@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}"

@app.route('/<int:count>/<name>')
def mult_name(count, name):
    return f"{name}" * count

if __name__ == "__main__":
    app.run(debug=True)