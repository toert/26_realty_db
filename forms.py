from flask import request
from model import Ad, REGION_LIST


def get_forms_content():
    region = request.args.get('oblast_district')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    page = request.args.get('page')
    return validate_form_data(region, min_price, max_price, page)


def validate_form_data(region, min_price, max_price, page):
    if not region or region is None:
        region = REGION_LIST[0]['districts'][0][0]
    if not min_price or min_price is None:
        min_price = 0
    if not max_price or max_price is None:
        max_price = Ad.query.order_by(Ad.price.desc()).first().price
    if not page or page is None:
        page = 1
    return region, min_price, max_price, page
