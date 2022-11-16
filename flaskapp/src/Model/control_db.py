from pymongo import MongoClient
from config import db_client
from src.Model.openapi import load_price

client = MongoClient(db_client)
db = client.zzangbaguni


# 모든 상품 불러오기
def find_all_good():
    collection_good = db.goodlist
    return list(collection_good.find({}, {"goodId": 1, "goodName": 1, "goodSmlclsCode": 1, "_id": 0}))


# 모든 상품 ID 불러오기
def find_all_good_by_id():
    collection_good = db.goodlist
    all_row = collection_good.find()
    goodId = []
    for row in all_row:
        goodId.append(row["goodId"])
    return goodId


# update 업체의 위도 경도
def update_entp_pos(id, lat, long):
    collect_entp = db.entplist
    collect_entp.update_one({"entpId": id}, {"$set": {"latitude": lat, "longitude": long}}, upsert=True)


# update 가격 정보 2주 단위로 실행할 수 있도록 작성
def update_price(date):
    data = load_price(date)
    collect_price = db.price
    cnt = 0

    for row in data:
        collect_price.replace_one({"goodId": row['goodId'], "entpId": row['entpId']}, row, upsert=True)

        cnt += 1
        if cnt//50 == 0:
            print(cnt)


# 모든 업체 불러오기
def find_all_entp():
    collect_entp = db.entplist
    all_entp = collect_entp.find()
    return all_entp


# 상품 이름, 카테고리로 정리(상품 코드 AAAAAXXX : 앞 다섯자리)
# 30101 30102 30103 30201 30202 30203 30204 30205 30206 30301 30302 30304 30305
def find_all_good_category():
    collection_good = db.goodlist
    all_row = collection_good.find()
    info = []
    for row in all_row:
        category_number = row['goodSmlclsCode'] // 1000
        info.append({"name": row["goodName"], "category": category_number})
    return info


# id_list 안에 있는 매장 정보 출력
def find_entp(entp_id_list):
    collect_entp = db.entplist
    result = list(collect_entp.find({"entpId": {"$in": entp_id_list}},
                                    {"entpId": 1, "entpName": 1, "latitude": 1, "longitude": 1, "_id": 0}))
    return result


# id_list 안에 있는 상품 정보 출력
def find_good(good_id_list):
    collection_good = db.goodlist
    result = list(collection_good.find({"goodId": {"$in": good_id_list}}, {"goodId": 1, "goodName": 1, "_id": 0}))

    return result


# 상품 id, 주변 업체 id list -> 상품 명, 업체 명, 가격 정보 출력(개선 전)
def find_price_by_id(good_id_list, entp_id_list):
    collection_good = db.goodlist
    collect_entp = db.entplist
    collect_price = db.price
    info = []
    data_entp = []

    price_row = list(collect_price.find({"entpId": {"$in": entp_id_list}, "goodId": {"$in": good_id_list}}, \
                                        {"entpId": 1, "goodId": 1, "goodPrice": 1, "_id": 0}))
    entp_name = list(collect_entp.find({"entpId": {"$in": entp_id_list}},
                                       {"entpId": 1, "entpName": 1, "latitude": 1, "longitude": 1, "_id": 0}))
    good_name = list(collection_good.find({"goodId": {"$in": good_id_list}}, {"goodId": 1, "goodName": 1, "_id": 0}))

    return price_row, entp_name, good_name


def find_good_by_entp_with_category(entp_id_list, category):
    good_list = find_good_by_entp(entp_id_list)
    result = []
    for row in good_list:
        if row['goodSmlclsCode'] // 1000 == category:
            result.append(row)

    return result


# 업체가 보유하고 있는 상품 리스트
def find_good_by_entp(entp_id_list):
    collection_good = db.goodlist
    collect_price = db.price

    good_id_json = list(collect_price.find({"entpId": {"$in": entp_id_list}}, {"goodId": 1, "_id": 0}))

    good_id_list = set([])
    # goodId 중복 제거
    for gid in good_id_json:
        good_id_list.add(gid['goodId'])
    good_id_list = list(good_id_list)
    result = list(collection_good.find({"goodId": {"$in": good_id_list}},
                                       {"goodId": 1, "goodName": 1, "goodSmlclsCode": 1, "_id": 0}))

    return result


# 개선된 업체 정보
# ex) {123:"롯데마트"}
def new_find_entp(entp_id_list):
    collect_entp = db.entplist
    entp_name = list(collect_entp.find({"entpId": {"$in": entp_id_list}}, {"entpId": 1, "entpName": 1, "_id": 0}))
    result = {}
    for row in entp_name:
        result[row['entpId']] = row['entpName']

    return result


# 개선된 상품 정보
# ex) {991:"새우깡"}
def new_find_good(good_id_list):
    collection_good = db.goodlist
    good_name = list(collection_good.find({"goodId": {"$in": good_id_list}}, {"goodId": 1, "goodName": 1, "_id": 0}))
    result = {}
    for row in good_name:
        result[row['goodId']] = row['goodName']

    return result


# 상품 id, 주변 업체 id list -> 상품 명, 업체 명, 가격 정보 출력(개선 후)
def find_all_price(good_id_list, entp_id_list):
    collect_price = db.price

    result = {}
    good = new_find_good(good_id_list)
    entp = new_find_entp(entp_id_list)

    for eid in entp_id_list:
        price_row = list(collect_price.find({"entpId": eid, "goodId": {"$in": good_id_list}}, \
                                            {"goodId": 1, "goodPrice": 1, "_id": 0}))
        price_coll = {}
        for row in price_row:
            price_coll[good[row['goodId']]] = row['goodPrice']
        result[entp[eid]] = price_coll
    return result


def find_price(goodId, entp_id_list):
    collect_price = db.price

    entp = new_find_entp(entp_id_list)
    price = list(collect_price.find({"entpId": {"$in":entp_id_list}, "goodId": goodId}, \
                                            {"entpId": 1, "goodPrice": 1, "_id": 0}).sort("goodPrice"))

    return price