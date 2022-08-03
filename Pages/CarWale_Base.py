from selenium.webdriver.common.by import By

from Utilities import ConfigReader


class CarWaleBase:

    def __init__(self, driver):
        self.driver = driver

    def getCarTitle(self):
        return self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", "car_Title_XPATH")).text

    def getCarName(self):
        carNames = self.driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", "car_Names_XPATH")).text
        carPrice = self.driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", "car_Price_XPATH")).text

        for i in range(1, len(carPrice)):
            print("Car Name is : ", carNames[i])
