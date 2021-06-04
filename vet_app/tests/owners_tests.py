import unittest
from models.owner import Owner

class OwnerTest(unittest.TestCase):

    def setUp(self):
        self.owner1 = Owner("Sara", "Humphries", "01234", "21, Millar Crescent")

    def test_owner_first_name(self):
        self.assertEqual("Sara", self.owner1.first_name)

    def test_owner_last_name(self):
        self.assertEqual("Humphries", self.owner1.last_name)
