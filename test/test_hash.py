import sys

from unittest import TestCase
from digfied import hash_code

class TestHash(TestCase):

    def test_hash(self):
        result = hash_code('hola')
        self.assertEqual(result,'4d186321c1a7f0f354b297e8914ab240','failes test')



if __name__ == '__main__':
    unittest.debug()