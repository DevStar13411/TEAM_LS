import requests
from flask import json
from haversine import haversine

import config

from src.Model.control_db import find_all_entp, update_entp_pos


# entp collection의 row -> 지번주소 혹은 도로명 주소를 이용해 (위도, 경도) 추출
# 카카오 맵이 지번 주소 정보를 담고 있지 않는 경우가 종종 있어 도로명으로 2차 확인
# DB에 도로명주소가 없는 경우도 존재(지번 주소는 모두 가지고 있음)

# 지번 주소가 정확하지 않아 도로명 주소로 전환
# https://www.juso.go.kr/CommonPageLink.do?link=/support/AddressTransformThousand

# 도로명 주소 -> 위도,경도로 변환
def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address

    headers = {"Authorization": "KakaoAK " + config.kakao_key}
    api_json = json.loads(str(requests.get(url, headers=headers).text))
    print(api_json)
    docu = api_json['documents']
    try:
        crd = (float(docu[0]['address']['y']), float(docu[0]['address']['x']))
    except:
        print('도로명 주소를 찾을 수 없습니다.', address)
        return 0, 0

    return crd


# 위도 경도 DB에 update
def update_entp_position():
    entp_list = find_all_entp()
    for entp_row in entp_list:
        if entp_row['latitude']==0:
            address = entp_row['roadAddrBasic']
            x, y = get_location(address)
            update_entp_pos(entp_row['entpId'], x, y)


# a = (위도1,경도1) b = (위도2, 경도2) 위도 : float
def get_distacne(a, b):
    return haversine(a, b, unit="km")


# now_pos (위도,경도) rad(주변 반경) 업체 id 리스트 출력
# -> 추후 now_pos 도로명 주소로 변경 가능성 고민
def find_near_entp(now_pos, rad):
    entp_list = find_all_entp()
    entpId_near = []
    for entp_row in entp_list:
        address = entp_row['roadAddrBasic']
        x, y = get_location(address)

        dist = get_distacne(now_pos, (x, y))
        if dist <= rad:
            entpId_near.append(entp_row['entpId'])
    return entpId_near
