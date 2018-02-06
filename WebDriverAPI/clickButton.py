from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_window_size(self):
        url = "file://d:\\pycharm\\selenium\\WebDriverAPI\\test3.html"
        self.driver.get(url)
        import time
        time.sleep(3)
        # 获取按钮页面对象
        button = self.driver.find_element_by_id("button")
        # 模拟鼠标左键单击操作
        button.click()
        time.sleep(3)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()