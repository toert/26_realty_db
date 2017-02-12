from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from model import db, Ad, REGION_LIST
from forms import get_forms_content

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

ADS_IN_ONE_PAGE = 15


@app.route('/', methods=['GET'])
def ads_list():
    region_param, min_price_param, max_price_param, page = get_forms_content()
    suitable_ads = Ad.query.filter(Ad.oblast_district == region_param,
                                   Ad.price > min_price_param,
                                   Ad.price < max_price_param,
                                   Ad.actual
                                   ).paginate(int(page), ADS_IN_ONE_PAGE, False)
    parameters = {'region_param': region_param,
                  'min_price_param': min_price_param,
                  'max_price_param': max_price_param}

    return render_template('ads_list.html',
                           ads=suitable_ads,
                           params=parameters,
                           region_list=REGION_LIST,
                           max_price=Ad.query.order_by(Ad.price.desc()).first().price)


if __name__ == "__main__":
    app.run()
