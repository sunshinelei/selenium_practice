from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_visitURL(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 获取当前浏览器在屏幕上的位置，返回的是字典对象
        position = self.driver.get_window_position()
        print(position)
        print("当前浏览器所在位置的横坐标: ", position['x'])
        print("当前浏览器所在位置的纵坐标: ", position['y'])
        # 设置当前浏览器在屏幕上的位置
        self.driver.set_window_position(y = 200, x = 400)
        # 设置浏览器的位置后，再次获取浏览器的位置
        print(self.driver.get_window_position())


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()