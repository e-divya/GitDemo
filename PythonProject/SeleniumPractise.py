import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Using Firefox Driver
firefox = Service("D:/Selenium/Driver/geckodriver")
driver = webdriver.Firefox(service=firefox)
driver.implicitly_wait(6)
# Open Webpage in Selenium
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

expectedProducts = ['Beetroot - 1 Kg','Mushroom - 1 Kg']
actualProducts = []
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("roo")
time.sleep(5)
products = driver.find_elements(By.CSS_SELECTOR, "div [class='product']")
for product in products:
    actualProducts.append(product.find_element(By.CSS_SELECTOR, "h4").text)
    product.find_element(By.CSS_SELECTOR, " div[class='product-action'] button[type='button']").click()
assert expectedProducts == actualProducts
driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
# Verify Total Amount in Cart is correct
amounts = driver.find_elements(By.CSS_SELECTOR, ".cartTable td:nth-child(5) .amount")
summ = 0
for amount in amounts:
    summ = summ + float(amount.text)
print(summ)
totAmt = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert totAmt == summ
# Verify if correct Discount is applied
discT = driver.find_element(By.CSS_SELECTOR, '.discountPerc')
disc = int(discT.text.split('%')[0])
print(disc)
appDisc = totAmt * (disc/100)
totDisc = float(totAmt - appDisc)
print(totDisc)
pageDisc = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(pageDisc)
assert totDisc == pageDisc
print("discount is same")
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
thank = driver.find_element(By.CSS_SELECTOR, ".wrappertwo").text
assert "Thank you" in thank
print("Order Journey completed")
