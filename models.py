"""Models for Blogly."""
from datetime import datetime, date
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
    created_at = db.Column(db.DateTime,
        nullable=False,
        default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref='posts')

    tags = db.relationship('Tag', secondary= 'post_tags', backref='posts')


class PostTag(db.Model):
    """post tags"""

    __tablename__ = "post_tags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key = True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key = True)


class Tag(db.Model):
    """tags"""

    __tablename__ = "tags"

    id = db.Column(db.Integer, 
                    primary_key = True,
                    autoincrement = True)
    name = db.Column(db.String, unique = True)