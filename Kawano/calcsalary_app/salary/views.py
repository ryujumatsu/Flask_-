from flask import request,redirect,url_for,render_template,flash,session
#__init__.pyで作成したappをインポート
from salary import app
import re
#URLアクセスがあったときの処理

@app.route('/',methods=['GET','POST'])
def input():
    init_value = session.get("input_salary", None)
    return render_template('input.html' , input_salary=init_value)
    
@app.route('/output',methods=['GET','POST'])
def output():
    form_salary = request.form['salary']
    if int(form_salary) <= 0:
        flash(f"Error:給与は正の整数を入力してください  エラー値:{form_salary}")
        session['input_salary'] = form_salary
        return redirect(url_for('input'))
    elif len(form_salary) == 0:
        flash(f"Error:値が入力されていません  エラー値:{form_salary}")
        session['input_salary'] = form_salary
        return redirect(url_for('input'))
    elif len(form_salary) > 10:
        flash(f"Error:給与は最大9,999,999,999まで入力可能です")
        session['input_salary'] = form_salary
        return redirect(url_for('input'))
    elif re.fullmatch('[0-9]+', form_salary) == None:
        flash(f"数字を入力してください")
        session['input_salary'] = form_salary
        return redirect(url_for('input'))
    if request.method != "" :
        input_salary = int(form_salary) 
        if input_salary > 1000000:
            tax = (input_salary -1000000)*0.2 + 1000000*0.1
            supply = input_salary - tax
        elif input_salary <= 1000000:
            tax = int(input_salary*0.1)
            supply = int(input_salary - tax)
        tax = "{:,.0f}".format(tax)
        supply = "{:,.0f}".format(supply)
        input_salary = "{:,.0f}".format(input_salary)
        session['input_salary'] = None
    return render_template('output.html',salary=input_salary,supply=supply,tax=tax)
    
   


