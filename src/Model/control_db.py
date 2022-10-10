from pymongo import MongoClient

from config import db_client
from src.Model import openapi

client = MongoClient(db_client)
db = client.zzangbaguni


# collection_good = db.goodlist
# collect_entp = db.entplist
# collect_price = db.price

def find_all_good_by_id():
    collection_good = db.goodlist
    all_row = collection_good.find()
    goodId = []
    for row in all_row:
        goodId.append(row["goodId"])
    return goodId


# data type(collection) 에 따라 control 가능하도록 구현
def insert_row(coll, add_row):
    collect_price = db.price
    collect_price.insert_many(add_row)


# update 업체의 위도 경도
def update_entp_pos(id,lat,long):
    collect_entp = db.entplist
    collect_entp.update_one({"entpId":id}, {"$set":{"latitude": lat, "longitude": long}}, upsert=True)

# 모든 업체 불러오기
def find_all_entp():
    collect_entp = db.entplist
    all_entp = collect_entp.find()
    return all_entp

