from flask import Blueprint, request, render_template

from src.Model.control_db import find_price_by_id, find_all_good_by_id, find_good_by_entp, find_price, find_good, \
    find_entp, find_good_by_entp_with_category
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
def get_price():
    # 상품 목록과 현재 위치를 담은 json 파일 받을 예정 -> gid, eid를 통해 가격 결과 출력

    data = request.get_json()
    good_id_list = data.get("goods")
    latitude = data.get("latitude")
    longitude = data.get("longitude")

    entp_list = find_near_entp((latitude, longitude))
    good = find_good(good_id_list)
    entp = find_entp(entp_list)
    price = find_price(good_id_list, entp_list)

    p = {"price": price, "entp": entp, "good": good}
    return p


# 가격 정보 호출(개선 전)
@main_page.route('/price', methods=['POST'])
def get_result_page():
    # 상품 목록과 현재 위치를 담은 json 파일 받을 예정 -> gid, eid를 통해 가격 결과 출력
    if request.method == 'POST':
        data = request.get_json()
        good_id_list = data.get("goods")
        latitude = data.get("latitude")
        longitude = data.get("longitude")

    # 테스트 용 임시
    else:
        if request.method == 'GET':
            latitude = request.args.get('latitude', default=37.29640641606932, type=float)
            longitude = request.args.get('longitude', default=126.9776123527779, type=float)

            good_id_list = find_all_good_by_id()

    entp_list = find_near_entp((latitude, longitude))
    price, entp, good = find_price_by_id(good_id_list, entp_list)

    p = {"price": price, "entp": entp, "good": good}
    return p
    # return render_template('map.html',price = data)
