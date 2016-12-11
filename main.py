from flask import Flask, jsonify, render_template, request, redirect, url_for
from random import randint, seed

app = Flask(__name__)
app.debug = True
seed()

cash = 20
totalprice = 0

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/powerball', methods=['GET', 'POST'])
def powerball():
    global totalprice
    global cash
    lowfunds = 'fade'
    winningnumbers = [' ',' ',' ',' ',' ']
    netcolor = 'positive'

    if request.method == 'GET':
        net = 0
        totalprice = 0
        return render_template('powerball.html',cash=cash,totalprice=totalprice,lowfunds=lowfunds,winningnumbers=winningnumbers,net=net,netcolor=netcolor)
    elif request.method == 'POST':
        winningnumbers = [randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)]
        requestdata = request.form['numofticks']
        requesttick = request.form['tickradio']

        try:
            tickets = int(requestdata)
        except:
            net = 0
            totalprice = 0
            return render_template('powerball.html',cash=cash,totalprice=totalprice,lowfunds=lowfunds,winningnumbers=winningnumbers,net=net,netcolor=netcolor)

        if requesttick == 'hard':
            ticketprice = 50
        elif requesttick == 'med':
            ticketprice = 20
        elif requesttick == 'easy':
            ticketprice = 4


        totalprice = tickets * ticketprice
        maxticks = cash / ticketprice
        maxcost = maxticks * ticketprice
        coststr = str(maxcost)
        maxstr = str(maxticks)

        if totalprice > cash:
            lowfunds = 'show'
            net = 0
            return render_template('powerball.html',cash=cash,ticketprice=ticketprice,totalprice=totalprice,maxstr=maxstr,lowfunds=lowfunds,winningnumbers=winningnumbers,coststr=coststr,net=net)
        else:
            boards = []
            stats = []
            indexes = []
            matches = []
            prizes = []
            winstats = []
            i = 0

            while len(boards) < tickets:
                cash = cash - ticketprice
                one = randint(1,10)
                two = randint(1,10)
                three = randint(1,10)
                four = randint(1,10)
                five = randint(1,10)
                boards.append(list([one,two,three,four,five]))

                if ((one == winningnumbers[0]) and (two == winningnumbers[1]) and (three == winningnumbers[2]) and (four == winningnumbers[3]) and (five == winningnumbers[4])):
                    status = '!!!!!!!WINNER!!!!!!!'
                    amount = 1200
                    cash = cash + amount
                elif ((one == winningnumbers[0]) and (two == winningnumbers[1]) and (three == winningnumbers[2]) and (four == winningnumbers[3])):
                    status = 'Four'
                    amount = 1000
                    cash = cash + amount
                elif ((one == winningnumbers[0]) and (two == winningnumbers[1]) and (three == winningnumbers[2])):
                    status = 'Three'
                    amount = 600
                    cash = cash + amount
                elif ((one == winningnumbers[0]) and (two == winningnumbers[1])):
                    status = 'Two'
                    amount = 200
                    cash = cash + amount
                elif one == winningnumbers[0]:
                    status = 'One'
                    amount = 40
                    cash = cash + amount
                else:
                    status = 'L'
                    cash = cash
                    amount = 0
                stats.append(status)

                if len(stats[i]) > 1:
                    index = str(i + 1)
                    match = stats[i]
                    prize = '+$' + str(amount) + '.00'
                    winstats.append(list([index,match,prize]))
                    i += 1
                else:
                    i += 1

            net = (-totalprice) + amount
            if net < 0:
                netcolor = 'negative'

        try:
            res = request.form['purchase']
        except:
            'oops'
        return render_template('powerball.html',cash=cash,totalprice=totalprice,maxstr=maxstr,lowfunds=lowfunds,winningnumbers=winningnumbers,coststr=coststr,boards=boards,net=net,winstats=winstats,netcolor=netcolor)
    else:
        return 'Invalid Request Method'



if __name__ == '__main__':
    app.run()
