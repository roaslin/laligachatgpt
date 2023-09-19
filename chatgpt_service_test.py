import unittest
from unittest import TestCase

from ChatgptService import ChatgptService


class ChatGPTServiceTest(TestCase):

    def test_throw_exception_when_data_file_does_not_exist(self):
        chat_gpt_service = ChatgptService('file_does_not_exist.txt')

        self.assertRaises(FileNotFoundError, chat_gpt_service.ask, 'My question that')


if __name__ == '__main__':
    unittest.main()
