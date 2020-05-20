from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=10, poll=1):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def click(self, loc):
        self.find_element(loc).click()

    def input(self, loc, content):
        self.find_element(loc).send_keys(content)

    def clear(self, loc):
        self.find_element(loc).clear()

    def press_back(self):
        self.driver.press_keycode(4)

    def press_enter(self):
        self.driver.press_keycode(66)