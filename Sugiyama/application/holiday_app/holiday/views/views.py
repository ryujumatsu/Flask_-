#views.py

from flask import request, redirect,url_for,render_template,flash,session
from holiday import app, db
from holiday.models.entries import Entry

@app.route('/',methods=['GET','POST'])
def start():
    return render_template('input.html')


@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        holidate = request.form['holidate']
        holitext = request.form['holitext']
        entry = Entry(
            holi_date=request.form['holidate'],
            holi_text=request.form['holitext']
        )
        db.session.add(entry)
        db.session.commit()
        flash('{}は「{}」に更新されました'.format(holidate, holitext))
    return render_template('output.html',holidate = holidate, holitext=holitext)

@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        holidate = request.form['holidate']
        holitext = request.form['holitext']
        entry = Entry.query.get(holidate)
        db.session.delete(entry)
        db.session.commit()
        flash('{}（{}）は削除されました'.format(holidate, holitext))
    return render_template('output.html',holidate = holidate, holitext=holitext)
