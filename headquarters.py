import os



from flask import Flask
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:#breakingMoons~@127.0.0.1:5432/PHFCC'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.secret_key = 'wastedPenguin27.'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
heroku = Heroku(app)
