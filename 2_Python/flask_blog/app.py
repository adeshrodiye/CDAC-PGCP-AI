"""
Flask Blogging Website with Login System
Main application file - contains app config and all routes.
"""

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import (
    LoginManager, login_user, login_required,
    logout_user, current_user
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from models import db, User, Post, CATEGORIES

# ---------------------------------------------------------------------
# App configuration
# ---------------------------------------------------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-secret-key-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# Make the category list available in every template (used by the nav bar)
@app.context_processor
def inject_categories():
    return dict(all_categories=CATEGORIES)


# ---------------------------------------------------------------------
# Public routes
# ---------------------------------------------------------------------
@app.route('/')
def index():
    selected_category = request.args.get('category', 'All')

    query = Post.query.order_by(Post.date_posted.desc())
    if selected_category != 'All':
        query = query.filter_by(category=selected_category)
    posts = query.all()

    featured = None
    if selected_category == 'All' and posts:
        featured = posts[0]
        posts = posts[1:]

    return render_template(
        'index.html',
        posts=posts,
        featured=featured,
        selected_category=selected_category
    )


@app.route('/post/<int:post_id>')
def post(post_id):
    single_post = db.session.get(Post, post_id)
    if single_post is None:
        flash('Post not found.', 'danger')
        return redirect(url_for('index'))
    return render_template('post.html', post=single_post)


# ---------------------------------------------------------------------
# Auth routes
# ---------------------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm_password', '')

        if not username or not email or not password:
            flash('All fields are required.', 'danger')
            return redirect(url_for('register'))

        if password != confirm:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('register'))

        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


# ---------------------------------------------------------------------
# User profile
# ---------------------------------------------------------------------
@app.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User not found.', 'danger')
        return redirect(url_for('index'))

    user_posts = Post.query.filter_by(user_id=user.id) \
        .order_by(Post.date_posted.desc()).all()

    return render_template('profile.html', profile_user=user, posts=user_posts)


@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        current_user.bio = request.form.get('bio', '').strip()
        db.session.commit()
        flash('Profile updated!', 'success')
        return redirect(url_for('profile', username=current_user.username))

    return render_template('edit_profile.html')


# ---------------------------------------------------------------------
# Blog post CRUD (login required)
# ---------------------------------------------------------------------
@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        category = request.form.get('category', CATEGORIES[0])
        image_url = request.form.get('image_url', '').strip() or None

        if not title or not content:
            flash('Title and content are required.', 'danger')
            return redirect(url_for('create_post'))

        if category not in CATEGORIES:
            category = CATEGORIES[0]

        new_post = Post(
            title=title,
            content=content,
            category=category,
            image_url=image_url,
            date_posted=datetime.utcnow(),
            author=current_user
        )
        db.session.add(new_post)
        db.session.commit()

        flash('Post published!', 'success')
        return redirect(url_for('index'))

    return render_template('create_post.html', categories=CATEGORIES)


@app.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    single_post = db.session.get(Post, post_id)
    if single_post is None:
        flash('Post not found.', 'danger')
        return redirect(url_for('index'))

    if single_post.author != current_user:
        flash('You can only edit your own posts.', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        single_post.title = request.form.get('title', '').strip()
        single_post.content = request.form.get('content', '').strip()
        category = request.form.get('category', single_post.category)
        single_post.category = category if category in CATEGORIES else single_post.category
        single_post.image_url = request.form.get('image_url', '').strip() or None
        db.session.commit()
        flash('Post updated!', 'success')
        return redirect(url_for('post', post_id=single_post.id))

    return render_template('create_post.html', post=single_post, categories=CATEGORIES)


@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    single_post = db.session.get(Post, post_id)
    if single_post is None:
        flash('Post not found.', 'danger')
        return redirect(url_for('index'))

    if single_post.author != current_user:
        flash('You can only delete your own posts.', 'danger')
        return redirect(url_for('index'))

    db.session.delete(single_post)
    db.session.commit()
    flash('Post deleted.', 'info')
    return redirect(url_for('index'))


# ---------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
