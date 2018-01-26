from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_maximizeWindow(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 最大化浏览器窗口
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()