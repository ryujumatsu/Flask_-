import hashlib
from typing import Optional

from flask_blog import db
from flask_blog.models.users import User


def create_user(name: str, password: str) -> User:
    user = User(name, password)
    db.session.add(user)
    db.session.commit()
    return user


def get_user_by_id(user_id: int) -> Optional[User]:
    return User.query.get(user_id)


def get_user_by_name(name: str) -> Optional[User]:
    return db.session.query(User).filter(User.name == name).first()


def delete_user_by_id(id: int) -> None:
    db.session.query(User).filter(User.id == id).delete()
    db.session.commit()
    return


def does_password_match(user: User, plain_password: str) -> bool:
    hashed = hashlib.md5(plain_password.encode()).hexdigest()
    return user.password == hashed
