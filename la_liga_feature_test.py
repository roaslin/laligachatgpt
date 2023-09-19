import os
import unittest
from unittest import TestCase

from mockito import inorder, mock, when

import Console
from ChatgptService import ChatgptService
from ScrappingService import ScrappingService
from scrapper import Scrapper


# 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
class LaLigaFeature(TestCase):

    def setUp(self):
        if os.path.exists("la_liga_standing_data.txt"):
            os.remove("la_liga_standing_data.txt")

    def tearDown(self):
        if os.path.exists("la_liga_standing_data.txt"):
            os.remove("la_liga_standing_data.txt")

    def test_chatGPT_answers_two_questions_about_LaLiga(self):
        console = mock(Console)
        scrapper = mock(Scrapper)
        when(scrapper).scrap('https://www.laliga.com/en-GB/laliga-easports/standing').thenReturn(
            'dummy scrapped data with all data from standing')
        scrapping_service = ScrappingService(scrapper)

        scrapping_service.scrap('https://www.laliga.com/en-GB/laliga-easports/standing', 'la_liga_standing_data.txt')

        self.assertTrue(os.path.isfile('./la_liga_standing_data.txt'))

        chatgpt_service = ChatgptService()
        chatgpt_service.ask('Who is the current leader of La Liga EA Sports?')

        inorder.verify(
            console.printLn(
                'Based on the provided information from the current standings of La Liga EA Sports, the current '
                'leader is Real Madrid with 15 points.'))

        chatgpt_service.ask('Which teams have more than 6 points?')

        inorder.verify(console.printLn(
            'The teams that have more than 6 points in the current standings of La Liga EA Sports are:'))
        inorder.verify(console.printLn('Real Madrid: 15 points'))
        inorder.verify(console.printLn('FC Barcelona: 13 points'))
        inorder.verify(console.printLn('Girona FC: 13 points'))
        inorder.verify(console.printLn('Athletic Club: 10 points'))
        inorder.verify(console.printLn('Valencia CF: 9 points'))
        inorder.verify(console.printLn('Rayo Vallecano: 9 points'))
        inorder.verify(console.printLn('These teams have accumulated more than 6 points in the league.'))


if __name__ == '__main__':
    unittest.main()
