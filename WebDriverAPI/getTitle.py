from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_getTitle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 调用driver的title属性获取页面的title属性值
        title = self.driver.title
        print("当前网页的title属性值为: ", title)
        # 断言页面的title属性值是否是“百度一下，你就知道”
        self.assertEqual(title, u"百度一下，你就知道", "页面title属性值错误!")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()