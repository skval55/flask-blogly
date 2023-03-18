"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post

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
    """page to add new user"""

    return render_template("new_user.html")

@app.route('/users/new', methods=['POST'])
def post_new_user():
    """add new user and redirect ro list"""

    first_name = request.form['first_name']
    if first_name == "":
        return redirect('/users')
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    if image_url == "":
        image_url = None

    user = User (first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """shows user profile with posts"""

    user = User.query.get_or_404(user_id)
    posts = user.posts
    return render_template("user_profile.html", user=user, posts=posts )

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """edit user form"""
    
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

@app.route('/users/<int:user_id>/posts/new')
def new_post(user_id):
    """add a post"""

    user = User.query.get(user_id)
    return render_template("new_post.html", user=user)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def post_new_post(user_id):
    """posts new post to posts table and redirects to users page"""

    title = request.form['title']
    content = request.form['content']
    post = Post(title=title, content=content, user_id=user_id)

    db.session.add(post)
    db.session.commit()

    return redirect(f'/users/{user_id}')

@app.route("/posts/<int:post_id>")    
def show_post(post_id):
    """show post"""

    post = Post.query.get_or_404(post_id)

    return render_template("post.html", post=post)

@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    """edit post"""

    post = Post.query.get_or_404(post_id)

    return render_template("edit_post.html", post=post)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def post_edited_post(post_id):
    """post edited post"""

    post = Post.query.get_or_404(post_id)
    title = request.form['title']
    content = request.form['content']
    post.title = title
    post.content = content

    db.session.add(post)
    db.session.commit()

    return redirect(f'/users/{post.user.id}')


@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    """delete post and redirect back to users page"""

    post = Post.query.get_or_404(post_id)
    user_id = post.user.id
    db.session.delete(post)
    db.session.commit()

    return redirect(f'/users/{user_id}')