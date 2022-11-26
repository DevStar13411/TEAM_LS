from flask import Blueprint, request, render_template

from src.Model.control_db import find_price_by_id, find_all_good_by_id, find_good_by_entp, find_all_price, find_good, \
    find_entp, find_good_by_entp_with_category, new_find_good, new_find_entp, find_price
from src.Service.address import get_location, find_near_entp

main_page = Blueprint("main", __name__, url_prefix='/')


# 메인 화면
@main_page.route('/')
def hello_world():
    return render_template('index.html')


# 주소 -> 좌표 변환
@main_page.route('/coordinates', methods=['GET'])
def get_coord():
    address = request.args.get('address', default="", type=str)
    latitude, longitude = get_location(address)
    result = {"latitude": latitude, "longitude": longitude}
    return result


# 상품 목록
@main_page.route('/goods', methods=['GET'])
def get_goods():
    latitude = request.args.get('latitude', default=37.29640641606932, type=float)
    longitude = request.args.get('longitude', default=126.9776123527779, type=float)

    entp_list = find_near_entp((latitude, longitude))
    data = find_good_by_entp(entp_list)

    result = {"latitude": latitude, "longitude": longitude, "goods": data}
    return result


# 상품 목록
@main_page.route('/goods/<int:category>', methods=['GET'])
def get_goods_category(category):
    latitude = request.args.get('latitude', default=37.29640641606932, type=float)
    longitude = request.args.get('longitude', default=126.9776123527779, type=float)

    entp_list = find_near_entp((latitude, longitude))
    data = find_good_by_entp_with_category(entp_list, category)

    result = {"latitude": latitude, "longitude": longitude, "goods": data}
    return result


# 가격 정보 호출(개선 후)
@main_page.route('/prices', methods=['POST'])
def get_prices():
    # 상품 목록과 현재 위치를 담은 json 파일 받을 예정 -> gid, eid를 통해 가격 결과 출력

    data = request.get_json()
    good_id_list = data.get("goods")
    latitude = data.get("latitude")
    longitude = data.get("longitude")

    entp_list = find_near_entp((latitude, longitude))
    good = find_good(good_id_list)
    price, eid = find_all_price(good_id_list, entp_list)
    entp = find_entp(eid)

    p = {"price": price, "entp": entp, "good": good}
    print(p)

    return p


# 메인페이지에서 가격 확인을 위함
@main_page.route('/price/<int:gid>', methods=['GET'])
def get_price(gid):

    latitude = request.args.get('latitude', default=37.29640641606932, type=float)
    longitude = request.args.get('longitude', default=126.9776123527779, type=float)

    entp_list = find_near_entp((latitude, longitude))
    price = find_price(gid, entp_list)

    print(price)
    return price
