from flask import request,redirect,url_for,render_template,flash,session
from holiday import app
# from decimal import Decimal,ROUND_HALF_UP

@app.route('/')
def show_entries():
    print("show entries")
    return render_template('input.html')


# @app.route('/input',methods=['GET','POST'])
# def input():
#     init_val = session.get("input_data",None)
#     return render_template('input.html',salary=init_val)

# @app.route('/output',methods=['GET','POST'])
# def output():
#     if request.method == 'POST':    
#         input_salary = request.form['salary']

#         if is_output_error(input_salary):
#             return redirect(url_for("input"))

#         input_price,input_tax = calc_salary(int(input_salary))
#         return render_template('output.html',salary=int(input_salary),price=input_price,tax=input_tax)
#     return redirect(url_for('input',salary=1000))


# def is_output_error(val):
#     if val == '':
#         flash("給与が未入力です。入力してください。")
#         return True
#     if int(val) > 1e10:
#         session["input_data"] = val
#         flash('給与は最大9,999,999,999まで入力可能です')
#         return True
#     if int(val) < 0:
#         session["input_data"] = val
#         flash('給与にはマイナスの値は入力できません')
#         return True
#     return False

# def calc_salary(val):    
#     max = 1e6
#     tax = 0
#     if val > max:
#         tax = (max * 0.1 + (val - max) * 0.2)
#     else:
#         tax = val * 0.1

#     tax = int(Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))
#     price = val - tax
#     return price,tax