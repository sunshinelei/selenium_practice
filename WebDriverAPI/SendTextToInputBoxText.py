from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_window_size(self):
        url = "file://d:\\pycharm\\selenium\\WebDriverAPI\\test2.html"
        self.driver.get(url)
        # 获取输入框页面对象
        input = self.driver.find_element_by_id("text")
        # 清除输入框中默认内容
        input.clear()
        input.send_keys(u"我是输入的文本内容")
        import time
        # 等待3s，主要看清空输入框内容后的效果
        time.sleep(3)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()