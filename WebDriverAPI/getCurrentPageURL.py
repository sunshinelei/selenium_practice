from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_getCurrentPageURL(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        # 获取当前页面的URL
        currentPageURL = self.driver.current_url
        # 打印当前URL
        print(currentPageURL)
        # 断言当前网页的网址是否为https://www.sogou.com/
        self.assertEqual(currentPageURL, "https://www.sogou.com/", "当前网页网址非预期!")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()