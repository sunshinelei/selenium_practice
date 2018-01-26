from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_getBasicInfo(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 查找百度首页上的“新闻”链接元素
        newsElement = self.driver.find_element_by_xpath("//a[text() = '新闻']")
        # 获取查找到的“新闻”链接元素的基本信息
        print(u"元素的标签名: ", newsElement.tag_name)
        print(u"元素的size: ", newsElement.size)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()