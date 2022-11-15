import unittest
from task1 import MyOpenFile as ContMNG


class Test(unittest.TestCase):

    def test_counter(self):
        start = ContMNG.get_num_of_usage()
        with ContMNG() as f:
            f.open_file('sea.txt', 'r')
        finish = ContMNG.get_num_of_usage()
        self.assertEqual(finish, start + 1)

    def test_counter_of_type(self):
        start = ContMNG.get_num_of_usage_types('txt')
        with ContMNG() as f:
            f.open_file('sea.txt', 'r')
        finish = ContMNG.get_num_of_usage_types('txt')
        self.assertEqual(finish, start + 1)

    def test_file_types(self):
        start = ContMNG.file_types['other']
        try:
            with ContMNG() as f:
                f.open_file('1.test')
        except TypeError as error:
            self.assertEqual(str(error), 'The type of file is not enabled.')
        finish = ContMNG.file_types['other']
        self.assertEqual(finish, start + 1)

    def test_open_file(self):
        with ContMNG() as f:
            x = f.open_file('sea.txt')
            status_file = x.closed
        self.assertEqual(status_file, True)

