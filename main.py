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
                if (winningnumbers[0]==one and winningnumbers[1]==two and winningnumbers[2]==three and winningnumbers[3]==four and winningnumbers[4]==five):
                    winner = True
                    loser = False
                    matchone = False
                    matchtwo = False
                    matchthree = False
                    matchfour = False
                    break
                elif (winningnumbers[0]==one and winningnumbers[1]==two and winningnumbers[2]==three and winningnumbers[3]==four):
                    matchfour = True
                    winner = False
                    loser = False
                    matchone = False
                    matchtwo = False
                    matchthree = False
                    break
                elif (winningnumbers[0]==one and winningnumbers[1]==two and winningnumbers[2]==three):
                    matchthree = True
                    winner = False
                    loser = False
                    matchone = False
                    matchtwo = False
                    matchfour = False
                    break
                elif (winningnumbers[0]==one and winningnumbers[1]==two):
                    matchtwo = True
                    winner = False
                    loser = False
                    matchone = False
                    matchthree = False
                    matchfour = False
                    break
                elif winningnumbers[0]==one:
                    matchone = True
                    winner = False
                    loser = False
                    matchtwo = False
                    matchthree = False
                    matchfour = False
                    break
                else:
                    loser = True
                    winner = False
                    matchone = False
                    matchtwo = False
                    matchthree = False
                    matchfour = False
                stats.append(list([winner,loser,matchone,matchtwo,matchthree,matchfour]))

                # - fix if statement above - change winnignumbers back to dict, keys 1, 2, 3
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
