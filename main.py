from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from random import randint, seed

app = Flask(__name__)
app.debug = True
seed()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/powerball', methods=['GET', 'POST'])
def powerball():
    money = 0
    if request.method == 'GET':
        return render_template('powerball.html', money=money)

    if request.method == 'POST':
        requestdata = request.form['numofticks']
        tickets = int(requestdata)
        winningnumbers = [randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)]
        boards = []
        stats = []
        while len(boards) < tickets:
            one = randint(1,10)
            two = randint(1,10)
            three = randint(1,10)
            four = randint(1,10)
            five = randint(1,10)
            boards.append(list([one,two,three,four,five]))
            if ((one == winningnumbers[0]) and (two == winningnumbers[1]) and (three == winningnumbers[2]) and (four == winningnumbers[3]) and (five == winningnumbers[4])):
                status = 'WINNER'
                money = money + 1200
            elif ((one == winningnumbers[0]) and (two == winningnumbers[1]) and (three == winningnumbers[2]) and (four == winningnumbers[3])):
                status = 'Four'
                money = money + 1000
            elif ((one == winningnumbers[0]) and (two == winningnumbers[1]) and (three == winningnumbers[2])):
                status = 'Three'
                money = money + 600
            elif ((one == winningnumbers[0]) and (two == winningnumbers[1])):
                status = 'Two'
                money = money + 200
            elif one == winningnumbers[0]:
                status = 'One'
                money = money + 40
            else:
                status = ''
                money = money
            stats.append(status)
        return render_template('powerball.html',boards=boards,winningnumbers=winningnumbers,stats=stats,money=money)

    else:
        return 'Invalid Request Method'

if __name__ == '__main__':
    app.run()
