import time
from unittest import TestCase


from src.Model.control_db import find_all_good_by_id, find_price_by_id, \
    update_price, find_all_price, find_good, find_entp, find_all_good

from src.Service.address import find_near_entp
from src.Service.image import list_chuck, search_images
import time
from multiprocessing import Pool

class Test(TestCase):
    def test_main(self):

        self.test_price(1)
        self.test_price(2)

    def test_price(self, num):

        start = time.time()
        # 테스트 환경 : 모든 상품목록, 학교 주변 매장
        if num == 1:
            self.test_price1()
        elif num == 2:
            self.test_price2()

        end = time.time()
        print("test", num, f"{end - start:.5f} sec")

    def test_price1(self):

        good_id_list = find_all_good_by_id()
        entp_id_list = find_near_entp((37.265903839248956, 126.9999098091105), 5)

        price_row, entp_name, good_name = find_price_by_id(good_id_list, entp_id_list)

    def test_price2(self):

        good_id_list = find_all_good_by_id()
        entp_id_list = find_near_entp((37.265903839248956, 126.9999098091105), 5)

        good = find_good(good_id_list)
        entp = find_entp(entp_id_list)
        price = find_all_price(good_id_list, entp_id_list)

    def test_update(self):
        # trans_jsonfile("20220909")
        # update_price("20220923")
        # update_price("20221007")
        # update_price("20221021")
        update_price("20221104")

    def test_image(self):

        start = time.time()
        p_num = 4

        goods = find_all_good()
        goods_split = list_chuck(goods, p_num)

        with Pool(processes=p_num) as pool:
            pool.map(search_images, goods_split)
            pool.close()
            pool.join()
        print('Download time : ' + str(time.time() - start)[:5] + ' 초')
