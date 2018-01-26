from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_visitURL(self):
        visitURL = "http://www.sogou.com"
        self.driver.get(visitURL)
        assert self.driver.title.find(u"搜狗搜索引擎") >= 0, "assert error"


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()