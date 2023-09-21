import os
import unittest
from unittest import TestCase

import responses
from mockito import mock, when, inorder, spy
from requests import Response

from chat_gpt_chat_client import ChatGPTChatClient
from chat_gpt_service import ChatgptService
from console import Console
from data_repository import DataRepository
from scrapper import Scrapper
from scrapping_service import ScrappingService

# Real responses from ChatGPT
FIRST_QUESTION_JSON_RESPONSE = {'id': 'chatcmpl-80rL3miP00BIbi4JVueVU16BYyQkv', 'object': 'chat.completion',
                                'created': 1695215725,
                                'model': 'gpt-3.5-turbo-0613', 'choices': [{'index': 0, 'message': {'role': 'assistant',
                                                                                                    'content': 'The current leader of La Liga EA Sports is Real Madrid with 15 points.\n'},
                                                                            'finish_reason': 'stop'}],
                                'usage': {'prompt_tokens': 2561, 'completion_tokens': 16, 'total_tokens': 2577}}
SECOND_QUESTION_JSON_RESPONSE = {'id': 'chatcmpl-80rKPsGh7KwiozvhrAzMPnLxv8Rnf', 'object': 'chat.completion',
                                 'created': 1695215685, 'model': 'gpt-3.5-turbo-0613', 'choices': [{'index': 0,
                                                                                                    'message': {
                                                                                                        'role': 'assistant',
                                                                                                        'content': 'The teams that have more than 6 points in the LALIGA EA SPORTS standings are:\n\n1. Real Madrid - 15 points\n2. FC Barcelona - 13 points\n3. Girona FC - 13 points\n4. Athletic Club - 10 points\n5. Valencia CF - 9 points\n6. Rayo Vallecano - 9 points\n'},
                                                                                                    'finish_reason': 'stop'}],
                                 'usage': {'prompt_tokens': 2559, 'completion_tokens': 78, 'total_tokens': 2637}}


class LaLigaFeature(TestCase):

    def setUp(self):
        if os.path.exists("la_liga_standing_data.txt"):
            os.remove("la_liga_standing_data.txt")
        if os.path.exists("chat_gpt_answers.txt"):
            os.remove("chat_gpt_answers.txt")

    def tearDown(self):
        if os.path.exists("la_liga_standing_data.txt"):
            os.remove("la_liga_standing_data.txt")
        if os.path.exists("chat_gpt_answers.txt"):
            os.remove("chat_gpt_answers.txt")

    @responses.activate
    def test_chatGPT_answers_two_questions_about_LaLiga(self):
        # Scrapping LaLiga Standing web page
        scrapper = mock(Scrapper)
        chat_gpt_chat_client = ChatGPTChatClient()
        data_repository = DataRepository()
        when(scrapper).scrap('https://www.laliga.com/en-GB/laliga-easports/standing').thenReturn(
            'dummy scrapped data with all data from standing')
        scrapping_service = ScrappingService(scrapper, data_repository)

        scrapping_service.scrap('https://www.laliga.com/en-GB/laliga-easports/standing', 'la_liga_standing_data.txt')

        self.assertTrue(os.path.isfile('./la_liga_standing_data.txt'))

        # Asking questions to ChatGPT
        console = Console()
        mocked_console = spy(console)
        chatgpt_service = ChatgptService(chat_gpt_chat_client, data_repository, 'chat_gpt_answers.txt', mocked_console,
                                         'la_liga_standing_data.txt')

        # Intercept first question
        responses.add(
            responses.POST,
            'https://api.openai.com/v1/chat/completions',
            json=FIRST_QUESTION_JSON_RESPONSE,
            status=200,
        )
        chatgpt_service.ask('Who is the current leader of La Liga EA Sports?')

        inorder.verify(
            mocked_console).println(
            'The current leader of La Liga EA Sports is Real Madrid with 15 points.')

        # Intercept second question
        responses.add(
            responses.POST,
            'https://api.openai.com/v1/chat/completions',
            json=SECOND_QUESTION_JSON_RESPONSE,
            status=200,
        )

        chatgpt_service.ask('Which teams have more than 6 points?')

        inorder.verify(mocked_console).println(
            'The teams that have more than 6 points in the LALIGA EA SPORTS standings are:')
        inorder.verify(mocked_console).println('')
        inorder.verify(mocked_console).println('1. Real Madrid - 15 points')
        inorder.verify(mocked_console).println('2. FC Barcelona - 13 points')
        inorder.verify(mocked_console).println('3. Girona FC - 13 points')
        inorder.verify(mocked_console).println('4. Athletic Club - 10 points')
        inorder.verify(mocked_console).println('5. Valencia CF - 9 points')
        inorder.verify(mocked_console).println('6. Rayo Vallecano - 9 points')

        self.assertTrue(os.path.isfile('./chat_gpt_answers.txt'))

    @staticmethod
    def build_ok_response():
        fake_response = Response()
        fake_response.status_code = 200
        return fake_response


if __name__ == '__main__':
    unittest.main()
