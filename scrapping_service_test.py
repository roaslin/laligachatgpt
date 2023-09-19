import os.path
import unittest
from unittest import TestCase

from ScrappingService import ScrappingService


class ScrappingServiceTest(TestCase):

    def setUp(self):
        if os.path.exists("la_liga_standing_data.txt"):
            os.remove("la_liga_standing_data.txt")

    def tearDown(self):
        if os.path.exists("la_liga_standing_data.txt"):
            os.remove("la_liga_standing_data.txt")

    def test_creates_a_file_to_store_scrapped_data(self):
        scrapping_service = ScrappingService()

        scrapping_service.scrap('https://www.laliga.com/en-GB/laliga-easports/standing', 'la_liga_standing_data.txt')

        self.assertTrue(os.path.isfile('la_liga_standing_data.txt'))


if __name__ == '__main__':
    unittest.main()
