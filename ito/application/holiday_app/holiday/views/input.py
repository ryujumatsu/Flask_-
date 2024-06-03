from flask import request,redirect,url_for,render_template,flash,session
from holiday import app
# from decimal import Decimal,ROUND_HALF_UP

@app.route('/')
def show_entries():
    print("show entries")
    return render_template('input.html')