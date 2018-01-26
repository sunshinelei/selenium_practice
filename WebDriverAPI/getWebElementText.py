from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_getWebElementText(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        import time
        time.sleep(3)
        # 通过xpath定位方式找到id属性值为“u1”的div元素下的第一个链接元素
        aElement = self.driver.find_element_by_xpath("//*[@class='mnav'][6]")
        # 通过找到的链接元素对象的text属性获取到链接元素的文本内容
        a_text = aElement.text
        self.assertEqual(a_text, u"学术")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()