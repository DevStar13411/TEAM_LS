from unittest import TestCase

from src.Model.control_db import find_all_good_by_id
from src.Model.openapi import load_good


class Test(TestCase):
    def test_load_good(self):
        self.assertEqual(1+1,2)

