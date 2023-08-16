from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = Service("D:/Selenium/Driver/chromedriver")
driver = webdriver.Chrome(service=browser)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("Divya")
driver.find_element(By.NAME, "email").send_keys("divya.elangovan@outlook.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@123")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.ID, "exampleFormControlSelect1").click()
dropdown = Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
dropdown.select_by_visible_text('Female')

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
# try:
#     assert(message == "Success! The Form has been submitted successfully!.")
#     print("PASS")
#
# except:
#     print("Failed")
# print("Success")
#
#
