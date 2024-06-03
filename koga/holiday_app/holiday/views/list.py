from holiday.models.mst_holiday import Holiday
from flask import request,redirect,url_for,render_template,flash,request,session
from holiday import app

@app.route('/result',methods=['GET'])
def list():
    datelist=Holiday.query.order_by(Holiday.holi_date.desc()).all()
    print(datelist)
    return render_template('list.html',datelistHTML=datelist) #HTMLに射影したリストを渡す。

