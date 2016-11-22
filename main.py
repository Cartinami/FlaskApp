from flask import Flask, jsonify, render_template, request, redirect, url_for
from random import randint, seed

global money
seed()

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/name', methods=['POST'])
def getnames():
        first = request.form.get('firstname');
        last = request.form.get('lastname');
        num = request.form.get('number');
        return render_template("newpage.html", first=first, last=last, num=num)

if __name__ == "__main__":
    app.run()
