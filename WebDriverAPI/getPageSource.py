from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_getPageSource(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        # 调用driver的page_source属性获取页面源码
        pageSource = self.driver.page_source
        # 打印页面源码
        print(pageSource)
        # 断言页面源码中是否包含“新闻”两个关键字，以此判断页面内容是否正确
        self.assertTrue(u"新闻"in pageSource, "页面源码中未找到'新闻'关键字")



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()