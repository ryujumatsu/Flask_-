from flask import request,redirect,url_for,render_template,flash,session
#__init__.pyで作成したappをインポート
from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday import db



@app.route('/result',methods=['POST'])
def result():
    holiday = Holiday.query.get(request.form['holi_date'])
    if holiday is not None:
        holiday = Holiday(
            holi_date = request.form['holi_date'],
            holi_text = request.form['holi_text']
        )
        db.session.merge(holiday)
        holi_date = request.form['holi_date']
        holi_text = request.form['holi_text']
        judge = "update"
    else:
        holiday = Holiday(
            holi_date = request.form['holi_date'],
            holi_text = request.form['holi_text']
        )
        holi_date = request.form['holi_date']
        holi_text = request.form['holi_text']
        db.session.add(holiday)
        judge = "insert"
    db.session.commit()
    return render_template('result.html', holi_date=holi_date, holi_text=holi_text, judge=judge)


@app.route('/delete',methods=['POST'])
def delete_holiday():
    holiday = Holiday.query.get(request.form['holi_date'])
    if holiday is not None:
        db.session.delete(holiday)
        db.session.commit()
        holi_date = request.form['holi_date']
        holi_text = request.form['holi_text']
        judge = "delete"
        return render_template('result.html', holi_date=holi_date, holi_text=holi_text, judge=judge)
    else:
        flash("Error:削除対象の祝日が一覧に存在しません")
        return redirect(url_for('input'))
