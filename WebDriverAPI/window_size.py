from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_window_size(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 获取浏览器窗口的大小，返回字典类型
        sizeDict = self.driver.get_window_size()
        print(sizeDict)
        print("当前浏览器窗口的宽: ", sizeDict['width'])
        print("当前浏览器窗口的高: ", sizeDict['height'])
        # 设置浏览器窗口的大小
        self.driver.set_window_size(width= 200, height= 400, windowHandle= 'current')
        # 设置浏览器窗口的大小后，再次获取浏览器窗口大小信息
        print(self.driver.get_window_size(windowHandle= 'current'))


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()