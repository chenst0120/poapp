from page.massage_page import MassagePage
from page.new_massage_page import NewMassagePage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def massage(self):
        return MassagePage(self.driver)

    @property
    def new_massage(self):
        return NewMassagePage(self.driver)
