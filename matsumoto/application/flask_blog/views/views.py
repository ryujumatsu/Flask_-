from functools import wraps
import hashlib

from flask import flash, redirect, render_template, request, session, url_for

from flask_blog import app
from flask_blog.repository import users_repo


def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    
    return inner


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        hashed = hashlib.md5(password.encode()).hexdigest()

        user = users_repo.create_user(name, hashed)
        if user is None:
            flash("登録に失敗しました")
            return render_template("signup.html")
        else:
            session["logged_in"] = True
            session["id"] = user.id
            flash("登録に成功しました")
            return redirect(url_for("show_posts"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = users_repo.get_user_by_name(request.form["username"])
        if user is None:
            flash("ユーザー名が登録されていません")
        else:
            if not users_repo.does_password_match(user, request.form["password"]):
                flash("パスワードが異なります")
            else:
                session["logged_in"] = True
                session["id"] = user.id
                flash("ログインしました")
                return redirect(url_for("show_posts"))

    else:
        if session.get("logged_in"):
            return redirect(url_for("show_posts"))
        
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    session.pop("id", None)
    flash("ログアウトしました")
    return redirect(url_for("login"))
    