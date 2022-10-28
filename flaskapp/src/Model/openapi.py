import csv
from time import sleep

import requests
from bs4 import BeautifulSoup
import config
import datetime
import pandas as pd




def find_item(item, str):
    try:
        return item.find(str).get_text()
    except:
        return None

# 1.. 상품 목록

def parse_good(item):
    return {
        "goodId": find_item(item, "goodId"),
        "goodName": find_item(item, "goodName"),
        "goodUnitDivCode": find_item(item, "goodUnitDivCode"),
        "goodBaseCnt": find_item(item, "goodBaseCnt"),
        "goodSmlclsCode": find_item(item, "goodSmlclsCode"),
        "detailMean": find_item(item, "detailMean"),
        "goodTotalCnt": find_item(item, "goodTotalCnt"),
        "goodTotalDivCode": find_item(item, "goodTotalDivCode")
    }

    # "상품 아이디 : goodId
    # "상품 이름": goodName
    # "상품 단위 구분 코드 : goodUnitDivCode
    # "상품 단위 량": goodBaseCnt
    # "상품 소분류 코드": goodSmlclsCode"
    # "상품 설명 상세": detailMean"
    # "상품 용량": goodTotalCnt"
    # "상품 용량 구분 코드": goodTotalDivCode


def load_good():
    url = 'http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getProductInfoSvc.do'
    params = {'serviceKey': config.openapi_key}

    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'lxml-xml')
    items = soup.find_all("item")

    if not items:
        print(response.text)

    row = []
    for item in items:
        row.append(parse_good(item))
    return row

# 2. 업체 목록

def parse_entp(item):
    return {
        "entpId": find_item(item, "entpId"),
        "entpName": find_item(item, "entpName"),
        "entpTypeCode": find_item(item, "entpTypeCode"),
        "entpAreaCode": find_item(item, "entpAreaCode"),
        "areaDetailCode": find_item(item, "areaDetailCode"),
        "entpTelno": find_item(item, "entpTelno"),
        "postNo": find_item(item, "postNo"),
        "plmkAddrBasic": find_item(item, "plmkAddrBasic"),
        "plmkAddrDetail": find_item(item, "plmkAddrDetail"),
        "roadAddrBasic": find_item(item, "roadAddrBasic"),
        "roadAddrDetail": find_item(item, "roadAddrDetail")
    }


#         "업체_아이디": entpId
#         "업체_명": entpName
#         "업체_업태_코드": entpTypeCode
#         "업체_지역_코드": entpAreaCode
#         "지역_상세_코드": areaDetailCode
#         "전화번호": entpTelno
#         "우편번호": postNo
#         "지번_기본_주소_명": plmkAddrBasic
#         "지번_상세_주소": plmkAddrDetail
#         "도로_기본_주소_명": roadAddrBasic
#         "도로_상세_주소_명": roadAddrDetail

def entp_load():
    url = 'http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getStoreInfoSvc.do'
    params = {'serviceKey': config.openapi_key}

    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'lxml-xml')
    items = soup.find_all("iros.openapi.service.vo.entpInfoVO")

    if not items:
        print(response.text)

    row = []
    for item in items:
        row.append(parse_entp(item))
    return row

# 3. 가격 정보 목록
def parse_goodPrice(item):
    return {
        "goodInspectDay": find_item(item, "goodInspectDay"),
        "entpId": find_item(item, "entpId"),
        "goodId": find_item(item, "goodId"),
        "goodPrice": find_item(item, "goodPrice"),
        "plusoneYn": find_item(item, "plusoneYn"),
        "goodDcYn": find_item(item, "goodDcYn"),
        "inputDttm": find_item(item, "inputDttm"),
        "goodDcStartDay": find_item(item, "goodDcStartDay"),
        "goodDcEndDay": find_item(item, "goodDcEndDay"),

    }

#         "상품_조사_일": goodInspectDay
#         "업체_아이디": entpId
#         "상품_아이디": goodId
#         "상품_가격": goodPrice
#         "원플러스원_여부": plusoneYn
#         "상품_할인_여부": goodDcYn
#         "입력_일시": inputDttm
#         "상품_할인_시작일": goodDcStartDay
#         "상품_할인_종료일": goodDcEndDay

# 이전 날짜 불러오기
def date_list(date):
    date_li = [date]
    for i in range(2):
        date = (datetime.datetime.strptime(date, '%Y%m%d').date()- datetime.timedelta(days = 14)).strftime('%Y%m%d')
        date_li.append(date)
    return date_li

def price_by_date_Id(date, goodId):
    row = []
    # for d in date_list(date):
    url = 'http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getProductPriceInfoSvc.do'
    params = {'goodInspectDay': date,
              'serviceKey': config.openapi_key,
              'goodId': goodId}

    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'lxml-xml')
    items = soup.find_all("iros.openapi.service.vo.goodPriceVO")

    for item in items:
        row.append(parse_goodPrice(item))

    return row

def load_price():
    from flaskapp.src.Model.control_db import find_all_good_by_id
    date = "20220923" # 20220909 20220923 20221007
    row = []
    goodId = find_all_good_by_id()
    for id in goodId:
        row.append(price_by_date_Id(date, id))
        sleep(0.1) # 트래픽 제한 걸림
        print(id)
    print(row)
    return row

def trans_csv():
    row = load_price()
    keys = row[0].keys()

    with open('test.csv','w',newline='') as output_file:
        dict_writer = csv.DictWriter(output_file,keys)
        dict_writer.writeheader()
        dict_writer.writerows(row)


# 중복 제거
def erase_dup(row):
    for i in row:
        try:
            df = pd.DataFrame(i)
            df_drop = df.drop_duplicates(['entpId'], keep='first')
            li_drop = df_drop.T.to_dict().values()

        except TypeError:
            pass

    return li_drop

