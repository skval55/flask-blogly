"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
# db.drop_all()
# db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

@app.route("/")
def redirect_to_users():
    """redirects to users page"""

    return redirect('/users')

@app.route('/users')
def list_users():
    """list users on page with button to add user"""

    users = User.query.all()
    return render_template("users.html", users=users )

@app.route('/users/new')
def new_user():
    """list users on page with button to add user"""

    return render_template("new_user.html")

@app.route('/users/new', methods=['POST'])
def post_new_user():
    """add new user and redirect ro list"""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User (first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """list users on page with button to add user"""

    user = User.query.get_or_404(user_id)
    if user.image_url == "":
        user.image_url = 'https://icon-library.com/images/image-missing-icon/image-missing-icon-15.jpg'
    return render_template("user_profile.html", user=user )

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    
    user = User.query.get(user_id)
    return render_template("edit_user.html", user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def post_edited_user(user_id):
    """post edits made to /users"""

    user = User.query.get(user_id)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """delete user and redirect to /users"""
 

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')