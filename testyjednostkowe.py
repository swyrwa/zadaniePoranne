import unittest

class MojTest(unittest.TestCase):

    def setUp(self):
        print("Przygotowanie do testu")

    def testGoogleSearch(self):
        print("testujemy")

    def tearDown(self) -> None:
        print("sprzatamy")

if (__name__== '__main__'):
    unittest.main()