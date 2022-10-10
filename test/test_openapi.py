from unittest import TestCase

from src.Service import address


class Test(TestCase):
    def test_load_good(self):
        print(address.get_distacne((37.451, 126.986), (43.65, -79.38)))
