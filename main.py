from flask import Flask, render_template
from sqlalchemy import Column, Integer, String


app = Flask(__name__)




@app.route('/profile')
def profile():
    x = 0
    shop = []
    while x < 5:
        temp = input()
        shop.append(str(temp))
        x = x + 1

    return render_template('profile.html', shop=shop)

@app.route('/')
def phfcc():
    return render_template('phfcc.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)