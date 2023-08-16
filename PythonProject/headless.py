from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome = Service("D:/Selenium/Driver/chromedriver")
driver = webdriver.Chrome(service=chrome)
driver.implicitly_wait(5)
browserSorted = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
# driver.find_element(By.XPATH, "//a[text()='Top Deals']").click()
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

Elements = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in Elements:
    browserSorted.append(element.text)

browserSortOrg = browserSorted.copy()
print(browserSortOrg)
browserSorted.sort()

print(browserSorted)
assert browserSorted == browserSortOrg

print("Sort success")