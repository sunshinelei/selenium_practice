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
        # 导入select模块
        from selenium.webdriver.support.ui import Select
        # 使用xpath定位方式获取select页面元素对象
        select_element = Select(self.driver.find_element_by_xpath("//select"))
        # 打印默认选中项的文本
        print(self.first_selected_option.text)
        # 获取所以选择项的页面元素对象
        all_options = select_element.options
        # 打印选项总个数
        print(len(all_options))
        '''
        is_enabled():判断元素是否可操作
        is_selected():判断元素是否被选中
        '''
        if all_options[1].is_enabled() and not all_options[1].is_selected():
            # 方法一：通过序号选择第二个元素，序号从0开始
            select_element.select_by_index(1)
            # 打印已选中项的文本
            print(select_element.all_selected_options[0].text)
            # assertEqual（）方法断言当前选中的选项文本是否是“西瓜”
            self.assertEqual(select_element.all_selected_options[0].text, u"西瓜")
        # 方法二：通过选项的显示文本选择文本为“猕猴桃”选项
        select_element.select_by_visible_text("猕猴桃")
        # 断言已选中项的文本是否是“猕猴桃”
        self.assertEqual(select_element.all_selected_options[0].text, u"猕猴桃")
        time.sleep(2)
        # 方法三：通过选项的value属性值选择value=“shanzha”选项
        select_element.select_by_value("shanzha")
        print(select_element.all_selected_options[0].text)
        self.assertEqual(select_element.all_selected_options[0].text, u"山楂")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()