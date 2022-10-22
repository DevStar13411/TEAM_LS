import pymongo as pymongo
from flask import Blueprint, request, render_template
from src.Model.control_db import find_all_good_category

main_page = Blueprint("main", __name__, url_prefix='/')

# 메인 화면
@main_page.route('/')
def hello_world():
    return render_template('index.html')

# 상품 목록
@main_page.route('/goods', methods = ['GET'])
def get_goods_page():

    # 상품 정보를 담은 json 전달
    data = {"name" : "새우깡"}

    return find_all_good_category()

# 결과 지도 화면
@main_page.route('/result', methods = ['POST'])
def get_result_page():
    # 상품 목록과 현재 위치를 담은 json 파일 받을 예정
    if request.is_json:
        data = request.get_json()
    else:
        return None

    return data
