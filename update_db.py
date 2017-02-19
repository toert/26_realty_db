from requests import get
from model import add_ad_in_db
from server import db, Ad, app


URL_ACTUAL_ADS = 'https://devman.org/assets/ads.json'


def get_new_loads():
    return get(URL_ACTUAL_ADS).json()


def load_new_data(new_json):
    actual_ads_ids = []
    for ad in new_json:
        post_in_db = Ad.query.filter_by(id=ad['id']).first()
        if post_in_db is None:
            post_in_db = add_ad_in_db(ad, False)
        actual_ads_ids.append(post_in_db.id)

    all_ids = [ad.id for ad in db.session.query(Ad.id).all()]
    ids_of_expired_ads = [id for id in all_ids if id not in actual_ads_ids]
    update_ads_content(new_json)
    update_expiration(actual_ads_ids, is_expired=False)
    update_expiration(ids_of_expired_ads, is_expired=True)
    db.session.commit()


def update_ads_content(ad_json):
    db.session.bulk_update_mappings(Ad, ad_json)


def update_expiration(list_ids, is_expired):
    objects = (
        dict(
            id=ad,
            is_expired=is_expired
        )
        for ad in list_ids
    )
    db.session.bulk_update_mappings(Ad, objects)


if __name__ == '__main__':

    with app.app_context():
        db.create_all()
        new_data = get_new_loads()
        load_new_data(new_data)