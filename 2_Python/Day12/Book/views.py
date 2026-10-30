from flask import render_template
from streamlit import title

from . import app

book = [
    {
        'title':'Python for Beginners',
        'author':'abc',
        'price':800
    },
    {
        'title':'Python Data Science',
        'author':'xyz',
        'price':1000
    },
    {
        'title':'Java Cookbook',
        'author':'pqr',
        'price':1200
    }
]

@app.route('/')
def home():
    # return '<h3>Welcome To My Book Store</h3>'
    return render_template('home.html',book=book)
@app.route('/about')
def about():
    # return '<h3>About Us</h3>'
    return render_template('about.html',title='About Us')

@app.route('/index')
def index():
    # return '<h3>Welcome To My Book Store</h3>'
    return render_template('index.html')

@app.route('/register')
def base():
    # return '<h3>About Us</h3>'
    return render_template('register.html')

