import XLUtils

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/") #opens up the website

driver.maximize_window() #maximizing the window

path="C:\\Users\\User\\Desktop\\TestData.xlsx"

rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username=XLUtils.readData(path,"Sheet1",r,1)
    password=XLUtils.readData(path,"Sheet1",r,2)

    driver.find_element_by_name("txtUsername").send_keys(username) #populating username field
    driver.find_element_by_name("txtPassword").send_keys(password) #populating password field

    driver.find_element_by_name("Submit").click() #clicking submit

    if driver.title=="OrangeHRM":
        print("Our test is passed")
        XLUtils.writeData(path,"Sheet1",r,3,"test passed") #populating column 3 in case of passed tests, in the target data file

    else:
        print("test failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed") #populating column 3 in case of failed tests, in the target data file

        element=driver.find_element_by_id("welcome").click() #navigating back to the Home page to restart the login process
        drp=Select(element)
        drp.select_by_value("Logout")

driver.close()

