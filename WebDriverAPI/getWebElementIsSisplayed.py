from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_getWebElementIsDisplayed(self):
        url = "file://d:\\pycharm\\selenium\\WebDriverAPI\\test.html"
        self.driver.get(url)
        # 通过id=“div2”找到第二个div元素
        div2 = self.driver.find_element_by_id("div2")
        # 判断第二个div元素是否在页面上可见
        print(div2.is_displayed())
        # 单击第一个切换div按钮，将第二个div显示在页面上
        self.driver.find_element_by_id("button1").click()
        # 再次判断第二个div元素是否可见
        print(div2.is_displayed())
        # 通过id=“div4”找到第四个div元素
        div4 = self.driver.find_element_by_id("div4")
        # 判断第四个div元素是否在页面上可见
        print(div4.is_displayed())
        # 单击第二个切换div按钮，将第四个div显示在页面上
        self.driver.find_element_by_id("button2").click()
        # 再次判断第四个div元素是否可见
        print(div4.is_displayed())


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()