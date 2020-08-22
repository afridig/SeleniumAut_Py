from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

##testing sign in functionality

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
user_ele=driver.find_element_by_name("txtUsername") #checking login button
print(user_ele.is_displayed()) #returns True or False based on the status of the element
print(user_ele.is_enabled()) #returns true or false

pwd_ele=driver.find_element_by_name("txtPassword")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

#populating sign in and password fields and clicking sign in button
user_ele.send_keys("admin")
pwd_ele.send_keys("admin123")
driver.find_element_by_name("Submit").click()

#using id attribute and checking default selected state
leave_ele=driver.find_element_by_id("menu_leave_viewLeaveModule").click()
leave_ele_1=driver.find_element_by_id("ui-datepicker-div")
print(leave_ele_1.is_displayed())
print(leave_ele_1.is_enabled())
print(leave_ele_1.is_selected())

#another example with radio buttons
driver.get("https://www.edreams.com/")
print(driver.title)
radio_roundtrip=driver.find_element_by_id("tripTypeSwitcher_roundTrip")
radio_roundtrip=driver.find_element_by_css_selector("input[id=tripTypeSwitcher_roundTrip]")
print()
print("Status of round trip radio button is checked =",radio_roundtrip.is_selected())

radio_oneway=driver.find_element_by_id("tripTypeSwitcher_oneWayTrip")
print("Status of one way radio button is selected=",radio_oneway.is_selected())




















