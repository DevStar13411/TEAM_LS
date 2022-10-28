import traceback

import pymongo as pymongo
from flask import Blueprint, request, render_template
from src.Model.control_db import find_all_good_category

from flaskapp.src.Model.control_db import find_all_good, find_price_by_id, find_all_good_by_id, find_good_by_entp
from flaskapp.src.Service.address import get_location, find_near_entp

main_page = Blueprint("main", __name__, url_prefix='/')

# 메인 화면
@main_page.route('/')
def hello_world():
    return render_template('index.html')


# 상품 목록
@main_page.route('/goods', methods=['GET'])
def get_goods_page():
    address = request.args.get('address', default="", type=str)

    # 주소 -> 위, 경도로 변환
    if address:
        latitude, longitude = get_location(address)

    else:
        latitude = request.args.get('latitude', default=37.29640641606932, type=float)
        longitude = request.args.get('longitude', default=126.9776123527779, type=float)

    entp_list = find_near_entp((latitude, longitude))
    data = find_good_by_entp(entp_list)

    result = {"latitude": latitude, "longitude": longitude, "goods": data}
    return result
    # return render_template('goods.html',goods_data = data)


    # return find_all_good_category()


# 결과 지도 화면

@main_page.route('/prices', methods=['GET', 'POST'])
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
