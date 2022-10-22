import time

from pymongo import MongoClient
from config import db_client


client = MongoClient(db_client)
db = client.zzangbaguni


# collection_good = db.goodlist
# collect_entp = db.entplist
# collect_price = db.price

# 모든 상품 코드 불러오기
def find_all_good_by_id():
    collection_good = db.goodlist
    all_row = collection_good.find()
    goodId = []
    for row in all_row:
        goodId.append(row["goodId"])
    return goodId


# data type(collection) 에 따라 control 가능하도록 구현
# 날짜 최신으로 갱신하는 형태로 작성해야함
def insert_row(coll, add_row):
    collect_price = db.price
    collect_price.insert_many(add_row)


# update 업체의 위도 경도
def update_entp_pos(id, lat, long):
    collect_entp = db.entplist
    collect_entp.update_one({"entpId": id}, {"$set": {"latitude": lat, "longitude": long}}, upsert=True)


# 모든 업체 불러오기
def find_all_entp():
    collect_entp = db.entplist
    all_entp = collect_entp.find()
    return all_entp


# 상품 이름, 카테고리로 정리(상품 코드 AAAAAXXX : 앞 다섯자리)
# 30101 30102 30103 30201 30202 30203 30204 30205 30206 30301 30302 30304 30305
# 후에 카테고리 명칭 정해지면 분류해서 출력
def find_all_good_category():
    collection_good = db.goodlist
    all_row = collection_good.find()
    info = []
    for row in all_row:
        category_number = row['goodSmlclsCode'] // 1000
        info.append({"name": row["goodName"], "category": category_number})

    return info


# 각 업체 별 상품 개수 체크
def find_entp(entp_id_list):

    collect_entp = db.entplist
    collect_price = db.price

    for entp in entp_id_list:

        entp_name = collect_entp.find_one({"entpId": entp})["entpName"]
        row = collect_price.find({"entpId": entp})
        row = list(row)
        print(entp_name, len(row),347)


# 상품 id, 주변 업체 id list -> 상품 명, 업체 명, 가격 정보 출력
#
def find_price_by_id(good_id_list, entp_id_list):
    start = time.time()
    collection_good = db.goodlist
    collect_entp = db.entplist
    collect_price = db.price
    info =[]
    data_entp = []
    price_row = list(collect_price.find({"entpId":{"$in":entp_id_list},"goodId":{"$in":good_id_list}},{"entpId":1,"goodId":1,"goodPrice":1,"_id":0}))

    entp_name = list(collect_entp.find({"entpId": {"$in" :entp_id_list}},{"entpName":1,"latitude":1,"longitude":1,"_id":0}))
    good_name = list(collection_good.find({"goodId": {"$in" :good_id_list}},{"goodName":1,"_id":0}))
    print(good_name)


    price_row
    # for row in price_row:
    #     good_name = collection_good.find_one({"goodId": row['goodId']})["goodName"]
    #     entp_name = collect_entp.find_one({"entpId": row['entpId']})["entpName"]
    #     try:
    #         info.append({"good_name":good_name,"entp_name":entp_name,"price": row["goodPrice"]})
    #
    #     except TypeError:
    #
    #         # print("해당 업체("+entp_name+")는 상품("+good_name+")이 존재하지 않습니다.", )
    #         pass
    end = time.time()
    print(f"{end - start:.5f} sec")



    return price_row
