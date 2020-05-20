import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewMassagePage(BaseAction):
    # 接收者
    recipients_edit_text = By.ID, "com.android.mms:id/recipients_editor"

    # 内容
    content_edit_text = By.ID, "com.android.mms:id/embedded_text_editor"

    # 发送按钮
    send_button = By.XPATH, "//*[@content-desc='发送']"

    # 发送成功内容
    new_content_edit_text = By.XPATH, "//*[@bounds='[0,2072][1184,2178]']"

    @allure.step(title="输入接受者")
    def input_recipients(self, text):
        allure.attach('接受者：', text, allure.attach_type.TEXT)
        self.input(self.recipients_edit_text, text)
        allure.attach('截图：', self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    @allure.step(title="输入短信内容")
    def input_content(self, text):
        self.input(self.content_edit_text, text)

    @allure.step(title="点击短信发送按钮")
    def click_send(self):
        self.click(self.send_button)

    @allure.step(title="获取发送成功短信内容")
    def get_content_efit_text(self):
        return self.find_element(self.new_content_edit_text).text

