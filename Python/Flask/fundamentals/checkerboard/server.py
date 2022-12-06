from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<int:rows>')
@app.route('/<int:rows>/<int:cols>')
@app.route('/<int:rows>/<int:cols>/<string:clr1>')
@app.route('/<int:rows>/<int:cols>/<string:clr1>/<string:clr2>')
def home(rows=8, cols=8, clr1="red", clr2="black"):
    return render_template('index.html', rows=rows, cols=cols, clr1=clr1, clr2=clr2)


if __name__ == "__main__":
    app.run(debug=True)
