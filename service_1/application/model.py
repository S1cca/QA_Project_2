from application import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classes = db.Column(db.String(80), nullable=False)   # Service 2
    gender = db.Column(db.String(80), nullable=False)    # Service 3
    subclass = db.Column(db.String(80), nullable=False)  # Service 4
    birth_place = db.Column(db.String(80), nullable=False) # Service 4
    