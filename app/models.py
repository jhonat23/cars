from io import BufferedRandom
from main import db

#models
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.Integer, nullable=False)
    cv = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    seller_id = db.Column(db.Integer, db.ForeginKey('seller.id'), nullable=False)
    seller = db.relationship('Seller', backref=db.backref('cars', lazy=True))

class Seller(db.Model):
    id = db.Column(db.Integer, prmary_key=True)
    name = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

