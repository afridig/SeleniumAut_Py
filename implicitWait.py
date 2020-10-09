from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/") #Opening URL takes some time

driver.implicitly_wait(10) #To make up for the time it takes to fully load the website

print() #returns one line of empty space for clarity

assert "OrangeHRM" in driver.title

user_elem=driver.find_element_by_name("txtUsername")
user_elem.send_keys("admin")

pwd_elem=driver.find_element_by_name("txtPassword")
pwd_elem.send_keys("admin123")
driver.find_element_by_name("Submit").click() #clicks on the login button




