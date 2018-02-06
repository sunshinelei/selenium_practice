from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_window_size(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 找到搜索输入框
        searchBox = self.driver.find_element_by_id("kw")
        # 使用页面元素对象的value_of_css_property()方法获取元素的CSS属性值
        print(u"搜索输入框的高度是: ", searchBox.value_of_css_property("height"))
        print(u"搜索输入框的宽度是: ", searchBox.value_of_css_property("width"))
        font = searchBox.value_of_css_property("font-family")
        print(u"搜索输入框的字体是: ", font)
        # 断言搜索输入框的字体是否是arial字体
        self.assertEqual(font, "arial")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()