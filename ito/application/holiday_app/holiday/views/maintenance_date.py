from flask import request,redirect,url_for,render_template,flash,session
from holiday import app,db
from holiday.models.mst_holiday import Holiday
from datetime import date


@app.route('/maintenance_date',methods=['POST'])
def add_list():
    message = ""
    dt = request.form['date']
    print(dt)
    text = request.form['text']
    if request.form["button"] == "insert_update":
        print("insert and update")
        dt_time = date(int(dt[:4]),int(dt[5:7]),int(dt[8:10]))
        is_holi_exist = Holiday.query.filter_by(holi_date=dt_time).count()
        message = f"{dt} ({text})が登録されました"
        if is_holi_exist: # update
            message = f"{dt} ({text})が更新されました"
            h = Holiday.query.filter_by(holi_date=dt_time).first()
            h.holi_text = text
            db.session.add(h)
            db.session.commit()
        else: # insert
            holiday = Holiday(
                holi_date = request.form['date'],
                holi_text = request.form['text']
            )
            db.session.add(holiday)
            db.session.commit()
    elif request.form["button"] == "delete":
        holi = Holiday.query.get(dt)
        
        db.session.delete(holi)
        db.session.commit()
        message = f"{holi.holi_text}が削除されました"
    
    return render_template('result.html',massage=message)