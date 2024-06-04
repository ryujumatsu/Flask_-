from typing import Optional

from flask_blog import db
from flask_blog.models.posts import Post
from flask_blog.models.users import User


def create_post(user_id: int, title: str, text: str) -> Optional[Post]:
    post = Post(
        user_id=user_id,
        title=title,
        text=text
    )

    post = db.session.add(post)
    db.session.commit()
    return post


def get_all_posts() -> list[Post]:
    return (db.session.query(Post, User).
            join(User, Post.user_id == User.id).
            order_by(Post.id.desc()).
            all())


def get_post_by_id(post_id: int) -> Optional[Post]:
    return Post.query.get(post_id)


def update_post(post: Post) -> None:
    db.session.merge(post)
    db.session.commit()
    return


def delete_post(post: Post) -> None:
    db.session.delete(post)
    db.session.commit()
    return
