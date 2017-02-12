from flask import request
from model import Ad, REGION_LIST


def get_forms_content():
    region_param = request.args.get('oblast_district')
    min_price_param = request.args.get('min_price_param')
    max_price_param = request.args.get('max_price_param')
    page = request.args.get('page')
    return validate_form_data(region_param, min_price_param, max_price_param, page)


def validate_form_data(region_param, min_price_param, max_price_param, page):
    region_param = region_param or REGION_LIST[0]['districts'][0][0]
    min_price_param = min_price_param or 0
    max_price_param = max_price_param or Ad.query.order_by(Ad.price.desc()).first().price
    page = page or 1
    return region_param, min_price_param, max_price_param, page
