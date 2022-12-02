import unittest

from cpast.cpast import init


class TestSimple(unittest.TestCase):

    def test_init(self):
        self.assertEqual(init(), 'hello from gitpast :)')


if __name__ == '__main__':
    unittest.main()
