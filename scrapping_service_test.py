import os.path
import unittest
from unittest import TestCase

from mockito import when

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
        scrapper = Scrapper()
        when(scrapper).scrap('https://www.laliga.com/en-GB/laliga-easports/standing').thenReturn(
            'Based on the provided information from the current standings of La Liga EA Sports, '
            'the current'
            ' leader is Real Madrid with 15 points.')
        scrapping_service = ScrappingService(scrapper)

        scrapping_service.scrap('https://www.laliga.com/en-GB/laliga-easports/standing', 'la_liga_standing_data.txt')
        self.assertTrue(os.path.isfile('la_liga_standing_data.txt'))

        file = open('la_liga_standing_data.txt', 'r')
        result = file.read()
        print('RESULT')
        print(result)
        file.close()

        self.assertEqual(result,
                         'Based on the provided information from the current standings of La Liga EA Sports, '
                         'the current'
                         ' leader is Real Madrid with 15 points.')


if __name__ == '__main__':
    unittest.main()
