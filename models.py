from datetime import datetime
from app import app
from headquarters import db

from flask_login import UserMixin






class Users(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)


    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def get_id(self):
        try:
            return str(self.id).encode("utf-8").decode("utf-8")
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __repr__(self):
        return 'ID#: {0}, User: {1}, Password: ***{2}, Email: {3}'.format(self.id, self.name, self.password[3:], self.email)




class Sermon(db.Model):
    __tablename__ = 'sermon'

    id                      = db.Column(db.Integer, primary_key=True)
    sundayTitle             = db.Column(db.String(250))
    sundayTime              = db.Column(db.DateTime, index=True, 
                                        default=datetime.utcnow)
    bookOne                 = db.Column(db.String(100))
    bookTwo                 = db.Column(db.String(100))
    bookThree               = db.Column(db.String(100))
    bookFour                = db.Column(db.String(100))
    verseOne                = db.Column(db.String(100))
    verseTwo                = db.Column(db.String(100))
    verseThree              = db.Column(db.String(100))
    verseFour               = db.Column(db.String(100))
    sermon                  = db.Column(db.String(250))
    adultBibleClass         = db.Column(db.String(250))
    bibleClassTeacher       = db.Column(db.String(100))
    
    
    def __init__(
        self, sundayTitle, bookOne, 
        bookTwo, bookThree, bookFour,
        verseOne, verseTwo, verseThree,
        verseFour, sermon, adultBibleClass,
        bibleClassTeacher):

        self.sundayTitle        = sundayTitle
        self.bookOne            = bookOne
        self.bookTwo            = bookTwo
        self.bookThree          = bookThree
        self.bookFour           = bookFour
        self.verseOne           = verseOne
        self.verseTwo           = verseTwo
        self.verseThree         = verseThree
        self.verseFour          = verseFour
        self.sermon             = sermon
        self.adultBibleClass    = adultBibleClass
        self.bibleClassTeacher  = bibleClassTeacher



    def __repr__(self):
        return '{0}, SundayTitle={1}, BibleClass={2}>'.format(
                                                self.sundayTime, 
                                                self.sundayTitle, 
                                                self.adultBibleClass)

class Serving(db.Model):
    __tablename__ = 'serving'

    id                      = db.Column(db.Integer, primary_key=True)
    servingTime             = db.Column(db.DateTime, index=True, 
                                        default=datetime.utcnow)
    eldersThis              = db.Column(db.String(250))
    eldersNext              = db.Column(db.String(250))
    shutInMonth             = db.Column(db.String(250))
    deaconThis              = db.Column(db.String(250))
    deaconNext              = db.Column(db.String(250))
    doorThis                = db.Column(db.String(100))
    doorNext                = db.Column(db.String(100))
    narnexThis              = db.Column(db.String(100))
    narnexNext              = db.Column(db.String(100))
    cleanUpThis             = db.Column(db.String(100))
    cleanUpNext             = db.Column(db.String(100))
    
    
    def __init__(
        self, eldersThis, eldersNext,
        shutInMonth, deaconThis, deaconNext,
        doorThis, doorNext, narnexThis, narnexNext,
        cleanUpThis, cleanUpNext):

        self.eldersThis         = eldersThis
        self.eldersNext         = eldersNext
        self.shutInMonth        = shutInMonth
        self.deaconThis         = deaconThis
        self.deaconNext         = deaconNext
        self.doorThis           = doorThis
        self.doorNext           = doorNext
        self.narnexThis         = narnexThis
        self.narnexNext         = narnexNext
        self.cleanUpThis        = cleanUpThis
        self.cleanUpNext        = cleanUpNext



    def __repr__(self):
        return '{0}, {1},{2}'.format( self.eldersThis,self.deaconThis, 
                                      self.narnexThis)
                                      
class Date(db.Model):
    __tablename__ = 'date'
    
    id        = db.Column(db.Integer, primary_key=True)
    dateTime  = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    month     = db.Column(db.String(100))
    year      = db.Column(db.String(100))
    date      = db.Column(db.String(100))
    
    def __init__(self, month, year, date):
        self.month = month
        self.year = year
        self.date = date
        
    def __repr__(self):
        return '{0} {1} {2}'.format(date, month, year)
    
    
    
    
db.create_all()



