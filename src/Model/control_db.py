from pymongo import MongoClient

from config import db_client

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

# 이미 있는 row -> update
def update_row():
    collect_price = db.price