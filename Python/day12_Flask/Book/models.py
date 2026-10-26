from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120),nullable=False)
    author= db.Column(db.String(120),nullable=False)
    price = db.Column(db.Integer,nullable=False)


    def __repr__(self):
        return f"{self.title}"