from flask import Flask, render_template
app = Flask(__name__)
from forms import LoginForm


@app.route('/')
def phfcc():
    return render_template('phfcc.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')
	
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run()