import os
import unittest
from unittest import TestCase

from DataRepository import DataRepository


class DataRepositoryTest(TestCase):
    def setUp(self):
        if os.path.exists("file_name.txt"):
            os.remove("file_name.txt")

    def tearDown(self):
        if os.path.exists("file_name.txt"):
            os.remove("file_name.txt")

    def test_creates_file_for_appending_data(self):
        dataRepository = DataRepository()

        dataRepository.store('file_name.txt', 'First data')

        self.assertTrue(os.path.isfile('./file_name.txt'))

    def test_appends_data_in_file(self):
        dataRepository = DataRepository()
        dataRepository.store('file_name.txt', 'First data\n')
        dataRepository.store('file_name.txt', 'Second data\n')

        result = dataRepository.read('file_name.txt')

        self.assertEqual('First data\nSecond data\n', result)


if __name__ == '__main__':
    unittest.main()
