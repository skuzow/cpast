import os
import unittest

from cpast.core import format_date, prepare_vars


DATE: str = '2021-12-25'
TIME: str = '22:13:05'
FORMATTED_DATE: str = '"2021-12-25T22:13:05"'


class TestSimple(unittest.TestCase):

    def test_format_date(self):
        self.assertEqual(format_date(DATE, TIME), FORMATTED_DATE)

    def test_prepare_vars(self):
        prepare_vars(FORMATTED_DATE)
        self.assertEqual(os.environ['GIT_AUTHOR_DATE'], FORMATTED_DATE)
        self.assertEqual(os.environ['GIT_COMMITTER_DATE'], FORMATTED_DATE)


if __name__ == '__main__':
    unittest.main()
