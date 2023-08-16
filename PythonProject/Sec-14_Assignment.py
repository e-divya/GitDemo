import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Using Firefox Driver in Headless mode
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("headless")
firefox = Service("D:/Selenium/Driver/geckodriver")
driver = webdriver.Firefox(service=firefox, options=firefox_options)
driver.implicitly_wait(5)
# Open Webpage in Selenium
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "a[class='blinkingText']").click()
time.sleep(5)
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
driver.maximize_window()
emailid = driver.find_element(By.CSS_SELECTOR, "p[class ='red'] a").text
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(emailid)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(emailid)
driver.find_element(By.XPATH, "//label[@class='customradio']/input[@value='user']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#myModal")
driver.find_element(By.CSS_SELECTOR, "#okayBtn").click()
time.sleep(5)
dropdownE = driver.find_element(By.XPATH, "//select[@class='form-control']")
wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.element_to_be_clickable(dropdownE))
dropdown = Select(dropdownE)
dropdown.select_by_value("consult")
driver.find_element(By.CSS_SELECTOR, "#terms").click()
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver, 10)
MsgBox = driver.find_element(By.CSS_SELECTOR, ".alert")
wait.until(expected_conditions.visibility_of(MsgBox))
ErrorMsg = MsgBox.text
assert "Incorrect" in ErrorMsg
print(ErrorMsg)