"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    app.app_context().push()

default_img = "https://icon-library.com/images/image-missing-icon/image-missing-icon-15.jpg"

class User(db.Model):
    """user"""

    __tablename__ = "users"

    id = db.Column(db.Integer, 
        primary_key = True,
        autoincrement = True)
    first_name = db.Column(db.String(20),
                    nullable=False)
    last_name = db.Column(db.String(20))
    image_url = db.Column(db.Text, nullable=False, default=default_img)


class Post(db.Model):
    """post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, 
        primary_key = True,
        autoincrement = True)
    title = db.Column(db.String(50),
                    nullable=False)
    content = db.Column(db.String,
                    nullable=False)
    created_at = db.Column(db.TIMESTAMP)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref='posts')

