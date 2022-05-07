from application import db


class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classes_name = db.Column(db.String(80), nullable=False)
    Character_gender = db.Column(db.String(80), nullable=False)
    