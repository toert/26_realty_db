from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Ad(db.Model):
    actual = db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key=True)
    settlement = db.Column(db.String(80))
    under_construction = db.Column(db.Boolean)
    description = db.Column(db.String(80))
    price = db.Column(db.Integer)
    oblast_district = db.Column(db.String(80))
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean)
    address = db.Column(db.String(80))
    construction_year = db.Column(db.Integer)
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float)

    def __init__(self, new_json, actual):
        self.actual = actual
        self.id = new_json['id']
        self.settlement = new_json['settlement']
        self.under_construction = new_json['under_construction']
        self.description = new_json['description']
        self.price = new_json['price']
        self.oblast_district = new_json['oblast_district']
        self.living_area = new_json['living_area']
        self.has_balcony = new_json['has_balcony']
        self.address = new_json['address']
        self.construction_year = new_json['construction_year']
        self.rooms_number = new_json['rooms_number']
        self.premise_area = new_json['premise_area']