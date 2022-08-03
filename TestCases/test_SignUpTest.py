import logging
import pytest

from Pages.RegistrationPage import RegistrationPage
from TestCases.BaseTest import BaseTest
from Utilities.dataprovider import get_data
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_SignUpTest(BaseTest):

    @pytest.mark.parametrize("name, phone, email, country, city, username, password", get_data("LoginTest"))
    def test_doSignUp(self, name, phone, email, country, city, username, password):
        log.logger.info("Test Do Sign Up started")
        regpage = RegistrationPage(self.driver)
        regpage.fillform(name, phone, email, country, city, username, password)
        log.logger.info("Test Do Sign Up successfully executed")