from . import db

class Book(do.model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(DB.String(120),nullable = False)