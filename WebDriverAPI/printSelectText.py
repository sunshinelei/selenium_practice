from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="d:\\driver\\geckodriver")


    def test_window_size(self):
        url = "file://d:\\pycharm\\selenium\\WebDriverAPI\\select.html"
        self.driver.get(url)
        import time
        time.sleep(3)
        # 使用name属性找到页面上name属性为“fruit”的下拉列表元素
        select = self.driver.find_element_by_name("fruit")
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options:
            print("选项显示的文本: ", option.text)
            print("选项值为: ", option.get_attribute("value"))
            option.click()
            time.sleep(1)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()