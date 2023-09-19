import os
import unittest
from unittest import TestCase

from mockito import when

from ScrappingService import ScrappingService
from scrapper import Scrapper


class ChatGPTServiceTest(TestCase):

    def test_creates_a_file_with_chatgpt_response(self):
        scrapper = Scrapper()
        when(scrapper).scrap('https://www.laliga.com/en-GB/laliga-easports/standing').thenReturn(
            'dummy scrapped data')
        scrapping_service = ScrappingService(scrapper)

        scrapping_service.scrap('https://www.laliga.com/en-GB/laliga-easports/standing', 'la_liga_standing_data.txt')
        self.assertTrue(os.path.isfile('la_liga_standing_data.txt'))

        file = open('la_liga_standing_data.txt', 'r')
        result = file.read()
        print('RESULT')
        print(result)
        file.close()

        self.assertEqual(result, 'dummy scrapped data')


if __name__ == '__main__':
    unittest.main()
