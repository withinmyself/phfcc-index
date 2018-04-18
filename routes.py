

from models import Users, Sermon, Serving, Date
from flask import render_template, redirect, flash, request
from headquarters import db
from app import app



@app.route('/', methods=['GET', 'POST'])
def phfcc():
    sermon = db.session.query(Sermon).first()
    serving = db.session.query(Serving).first()
    return render_template('phfcc.html', sermon=sermon, serving=serving)


@app.route('/goto')
def goto():
    return render_template('goto.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/start_suns')
def start_suns():
    return render_template('wearing-suns.html')

@app.route('/wearing_suns', methods=['GET', 'POST'])
def wearing_suns():
    sundayTitle=request.form['sundayTitle']
    bookOne=request.form['bookOne']
    bookTwo=request.form['bookTwo']
    bookThree=request.form['bookThree']
    bookFour=request.form['bookFour']
    verseOne=request.form['verseOne']
    verseTwo=request.form['verseTwo']
    verseThree=request.form['verseThree']
    verseFour=request.form['verseFour']
    sermon=request.form['sermon']
    adultBibleClass=request.form['adultBibleClass']
    bibleClassTeacher=request.form['bibleClassTeacher']
    currentSermon = db.session.query(Sermon).first()
    
    if currentSermon == None or currentSermon == '':
        sermon = Sermon(sundayTitle=sundayTitle, bookOne=bookOne,
                        bookTwo=bookTwo, bookThree=bookThree,
                        bookFour=bookFour, verseOne=verseOne,
                        verseTwo=verseTwo, verseThree=verseThree,
                        verseFour=verseFour, sermon=sermon,
                        adultBibleClass=adultBibleClass,
                        bibleClassTeacher=bibleClassTeacher)
        db.session.add(sermon)
        db.session.commit()
        return render_template('verify-suns.html', sermon=sermon)
    
    else:
        if sundayTitle == None or sundayTitle == '':
            sundayTitle = currentSermon.sundayTitle
        if bookOne == None or bookOne == '':
            bookOne = currentSermon.bookOne
        if bookTwo == None or bookTwo == '':
            bookTwo = currentSermon.bookTwo
        if bookThree == None or bookThree == '':
            bookThree = currentSermon.bookThree
        if bookFour == None or bookFour == '':
            bookFour = currentSermon.bookFour
        if verseOne == None or verseOne == '':
            verseOne = currentSermon.verseOne
        if verseTwo == None or verseTwo == '':
            verseTwo = currentSermon.verseTwo
        if verseThree == None or verseThree == '':
            verseThree = currentSermon.verseThree
        if verseFour == None or verseFour == '':
            verseFour = currentSermon.verseFour
        if sermon == None or sermon == '':
            sermon = currentSermon.sermon
        if adultBibleClass == None or adultBibleClass == '':
            adultBibleClass = currentSermon.adultBibleClass
        if bibleClassTeacher == None or bibleClassTeacher == '':
            bibleClassTeacher = currentSermon.bibleClassTeacher
        db.session.query(Sermon).filter_by(sundayTime=currentSermon.sundayTime).delete()
        sermon = Sermon(sundayTitle=sundayTitle, bookOne=bookOne,
                        bookTwo=bookTwo, bookThree=bookThree,
                        bookFour=bookFour, verseOne=verseOne,
                        verseTwo=verseTwo, verseThree=verseThree,
                        verseFour=verseFour, sermon=sermon,
                        adultBibleClass=adultBibleClass,
                        bibleClassTeacher=bibleClassTeacher)

        db.session.add(sermon)
        db.session.commit()
        return render_template('verify-suns.html', sermon=sermon)

@app.route('/about_suns')
def about_suns():
    return render_template('wonderful-suns.html')

@app.route('/wonderful-suns', methods=['GET', 'POST'])
def wonderful_suns():
    eldersThis=request.form['eldersThis']
    eldersNext=request.form['eldersNext']
    shutInMonth=request.form['shutInMonth']
    deaconThis=request.form['deaconThis']
    deaconNext=request.form['deaconNext']
    doorThis=request.form['doorThis']
    doorNext=request.form['doorNext']
    narnexThis=request.form['narnexThis']
    narnexNext=request.form['narnexNext']
    cleanUpThis=request.form['cleanUpThis']
    cleanUpNext=request.form['cleanUpNext']
    currentServing = db.session.query(Serving).first()
    if currentServing == None or currentServing == '':
        serving = Serving(eldersThis=eldersThis, eldersNext=eldersNext,
                          shutInMonth=shutInMonth, deaconThis=deaconThis,
                          deaconNext=deaconNext, doorThis=doorThis,
                          doorNext=doorNext, narnexThis=narnexThis,
                          narnexNext=narnexNext, cleanUpThis=cleanUpThis,
                          cleanUpNext=cleanUpNext)
        db.session.add(serving)
        db.session.commit()
        return render_template ('vilify-suns.html', serving=serving, month="April", weekOf="April 18 2018")
    else:
        if eldersThis == None or eldersThis == '':
            eldersThis = currentServing.eldersThis
        if eldersNext == None or eldersNext == '':
            eldersNext = currentServing.eldersNext
        if shutInMonth == None or shutInMonth == '':
            shutInMonth = currentServing.shutInMonth
        if deaconThis == None or deaconThis == '':
            deaconThis = currentServing.deaconThis
        if deaconNext == None or deaconNext == '':
            deaconNext = currentServing.deaconNext
        if doorThis == None or doorThis == '':
            doorThis = currentServing.doorThis
        if doorNext == None or doorNext == '':
            doorNext = currentServing.doorNext
        if narnexThis == None or narnexThis == '':
            narnexThis = currentServing.narnexThis
        if narnexNext == None or narnexNext == '':
            narnexNext = currentServing.narnexNext
        if cleanUpThis == None or cleanUpThis == '':
            cleanUpThis = currentServing.cleanUpThis
        if cleanUpNext == None or cleanUpNext == '':
            cleanUpNext = currentServing.cleanUpNext
        db.session.query(Serving).filter_by(servingTime=currentServing.servingTime).delete()
        serving = Serving(eldersThis=eldersThis, eldersNext=eldersNext,
                          shutInMonth=shutInMonth, deaconThis=deaconThis,
                          deaconNext=deaconNext, doorThis=doorThis,
                          doorNext=doorNext, narnexThis=narnexThis,
                          narnexNext=narnexNext, cleanUpThis=cleanUpThis,
                          cleanUpNext=cleanUpNext)

        db.session.add(serving)
        db.session.commit()
        return render_template ('vilify-suns.html', serving=serving, month="April", weekOf="April 18 2018")

@app.route('/about_time')
def about_time():
    return render_template('about-time.html')

@app.route('/alter_time', methods=['GET', 'POST'])
def alter_time():
    date = request.form['date']
    month = request.form['month']
    year = request.form['year']
    date_full = db.session.query(Date).first()
    if date_full == None or date_full == '':
        date = Date(date=date, month=month, year=year)
        db.session.add(date)
        db.session.commit()
        return render_template('final-date.html', date=date)
    else:
        if date == None or date == '':
            date = date_full.date
        if month == None or month == '':
            month = date_full.month
        if year == None or year == '':
            year = date_full.year
        db.session.query(Date).filter_by(dateTime=date_full.dateTime).delete()
        date = Date(date=date, month=month, year=year)
        db.session.add(date)
        db.session.commit()
        return render_template('final-date.html', date=date)
