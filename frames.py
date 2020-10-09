from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe")

driver.get("https:/seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to_frame("packageListFrame") #moving to the target left frame window from the main frame window
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click() #clicking on the particular link in the concerned frame
time.sleep(3)

driver.switch_to_default_content() #moving to the second frame to the bottom left from the main frame window
driver.switch_to_frame("packageFrame")
driver.find_element(By.LINK_TEXT,"WebDriver").click() #clicking on the webdriver element in the second frame
time.sleep(3)

driver.switch_to_default_content() #going back to the main frame window
time.sleep(3)

driver.switch_to_frame("classFrame") #switching to the third frame
driver.find_element(By.XPATH,"/html/body/div[1]/ul/li[5]").click() #clicking the Deprecated button in the main frame window
time.sleep(3)

driver.close()


