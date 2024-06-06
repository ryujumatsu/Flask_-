#entries.py

from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.entries import Entry


@app.route('/entries',methods=['POST'])
def add_entry():
    entry = Entry(
        holi_date=request.form['holi_date'],
        holi_text=request.form['holi_text']
    )
    db.session.add(entry)
    db.session.commit()
    return redirect(url_for(''))

@app.route('/entries/<int:id>/delete', methods=['POST'])
def delete_entry(id):
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.comit()
    return redirect (url_for('show_entries'))

