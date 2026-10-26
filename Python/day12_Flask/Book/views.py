from flask import render_template
from sympy.physics.units import meter
from twisted.protocols.sip import Registration

from . import app
from .models import Book



# books=[
#     {"title":"Python for begineer",
#      "author":"abc","price":800},
#     {"title":"Python for data science", "author":"xyz","price": 900},
#     {
#         "title":"Java cookbook",
#         "price":5000,
#         "author":"dfd"
#     }
# ]



@app.route("/")
def home():
    books = Book.query.all()
    title = "GreatestStore"
    return render_template("home.html", book=books, title=title)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/book/<int:book_id>")
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template("book_details.html",book=book)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('register.html', title='Register',form=form)