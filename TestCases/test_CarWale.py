import logging
import time

import pytest

from Pages.CarWale_Base import CarWaleBase
from Pages.CarWale_HomePage import CarWale_HomePage
from TestCases.BaseTest import BaseTest
from Utilities import dataprovider
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_CarWale(BaseTest):

    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("******* Inside New Car Test ********")
        home = CarWale_HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(3)

    @pytest.mark.parametrize("carBrand, carTitle", dataprovider.get_data("NewCarsTest"))
    def test_selectCars(self, carBrand, carTitle):
        log.logger.info("******* Inside Select Car Test ********")
        home = CarWale_HomePage(self.driver)
        car = CarWaleBase(self.driver)
        time.sleep(2)

        if carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("Title of page is : " + title).encode('utf8')
            assert title == carTitle, "Not on correct page as title is different"
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("Title of page is : " + title).encode('utf8')
            assert title == carTitle, "Not on correct page as title is different"
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("Title of page is : " + title).encode('utf8')
            assert title == carTitle, "Not on correct page as title is different"
        elif carBrand == "Skoda":
            home.gotoNewCars().selectSkoda()
            title = car.getCarTitle()
            print("Title of page is : " + title).encode('utf8')
            assert title == carTitle, "Not on correct page as title is different"

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand, carTitle", dataprovider.get_data("NewCarsTest"))
    def test_CarNames(self, carBrand, carTitle):
        log.logger.info("******* Inside Car Names Test ********")
        home = CarWale_HomePage(self.driver)
        car = CarWaleBase(self.driver)
        time.sleep(2)

        if carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("Title of page is : " + title)
            assert title == carTitle, "Not on correct page as title is different"
            car.getCarName()
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("Title of page is : " + title)
            assert title == carTitle, "Not on correct page as title is different"
            car.getCarName()
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("Title of page is : " + title)
            assert title == carTitle, "Not on correct page as title is different"
            car.getCarName()
        elif carBrand == "Skoda":
            home.gotoNewCars().selectSkoda()
            title = car.getCarTitle()
            print("Title of page is : " + title)
            assert title == carTitle, "Not on correct page as title is different"
            car.getCarName()

        time.sleep(3)
