from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_refreshCurrentPage(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        # 刷新当前页面
        self.driver.refresh()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()