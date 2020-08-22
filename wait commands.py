#demonstrating implicit wait and explicit wait,synchronization issues in terms of code and page response

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#implicit wait is automatically applied on elements using time in seconds
##driver.implicitly_wait(5)
##driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

##assert "OrangeHRM" in driver.title

##user_ele=driver.find_element_by_name("txtUsername") #checking login button

##pwd_ele=driver.find_element_by_name("txtPassword")

##user_ele.send_keys("admin")
##pwd_ele.send_keys("admin123")
##driver.find_element_by_name("Submit").click()

#explicit wait works using conditions of the elements rather than using time
#exampe using expedia.org
from selenium.webdriver.common.by import By


##driver.maximize_window()

driver.get("https://www.expedia.ie/?pwaLob=wizard-hotel-pwa-v2")
prive_state=driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[1]/header/div[1]/div/div/div[1]/h2")
prive_state.find_element_by_xpath("//*[@id='app']/div[1]/div/div[1]/header/div[1]/div/div/div[2]/button").click()
#finding element using another method
flights=driver.find_element_by_css_selector("#wizard-flight-tab-roundtrip > div > div.uitk-layout-grid-item.uitk-layout-grid-item-columnspan-small-4.uitk-layout-grid-item-columnspan-medium-6.uitk-layout-grid-item-columnspan-large-8 > div > div:nth-child(1) > div > div > div > button")
flights.click()
#driver.find_element_by_xpath("/html/body").click()
#driver.find_element(By.ID,"tab-flight-tab-hp").click()

orig=driver.find_element_by_xpath("")
orig.click()
orig.send_keys("DUB")
distin=driver.find_element_by_id("location-field-leg1-destination-dialog-trigger")
distin.click()
distin.send_keys("ISB")

#driver.find_element_by_id("d1-btn").clear()
#driver.find_element_by_id("d1-btn").send_keys("04/09/2020")

#driver.find_element_by_id("d2-btn").clear()
#driver.find_element_by_id("d2-btn").send_keys("10/10/2020")

#driver.find_element_by_xpath("//*[@id='wizard-flight-pwa-1']/div[4]/div[2]/button").click()






