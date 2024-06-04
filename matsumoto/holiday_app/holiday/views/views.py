from flask import flash, redirect, render_template, request, url_for
from holiday import app, repository


@app.route("/")
def input():
    return render_template("input.html")


@app.route("/maintenance_date")
def output():
    return render_template("output.html")


@app.route("/create", methods=["POST"])
def create():
    holi_date = request.form["holi_date"]
    holi_text = request.form["holi_text"]

    if repository.get_holiday_by_date(holi_date):
        repository.update_holiday(holi_date, holi_text)
        flash("{}は「{}」に更新されました".format(holi_date, holi_text))
    else:
        repository.create_holiday(holi_date, holi_text)
        flash("{} ({}) が登録されました".format(holi_date, holi_text))
    
    return redirect(url_for("output"))


@app.route("/delete", methods=["POST"])
def delete():
    holi_date = request.form["holi_date"]

    holi_text = repository.delete_holiday(holi_date)
    if holi_text:
        flash("{} ({}) は、削除されました".format(holi_date, holi_text))
        return redirect(url_for("output"))
    else:
        flash("{}は、祝日マスタに登録されていません".format(holi_date))
        return redirect(url_for("input"))

@app.route("/list")
def show_list():
    holidays = repository.get_all()
    return render_template("list.html", holidays=holidays)
