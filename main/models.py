from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64))


class Album(db.Model):
    __tablename__ = 'galleries'

    id = db.Column(db.String(128), primary_key=True)
    link = db.Column(db.String(256))
    author_id = db.Column(db.ForeignKey('users.id'))
    author = db.relationship('User', backref='galleries')
