from flask import request
from model import db, Ad


REGION_LIST = [
    ('', [('Череповецкий район', 'Череповец'),
          ('Шекснинский район', 'Шексна'),
          ('Вологодский район', 'Вологда')]),

    ('Б', [('Бабаевский район', 'Бабаево'),
           ('Бабушкинский район', 'Село имени Бабушкина'),
           ('Белозерский район', 'Белозерск')]),
    ('В', [('Великоустюгский район', 'Великий Устюг'),
           ('Верховажский район', 'Верховажье'),
           ('Вожегодский район', 'Вожега'),
           ('Вологодский район', 'Вологда'),
           ('Вытегорский район', 'Вытегра')])]


def get_forms_content():
    region = request.args.get('oblast_district')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    page = request.args.get('page')
    if not region or region is None:
        region = REGION_LIST[0][1][0][0]
    if not min_price or min_price is None:
        min_price = 0
    if not max_price or max_price is None:
        max_price = Ad.query.order_by(Ad.price.desc()).first().price
    if not page or page is None:
        page = 1
    return region, min_price, max_price, page


def add_ad_in_db(info_json, actual=True):
    new_ad = Ad(info_json)
    db.session.add(new_ad, actual)
    db.session.commit()
    return new_ad.id
