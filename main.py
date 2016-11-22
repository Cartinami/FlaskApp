from flask import Flask, jsonify, render_template, request, redirect, url_for
from random import randint, seed
app.debug = True
seed()
global money

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lottery', methods=['POST'])
def getnumbers(data):
        amount = int(request.form['numofboards'])
        number = (randint(1,50))
        return amount + ' ' + number

@app.route('/data')
def data():

    return jsonify(**d)


if __name__ == "__main__":
    app.run()
