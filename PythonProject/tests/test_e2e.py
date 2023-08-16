from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest

from pageObjects.HomePage import HomePage
from pageObjects.CheckOutPage import CheckOutPage
from tests.conftest import setup
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homepage = HomePage(self.driver)
        homepage.shopItems().click()
        checkoutpage = CheckOutPage(self.driver)
        products = checkoutpage.getProdTitles()
        cart = checkoutpage.addCart()
        checkoutitems = checkoutpage.checkoutitems()
        i = -1
        for prod in products:
            i = i + 1
            prodName = prod.text
            print(prodName)
            if prodName == "BlackBerry":
                cart[i].click()
                break
        checkoutitems.click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, ".suggestions")))
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        success = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in success

