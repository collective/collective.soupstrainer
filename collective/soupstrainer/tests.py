import unittest
from collective.soupstrainer import SoupStrainer
import BeautifulSoup

class TestCase(unittest.TestCase):
    def test_return_type(self):
        strainer = SoupStrainer()
        data = u''
        self.assertTrue(isinstance(strainer(data), unicode))
        data = BeautifulSoup.BeautifulSoup(u'')
        self.assertTrue(isinstance(strainer(data), BeautifulSoup.Tag))

def test_suite():
    import sys
    return unittest.findTestCases(sys.modules[__name__])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
