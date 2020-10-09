from selenium import webdriver
from selenium.webdriver import ActionChains

#driver=webdriver.Ie(executable_path="C:\Drivers\IEDriverServer_Win32_3.150.1\IEDriverServer.exe") #taking too long to go beyond loading the initial page
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/") #opens up the website

driver.find_element_by_name("txtUsername").send_keys("admin") #populating the username text box

driver.find_element_by_name("txtPassword").send_keys("admin123") #populating the password text box

driver.find_element_by_name("Submit").click() #clicking the login

admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b") #identifying the admin tab and storing it in the admin variable
user_manag=driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']") #identifying the user management tab and storing it user_manag variavle
users=driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']") #identifying the users tab and storing it in the users variable

actions=ActionChains(driver) #defining an object to be used when prforming the mouse over action

#the following is the mouse over action
actions.move_to_element(admin).move_to_element(user_manag).move_to_element(users).click().perform() #moving to the desired tab and diving in to the sub tabs and clicking the final tab

driver.close()

