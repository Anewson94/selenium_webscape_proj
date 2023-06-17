from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

chrome_driver_path = "/Users/dacano/Documents/udemy.nosync/Web_Scraping/driver/chromedriver_mac_arm64"
driver = webdriver.Chrome()

website_url = "https://www.adamchoi.co.uk/overs/detailed"
# Opens website, clicks all matches button
driver.get(website_url)
all_matches_btn = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]')
all_matches_btn.click()
time.sleep(5)


date = []
home_team = []
score = []
away_team = []
matches = driver.find_elements(By.TAG_NAME, "tr")

for match in matches:
    match_elements = match.find_elements(By.XPATH, '//td')
    if len(match_elements) >= 4:
        date.append(match_elements[0].text)
        home_team.append(match_elements[1].text)
        score.append(match_elements[2].text)
        away_team.append(match_elements[3].text)

dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("France")
time.sleep(5)

driver.quit()

df = pd.DataFrame({"Date": date, "Home Team": home_team, "Score": score, "Away Team": away_team})
df.to_csv("Soccer_data.csv", index=True, header=True)
print(df)

# XPath examples of console in web browser // example of assigning to variable below in step 4
###############################################################################################
# Example locater using xpath where input is the element tag, username is the ID
# $x("//input[@id='username']")
# Example of class locator without specific area where button is the element tag
# $x("//button")
# Selecting specific element by class where button is element tag and class is specific class we are trying to reach
# $x("//button[@class='btn']")
# submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")

# by ID name
# element = driver.find_element_by_id("element_id")
# by name
# element = driver.find_element_by_name("element_name")
# by class name
# element = driver.find_element_by_class_name("element_class")
# by tag name
# element = driver.find_element_by_tag_name("div")
# by CSS selector
# element = driver.find_element_by_css_selector("#element_id")