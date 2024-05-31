from flask import request,redirect,url_for,render_template,flash,session
#__init__.pyで作成したappをインポート
from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday import db

@app.route('/list')
def list():
    holidays = Holiday.query.order_by(Holiday.holi_date.desc()).all()
    return render_template('list.html', holidays = holidays)