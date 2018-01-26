from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_visitRecentURL(self):
        firstvisitURL = "http://www.sogou.com"
        secondvisitURL = "http://www.baidu.com"
        # 首先访问搜狗首页
        self.driver.get(firstvisitURL)
        # 然后访问百度首页
        self.driver.get(secondvisitURL)
        # 返回上一次访问过的搜狗首页
        self.driver.back()
        # 再次回到百度首页
        self.driver.forward()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()