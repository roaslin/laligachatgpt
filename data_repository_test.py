import os
import unittest
from unittest import TestCase

from data_repository import DataRepository

FILE_NAME = 'file_name.txt'


class DataRepositoryTest(TestCase):
    def setUp(self):
        if os.path.exists('%s' % FILE_NAME):
            os.remove(FILE_NAME)

    def tearDown(self):
        if os.path.exists('%s' % FILE_NAME):
            os.remove(FILE_NAME)

    def test_creates_file_for_appending_data(self):
        data_repository = DataRepository()

        data_repository.store(FILE_NAME, 'First data')

        self.assertTrue(os.path.isfile('./%s' % FILE_NAME))

    def test_appends_data_in_file(self):
        data_repository = DataRepository()
        data_repository.store(FILE_NAME, 'First data\n')
        data_repository.store(FILE_NAME, 'Second data\n')

        result = data_repository.read(FILE_NAME)

        self.assertEqual('First data\nSecond data\n', result)


if __name__ == '__main__':
    unittest.main()
