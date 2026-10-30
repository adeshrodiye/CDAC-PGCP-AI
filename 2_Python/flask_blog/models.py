"""
Database models for the blogging website.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# Fixed list of categories used across the app (nav filter, post form, seed data)
CATEGORIES = [
    "Technology",
    "Travel",
    "Food",
    "Lifestyle",
    "Business",
    "Health",
]


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.Text, default='')
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    posts = db.relationship('Post', backref='author', lazy=True,
                             cascade='all, delete-orphan')

    @property
    def avatar_url(self):
        # Auto-generated avatar based on username initials - no upload needed
        return f"https://ui-avatars.com/api/?name={self.username}&background=6c5ce7&color=fff&size=128&bold=true"

    def __repr__(self):
        return f'<User {self.username}>'


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), default='Lifestyle', nullable=False)
    image_url = db.Column(db.String(400), nullable=True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def display_image(self):
        # Falls back to a deterministic placeholder image if the author didn't set one
        return self.image_url or f"https://picsum.photos/seed/post{self.id}/700/450"

    @property
    def excerpt(self):
        return self.content[:150] + ('...' if len(self.content) > 150 else '')

    def __repr__(self):
        return f'<Post {self.title}>'
