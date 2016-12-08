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
                    winner = True
                    loser = False
                    matchone = False
                    matchtwo = False
                    matchthree = False
                    matchfour = False
                elif ((one == winningnumbers[0]) and (two == winningnumbers[1]) and (three == winningnumbers[2]) and (four == winningnumbers[3])):
                    matchfour = True
                    winner = False
                    loser = False
                    matchone = False
                    matchtwo = False
                    matchthree = False
                elif ((one == winningnumbers[0]) and (two == winningnumbers[1]) and (three == winningnumbers[2])):
                    matchthree = True
                    winner = False
                    loser = False
                    matchone = False
                    matchtwo = False
                    matchfour = False
                elif ((one == winningnumbers[0]) and (two == winningnumbers[1])):
                    matchtwo = True
                    winner = False
                    loser = False
                    matchone = False
                    matchthree = False
                    matchfour = False
                elif one == winningnumbers[0]:
                    matchone = True
                    winner = False
                    loser = False
                    matchtwo = False
                    matchthree = False
                    matchfour = False
                else:
                    loser = True
                    winner = False
                    matchone = False
                    matchtwo = False
                    matchthree = False
                    matchfour = False
                stats.append(list([winner,loser,matchone,matchtwo,matchthree,matchfour]))

                # - fix if statement above -
                # - find database to use and connect to
                # - move for loops to backend
            return render_template('index.html', boards = boards, winningnumbers = winningnumbers, winner = winner, loser = loser, matchone = matchone, matchtwo = matchtwo, matchthree = matchthree, matchfour = matchfour, stats = stats)
        else:
            return 'Invalid Request Method'
    except:
        error = 'Error Occurred'
        return render_template('index.html', error = error)

if __name__ == '__main__':
    app.run()
