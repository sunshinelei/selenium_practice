from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_getWebElementIsEnabled(self):
        url = "file://d:\\pycharm\\selenium\\WebDriverAPI\\test1.html"
        self.driver.get(url)
        # 通过id找到第一个input元素
        input1 = self.driver.find_element_by_id("input1")
        # 判断第一个input元素是否可操作
        print(input1.is_enabled())
        # 通过id找到第二个input元素
        input2 = self.driver.find_element_by_id("input2")
        # 判断第二个input元素是否可操作
        print(input2.is_enabled())
        # 通过id找到第三个input元素
        input3 = self.driver.find_element_by_id("input3")
        # 判断第三个input元素是否可操作
        print(input3.is_enabled())



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()