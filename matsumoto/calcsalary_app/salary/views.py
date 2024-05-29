from decimal import Decimal, ROUND_HALF_UP
from flask import flash, redirect, render_template, request, session, url_for
from salary import app

@app.route("/", methods=["GET", "POST"])
def input():
    # POST method.
    if request.method == "POST":
        salary = request.form["salary"]
        if validate_salary(salary):
            output = calc_salary(int(salary))
            session["output"] = output
            return redirect(url_for("output"))
        
        else:
            session["input"] = salary
            return redirect(url_for("input"))
    
    # GET method.
    else:
        input = session.pop("input", None)
        return render_template("input.html", input=input)

@app.route("/output")
def output():
    output = session.pop("output", None)
    return render_template("output.html", output=output)

def validate_salary(salary: str) -> bool:
    if salary == "":
        flash("給与が未入力です。入力してください。")
        return False
    
    if len(salary) > 10:
        flash("給与には最大9,999,999,999まで入力可能です。")
        return False
    
    if int(salary) < 0:
        flash("給与にはマイナスの値は入力できません。")
        return False
    
    return True

def calc_salary(salary: int) -> str:
    if salary > 1000000:
        tax = (salary - 1000000)*0.2 + 1000000*0.1
    else:
        tax = salary * 0.1

    tax = Decimal(tax).quantize(Decimal(0), rounding=ROUND_HALF_UP)
    return "給与：{:,}円の場合、支給額：{:,}円、税額：{:,}円です。".format(salary, salary - tax, tax)
