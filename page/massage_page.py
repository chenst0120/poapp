import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MassagePage(BaseAction):
    # 新增短信按钮
    new_massage_button = By.ID, "com.android.mms:id/action_compose_new"

    @allure.step(title="点击新增短信")
    def click_new_massage(self):
        self.click(self.new_massage_button)