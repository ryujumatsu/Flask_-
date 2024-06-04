from flask import flash, redirect, render_template, request, url_for

from flask_blog import app
from flask_blog.repository import posts_repo, users_repo
from flask_blog.views.views import login_required


@app.route("/")
@login_required
def show_posts():
    posts = posts_repo.get_all_posts()
    return render_template("posts/index.html", posts=posts)


@app.route("/<int:user_id>/posts", methods=["POST"])
@login_required
def add_post(user_id: int):
    posts_repo.create_post(user_id, request.form["title"], request.form["text"])
    flash("新しい記事が作成されました")
    return redirect(url_for("show_posts"))


@app.route("/<int:user_id>/posts/new", methods=["GET"])
@login_required
def new_post(user_id: int):
    return render_template("posts/new.html")


@app.route("/<int:user_id>/posts/<int:post_id>", methods=["GET"])
@login_required
def show_post(user_id: int, post_id: int):
    post = posts_repo.get_post_by_id(post_id)
    user = users_repo.get_user_by_id(user_id)
    return render_template("posts/show.html", post=post, user=user)


@app.route("/<int:user_id>/posts/<int:post_id>/edit", methods=["GET"])
@login_required
def edit_post(user_id: int, post_id: int):
    post = posts_repo.get_post_by_id(post_id)
    return render_template("posts/edit.html", post=post)


@app.route("/<int:user_id>/posts/<int:post_id>/update", methods=["POST"])
@login_required
def update_post(user_id: int, post_id: int):
    post = posts_repo.get_post_by_id(post_id)
    post.title = request.form["title"]
    post.text = request.form["text"]
    
    posts_repo.update_post(post)

    flash("記事が更新されました")
    return redirect(url_for("show_posts"))


@app.route("/<int:user_id>/posts/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(user_id: int, post_id: int):
    post = posts_repo.get_post_by_id(post_id)
    posts_repo.delete_post(post)

    flash("投稿が削除されました")
    return redirect(url_for("show_posts"))
