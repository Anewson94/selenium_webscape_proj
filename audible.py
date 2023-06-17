from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

chrome_driver_path = "/Users/dacano/Documents/udemy.nosync/Web_Scraping/driver/chromedriver_mac_arm64"
driver = webdriver.Chrome()

website = "https://www.audible.com/search"
driver.get(website)
driver.maximize_window()
driver.implicitly_wait(5)

container = driver.find_element(By.XPATH, '//li[contains(@class, "productListItem")]')
products = container.find_elements(By.XPATH, "./li")

titles = []
authors = []
runtimes = []
for product in products:
    # titles.append(product.find_elements(By.XPATH, ".//h3[contains(@class, 'bc-heading')]").text)
    authors.append(product.find_elements(By.XPATH, "//li[contains(@class, 'authorLabel')]").text)
    runtimes.append(product.find_elements(By.XPATH, "//li[contains(@class, 'runtimeLabel')]").text)

driver.quit()
print(titles)
dfbooks = pd.DataFrame({"Title": titles, "Author": authors, "Runtime": runtimes})
dfbooks.to_csv("books.csv", index=True)