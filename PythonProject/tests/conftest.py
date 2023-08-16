import logging
import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome = Service("D:/Selenium/Driver/chromedriver")
        driver = webdriver.Chrome(service=chrome)
    elif browser_name == "firefox":
        firefox = Service("D:/Selenium/Driver/geckodriver")
        driver = webdriver.Firefox(service=firefox)
    elif browser_name == "edge":
        edge = Service("D:/Selenium/Driver/msedgedriver")
        driver = webdriver.Edge(service=edge)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()

# @pytest.fixture()
# def log(request):
#     logger = logging.getLogger(__name__)
#     filehandler = logging.FileHandler("logfile.log")
#     formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
#     filehandler.setFormatter(formatter)
#     logger.addHandler(filehandler)
#     logger.setLevel(logging.INFO)
#     return logger
