from application import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Classes = db.Column(db.String(80), nullable=False)   # Service 2
    Gender = db.Column(db.String(80), nullable=False)    # Service 3
    SubClass = db.Column(db.String(80), nullable=False)  # Service 4
    BirthPlace = db.Column(db.String(80), nullable=False) # Service 4
    