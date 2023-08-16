from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# chrome_driver = Service("D:/Selenium/Driver/chromedriver")
# driver = webdriver.Chrome(service=chrome_driver)

firefox_driver = Service("D:/Selenium/Driver/geckodriver")
driver = webdriver.Firefox(service=firefox_driver)

# edge_driver = Service("D:/Selenium/Driver/msedgedriver")
# driver = webdriver.Edge(service=edge_driver)

driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.back()
driver.refresh()
driver.forward()
print(driver.title)
print(driver.current_url)
# driver.minimize_window()
driver.close()

