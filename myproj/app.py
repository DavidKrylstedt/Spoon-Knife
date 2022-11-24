from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/mars")
def mars():
    return render_template('mars.html')

@app.route("/recipe")
def recipe():
    return render_template('recipe.html')

@app.route("/earth")
def hello_earth():
    return "<p>Hello,people Earthlings!</p>"

if __name__ == '__main__':
    app.run(debug = True)

