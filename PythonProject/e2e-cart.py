from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.FirefoxOptions()
# chrome_options.add_argument("headless")
firefox = Service("D:/Selenium/Driver/geckodriver")
driver = webdriver.Firefox(service=firefox)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
selectProduct = 'Blackberry'
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for prod in products:
    prodName = prod.find_element(By.XPATH, "div/h4/a").text
    if prodName == selectProduct:
        prod.find_element(By.XPATH, "div/button").click()
        break
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight);")
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
wait.until(expected_conditions.invisibility_of_element((By.CSS_SELECTOR, ".suggestions")))
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
success = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in success
driver.close()