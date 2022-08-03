from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Utilities import ConfigReader


class NewCarsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def selectHyundai(self):
        self.click("hyundai_CSS")

    def selectToyota(self):
        self.click("toyota_CSS")

    def selectSkoda(self):
        self.click("skoda_XPATH")

    def selectHonda(self):
        self.click("honda_CSS")

