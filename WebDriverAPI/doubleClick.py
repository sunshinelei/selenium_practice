from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")
        self.driver = webdriver.Chrome(executable_path="d:\\driver\\chromedriver")

    def test_window_size(self):
        url = "file://d:\\pycharm\\selenium\\WebDriverAPI\\test4.html"
        self.driver.get(url)
        import time
        time.sleep(3)
        # 获取页面输入元素
        inputBox = self.driver.find_element_by_id("inputBox")
        # 导入支持双击操作的模块
        from selenium.webdriver import ActionChains
        # 开始模拟鼠标双击操作
        action_chains = ActionChains(self.driver)
        action_chains.double_click(inputBox).send_keys("hello,world").perform()
        time.sleep(5)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()