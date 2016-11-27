from flask import Flask, jsonify, render_template, request, redirect, url_for
from random import randint, seed
seed()


app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        tickets = request.form['numofticks']
        return render_template('index.html', tickets = tickets)
    else:
        return "Invlalid Request"

if __name__ == "__main__":
    app.run()
