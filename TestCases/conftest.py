import allure
import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from TestCases import test_SignUpTest
from Utilities import ConfigReader


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name=test_SignUpTest, attachment_type=AttachmentType.PNG)


@pytest.fixture(params=["chrome"], scope="class")
def get_browser(request):
    if request.param == "chrome":

        option1 = Options()
        option1.add_argument("--disable-notifications")

        ser = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=ser)

    request.cls.driver = driver
    driver.get(ConfigReader.readConfig("basic info", "testurl"))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
