import time
from unittest import TestCase

from src.Service import address
from src.Service.address import update_entp_position, find_near_entp


class Test(TestCase):
    def test(self):
        start = time.time()
        update_entp_position()
        end = time.time()
        print(f"{end - start:.5f} sec")

    def test1(self):
        start = time.time()
        print(find_near_entp((37.29640641606932,126.9776123527779)))
        end = time.time()
        print(f"{end - start:.5f} sec")
