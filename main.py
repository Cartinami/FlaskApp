from flask import Flask, jsonify, render_template, request, redirect, url_for
from random import randint, seed
seed()


app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'GET':
            return render_template('index.html')
        elif request.method == 'POST':
            requestdata = request.form['numofticks']
            tickets = int(requestdata)
            boards = []
            while len(boards) < tickets:
                one = randint(1,50)
                two = randint(1,50)
                three = randint(1,50)
                four = randint(1,50)
                five = randint(1,50)
                boards.append(dict({'one':one, 'two':two, 'three':three, 'four':four, 'five':five}))
            return render_template('index.html', boards = boards)
        else:
            return 'Error Occurred'
    except:
        numerror = 'Please enter a number'
        return render_template('index.html', numerror = numerror)

if __name__ == '__main__':
    app.run()
