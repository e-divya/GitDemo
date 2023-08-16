from selenium.webdriver.common.by import By

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver


    prodtitles = (By.CSS_SELECTOR, ".card-title a")
    addcart = (By.CSS_SELECTOR, ".card-footer button")
    checkoutitems = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getProdTitles(self):
        return self.driver.find_elements(*CheckOutPage.prodtitles)
    def addCart(self):
        return self.driver.find_elements(*CheckOutPage.addcart)
    def checkoutitems(self):
        return self.driver.find_elements(*CheckOutPage.checkoutitems)