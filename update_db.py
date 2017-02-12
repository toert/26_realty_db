from requests import get
from model import add_ad_in_db
from server import db, Ad, app


URL_ACTUAL_ADS = 'https://devman.org/assets/ads.json'


def get_new_loads():
    return get(URL_ACTUAL_ADS).json()


def reset_actual():
    all_ads_from_db = Ad.query.all()
    for ad in all_ads_from_db:
        ad.is_expired = True
        db.session.add(ad)
        db.session.commit()


def load_new_data(new_json):
    actual_ads = []
    for ad in new_json:
        new_post_in_db = Ad.query.filter_by(id=ad['id']).first()
        if new_post_in_db is None:
            new_post_in_db = add_ad_in_db(ad)
        actual_ads.append(new_post_in_db)
    reset_actual()
    for ad in Ad.query.all():
        if ad in actual_ads:
            ad.is_expired = False
            db.session.add(ad)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        new_data = get_new_loads()
        load_new_data(new_data)