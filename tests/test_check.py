import unittest

from cpast.check import check_date, check_time


DATE: str = '2021-12-25'
BROKEN_DATE: str = '2021-12-0'
OVERPASSED_DATE: str = '2021-12-32'

TIME: str = '22:13:05'
BROKEN_TIME: str = '-1:13:05'
OVERPASSED_TIME: str = '24:13:05'


class TestSimple(unittest.TestCase):

    def test_check_date(self):
        self.assertEqual(check_date(DATE), True)
        self.assertEqual(check_date(BROKEN_DATE), False)
        self.assertEqual(check_date(OVERPASSED_DATE), False)

    def test_check_time(self):
        self.assertEqual(check_time(TIME), True)
        self.assertEqual(check_time(BROKEN_TIME), False)
        self.assertEqual(check_time(OVERPASSED_TIME), False)


if __name__ == '__main__':
    unittest.main()
