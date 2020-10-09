from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe")

driver.get("http://testautomationpractice.blogspot.com/") #opening the webpage

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click() #clicking on the Alert button

time.sleep(5)

#driver.switch_to_alert().accept() #closes the alert window by using the OK button

driver.switch_to_alert().dismiss() #closes the alert window by using the CANCEL button

driver.close()