import os.path
import unittest
from unittest import TestCase

from mockito import when, mock

from DataRepository import DataRepository
from ScrappingService import ScrappingService
from scrapper import Scrapper


class ScrappingServiceTest(TestCase):

    def setUp(self):
        if os.path.exists("la_liga_standing_data.txt"):
            os.remove("la_liga_standing_data.txt")

    def tearDown(self):
        if os.path.exists("la_liga_standing_data.txt"):
            os.remove("la_liga_standing_data.txt")

    def test_saves_scrapped_data_to_file(self):
        scrapper = mock(Scrapper)
        data_repository = DataRepository()
        when(scrapper).scrap('https://www.laliga.com/en-GB/laliga-easports/standing').thenReturn(
            'dummy scrapped data')
        scrapping_service = ScrappingService(scrapper, data_repository)

        scrapping_service.scrap('https://www.laliga.com/en-GB/laliga-easports/standing', 'la_liga_standing_data.txt')
        self.assertTrue(os.path.isfile('la_liga_standing_data.txt'))

        result = data_repository.read('la_liga_standing_data.txt')

        self.assertEqual(result, 'dummy scrapped data')


if __name__ == '__main__':
    unittest.main()
