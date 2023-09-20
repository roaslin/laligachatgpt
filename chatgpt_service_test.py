import unittest
from unittest import TestCase

from mockito import when
from requests import Response

from ChatGPTChatCLient import ChatGPTChatCLient
from ChatgptService import ChatgptService
from DataRepository import DataRepository


class ChatGPTServiceTest(TestCase):

    def test_throw_exception_when_data_file_does_not_exist(self):
        chat_gpt_chat_client = ChatGPTChatCLient()
        data_repository = DataRepository()
        chat_gpt_service = ChatgptService(chat_gpt_chat_client, data_repository)

        self.assertRaises(FileNotFoundError, chat_gpt_service.updateContextWindowWith, 'filename_does_not_exist.txt')

    def test_returns_error_when_can_not_update_chat_gpt(self):
        chat_gpt_chat_client = ChatGPTChatCLient()
        data_repository = DataRepository()
        fake_response = Response()
        fake_response.status_code = 400
        when(data_repository).read('dummy_data.txt').thenReturn('Some dummy data')
        when(chat_gpt_chat_client).send(...).thenReturn(fake_response)
        chat_gpt_service = ChatgptService(chat_gpt_chat_client, data_repository)

        result = chat_gpt_service.updateContextWindowWith('dummy_data.txt')

        self.assertEqual('error-updating-context-window', result)


if __name__ == '__main__':
    unittest.main()
