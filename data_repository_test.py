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


if __name__ == '__main__':
    unittest.main()
