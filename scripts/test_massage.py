# import os,sys
# sys.path.append(os.getcwd())
import datetime
import pytest
import time
import allure

from base.base_analyze import analyze_file
from base.base_driver import driver
from page.page import Page

class TestMassage:
    def setup(self):
        self.driver = driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # 严重级别
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    # @pytest.mark.parametrize(("reps", "cont"),[("110","0"),("120","1")])
    @pytest.mark.parametrize("arge", analyze_file("massage_data.yaml","test_massage"))
    def test_send_massage(self, arge):
        reps = arge["reps"]
        cont = arge["cont"]
        print(reps)
        print(cont)

        # 点击新建短信
        self.page.massage.click_new_massage()

        # 输入 接收人
        self.page.new_massage.input_recipients(reps)

        # 输入 内容
        self.page.new_massage.input_content(cont)

        # 点击发送
        self.page.new_massage.click_send()

        # 断言
        assert cont == self.page.new_massage.get_content_efit_text()


