from kmujournal.model import User
from kmujournal import db


def query(model, **kwargs):
    return model.query.filter_by(**kwargs).first()


def delete(obj):
    db.session.delete(obj)
    commit()


def delete_user(user_key):
    user = query(User, user_key=user_key)
    if user:
        delete(user)
        return 0
    else:
        return 1


def add(obj):
    db.session.add(obj)
    commit()


def add_user(user_key):
    user = query(User, user_key=user_key)
    if not user:
        user = User(user_key)
        add(user)


def commit():
    db.session.commit()

def return_status(user_key):
    user = query(User, user_key=user_key)
    if not user:
        return u'true'
    else:
        return user.status

def change_status(user_key):
    user = query(User, user_key=user_key)
    if user.status:
        user.status = False
        commit()
    else:
        user.status = True
        commit()
