from flask import request,redirect,url_for,render_template,flash,request,session
from holiday import app,db
from holiday.models.mst_holiday import Holiday
from holiday.views.maintenance_holiday import judge_input


@app.route('/result',methods=['POST']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
def result():
    if request.form['input_date']=='' or request.form['input_text']=='':
        flash('日付又は名称が未入力です。入力してください。')
        return redirect(url_for('input'))
    if len(request.form['input_text'])>21:
        flash('名称は20文字以内で入力してください。')
        return redirect(url_for('input'))
    else:
        J=judge_input(request.form['input_date'],request.form['input_text'])
        if J == 0:#祝日被りエラー
            flash('その日程は既に登録されています。')
            return render_template('input.html')      
        if J == 1:#祝日のテキスト情報更新
            holiday = db.session.query(Holiday.holi_text).filter_by(holi_date=request.form['input_date']).first()
            holiday.holi_text = request.form['input_text']
            db.session.add(holiday)
            db.session.commit()
            return render_template('result.html',holiday=holiday)
        if J == 2:#祝日の新規登録
            holiday = Holiday(holi_date=request.form['input_date'],holi_text=request.form['input_text'])
            db.session.add(holiday)
            db.session.commit()
            return render_template('result.html',holiday=holiday)
