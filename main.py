from flask import Flask, jsonify, render_template, request, redirect, url_for
from random import randint, seed

app = Flask(__name__)
app.debug = True
seed()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/powerball', methods=['GET', 'POST'])
def powerball():
    money = 20
    ticketprice = -4
    totalprice = 0
    winningnumbers = ['','','','','']

    if request.method == 'GET':
        return render_template('powerball.html', money=money, winningnumbers=winningnumbers)
    elif request.method == 'POST':
        requestdata = request.form['numofticks']
        tickets = int(requestdata)
        winningnumbers = [randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)]
        boards = []
        stats = []
        indexes = []
        matches = []
        prizes = []
        winstats = []

        i = 0
        while len(boards) < tickets:
            if not (money < ticketprice):
                money = money - ticketprice
                totalprice = totalprice + ticketprice
                one = randint(1,10)
                two = randint(1,10)
                three = randint(1,10)
                four = randint(1,10)
                five = randint(1,10)
                boards.append(list([one,two,three,four,five]))

                if ((one == winningnumbers[0]) and (two == winningnumbers[1]) and (three == winningnumbers[2]) and (four == winningnumbers[3]) and (five == winningnumbers[4])):
                    status = '!!!!!!!WINNER!!!!!!!'
                    amount = 1200
                    money = money + amount
                elif ((one == winningnumbers[0]) and (two == winningnumbers[1]) and (three == winningnumbers[2]) and (four == winningnumbers[3])):
                    status = 'Four'
                    amount = 1000
                    money = money + amount
                elif ((one == winningnumbers[0]) and (two == winningnumbers[1]) and (three == winningnumbers[2])):
                    status = 'Three'
                    amount = 600
                    money = money + amount
                elif ((one == winningnumbers[0]) and (two == winningnumbers[1])):
                    status = 'Two'
                    amount = 200
                    money = money + amount
                elif one == winningnumbers[0]:
                    status = 'One'
                    amount = 40
                    money = money + amount
                else:
                    status = 'L'
                    money = money
                    amount = 0
                net = money + totalprice
                stats.append(status)

                if len(stats[i]) > 1:
                    index = str(i + 1)
                    match = stats[i]
                    prize = '+$' + str(amount) + '.00'
                    winstats.append(list([index,match,prize]))
                    i += 1
                else:
                    i += 1
            else:
                break
        return render_template('powerball.html',boards=boards,winningnumbers=winningnumbers,money=money,winstats=winstats,totalprice=totalprice,net=net)
    else:
        return 'Invalid Request Method'




if __name__ == '__main__':
    app.run()
