from flask import request,redirect,url_for,render_template,flash,request,session
from salary import app
from func_salary import calcsalary
import re

@app.route('/') #()内のアドレスにアクセスした際に、以下の指示を実行する。
def input():
    init_val=session.get("input_data",None)
    return render_template('input.html',input_data=init_val)
    
@app.route('/output',methods=['POST']) #()内のアドレスにアクセスした際に、以下の指示を実行する。
def output():
    session["input_data"]=request.form['salary']
    if request.form['salary']=='':
        flash('給料が未入力です。入力してください')
        return redirect(url_for('input'))
    if re.fullmatch('[0-9]+',request.form['salary'])== None:
        flash('数値を入力してください')
        return redirect(url_for('input'))
    if int(request.form['salary'])>999999999 or int(request.form['salary'])<0:
        flash('入力できる値は0円から999,999,999円までです。')
        return redirect(url_for('input'))
    else:
        input_salary=request.form.get('salary')
        results=calcsalary(input_salary)
        result_pay=results[0]
        result_tax=results[1]
        return render_template('output.html',salary=input_salary,pay=result_pay,tax=result_tax)
