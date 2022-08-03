from Pages.BasePage import BasePage
from Pages.CarWale_NewCars import NewCarsPage


class CarWale_HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def gotoNewCars(self):
        self.moveTo("newCars_XPATH")
        self.click("findNewCar_XPATH")

        return NewCarsPage(self.driver)

    def gotoCompareCars(self):
        pass

    def gotoUsedCars(self):
        pass