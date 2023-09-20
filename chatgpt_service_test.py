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
        fake_response = self.build_error_response()
        when(data_repository).read('dummy_data.txt').thenReturn('Some dummy data')
        when(chat_gpt_chat_client).send(...).thenReturn(fake_response)
        chat_gpt_service = ChatgptService(chat_gpt_chat_client, data_repository)

        result = chat_gpt_service.updateContextWindowWith('dummy_data.txt')

        self.assertEqual('error-updating-context-window', result)

    def test_returns_context_window_updated_when_can_update_chat_gpt_with_new_data(self):
        chat_gpt_chat_client = ChatGPTChatCLient()
        data_repository = DataRepository()
        fake_ok_response = self.build_ok_response()
        when(data_repository).read('dummy_data.txt').thenReturn('Some dummy data')
        when(chat_gpt_chat_client).send(...).thenReturn(fake_ok_response)
        chat_gpt_service = ChatgptService(chat_gpt_chat_client, data_repository)

        result = chat_gpt_service.updateContextWindowWith('dummy_data.txt')

        self.assertEqual('context-window-updated', result)

    def build_error_response(self):
        fake_response = Response()
        fake_response.status_code = 400
        return fake_response
    def build_ok_response(self):
        fake_response = Response()
        fake_response.status_code = 200
        return fake_response


if __name__ == '__main__':
    unittest.main()
