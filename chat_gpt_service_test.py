import os
import unittest
from unittest import TestCase

import responses
from mockito import when
from requests import Response

from console import Console
from data_repository import DataRepository
from chat_gpt_chat_client import ChatGPTChatClient
from chat_gpt_service import ChatgptService

JSON_RESPONSE = {'id': 'chatcmpl-80rL3miP00BIbi4JVueVU16BYyQkv', 'object': 'chat.completion',
                 'created': 1695215725,
                 'model': 'gpt-3.5-turbo-0613', 'choices': [{'index': 0, 'message': {'role': 'assistant',
                                                                                     'content': 'Red'},
                                                             'finish_reason': 'stop'}],
                 'usage': {'prompt_tokens': 2561, 'completion_tokens': 16, 'total_tokens': 2577}}

OUTPUT_FILENAME = 'dummy_output_filename.txt'


class ChatGPTServiceTest(TestCase):

    def setUp(self):
        if os.path.exists('%s' % OUTPUT_FILENAME):
            os.remove(OUTPUT_FILENAME)

    def tearDown(self):
        if os.path.exists('%s' % OUTPUT_FILENAME):
            os.remove(OUTPUT_FILENAME)

    def test_returns_file_not_found_when_data_file_does_not_exist(self):
        console = Console()
        chat_gpt_chat_client = ChatGPTChatClient()
        data_repository = DataRepository()
        when(data_repository).read(...).thenRaise(FileNotFoundError)
        chat_gpt_service = ChatgptService(chat_gpt_chat_client, data_repository, OUTPUT_FILENAME, console)

        result = chat_gpt_service.update_context_window_with('filename_does_not_exist.txt')

        self.assertEqual(result, 'file-not-found')

    def test_returns_error_when_can_not_update_chat_gpt(self):
        console = Console()
        chat_gpt_chat_client = ChatGPTChatClient()
        data_repository = DataRepository()
        fake_response = self.build_error_response()
        when(data_repository).read('dummy_data.txt').thenReturn('Some dummy data')
        when(chat_gpt_chat_client).send(...).thenReturn(fake_response)
        chat_gpt_service = ChatgptService(chat_gpt_chat_client, data_repository, OUTPUT_FILENAME, console)

        result = chat_gpt_service.update_context_window_with('dummy_data.txt')

        self.assertEqual('error-updating-context-window', result)

    def test_returns_context_window_updated_when_can_update_chat_gpt_with_new_data(self):
        console = Console()
        chat_gpt_chat_client = ChatGPTChatClient()
        data_repository = DataRepository()
        fake_ok_response = self.build_ok_response()
        when(data_repository).read('dummy_data.txt').thenReturn('Some dummy data')
        when(chat_gpt_chat_client).send(...).thenReturn(fake_ok_response)
        chat_gpt_service = ChatgptService(chat_gpt_chat_client, data_repository, OUTPUT_FILENAME, console)

        result = chat_gpt_service.update_context_window_with('dummy_data.txt')

        self.assertEqual('context-window-updated', result)

    # I couldn't create a fake Response object, so I had to intercept the call with an external library T_T
    @responses.activate
    def test_stores_a_response_in_a_file_when_asking_a_question(self):
        responses.add(
            responses.POST,
            'https://api.openai.com/v1/chat/completions',
            json=JSON_RESPONSE,
            status=200,
        )
        console = Console()
        chat_gpt_chat_client = ChatGPTChatClient()
        data_repository = DataRepository()
        chat_gpt_service = ChatgptService(chat_gpt_chat_client, data_repository, OUTPUT_FILENAME, console)

        chat_gpt_service.ask('What is your favourite color, my friend?')

        data = data_repository.read(OUTPUT_FILENAME)
        self.assertEqual('Red', data)
        self.assertTrue(os.path.isfile(OUTPUT_FILENAME))

    @staticmethod
    def build_error_response():
        fake_response = Response()
        fake_response.status_code = 400
        return fake_response

    @staticmethod
    def build_ok_response():
        fake_response = Response()
        fake_response.status_code = 200
        return fake_response


if __name__ == '__main__':
    unittest.main()
