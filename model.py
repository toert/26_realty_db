from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

REGION_LIST = [
    {'letter': '', 'districts': [('Череповецкий район', 'Череповец'),
                                 ('Шекснинский район', 'Шексна'),
                                 ('Вологодский район', 'Вологда')]},

    {'letter': 'Б', 'districts': [('Бабаевский район', 'Бабаево'),
                                  ('Бабушкинский район', 'Село имени Бабушкина'),
                                  ('Белозерский район', 'Белозерск')]},

    {'letter': 'В', 'districts': [('Великоустюгский район', 'Великий Устюг'),
                                  ('Верховажский район', 'Верховажье'),
                                  ('Вожегодский район', 'Вожега'),
                                  ('Вологодский район', 'Вологда'),
                                  ('Вытегорский район', 'Вытегра')]}]


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


def add_ad_in_db(info_json, actual=True):
    new_ad = Ad(info_json)
    db.session.add(new_ad, actual)
    db.session.commit()
    return new_ad.id


def create_ad_from_dict(new_json, actual):
    new_ad = Ad()
    new_ad.actual = actual
    new_ad.id = new_json['id']
    new_ad.settlement = new_json['settlement']
    new_ad.under_construction = new_json['under_construction']
    new_ad.description = new_json['description']
    new_ad.price = new_json['price']
    new_ad.oblast_district = new_json['oblast_district']
    new_ad.living_area = new_json['living_area']
    new_ad.has_balcony = new_json['has_balcony']
    new_ad.address = new_json['address']
    new_ad.construction_year = new_json['construction_year']
    new_ad.rooms_number = new_json['rooms_number']
    new_ad.premise_area = new_json['premise_area']
    return new_ad
