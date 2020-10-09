from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/") #opens up the website

driver.maximize_window() #maximize the window

element=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button") #identifying the element that needs to be double clicked

actions=ActionChains(driver) #declaring a variable to be used for double click action

#double click on the element
actions.double_click(element).perform() #this command will perform a double click on the desired button

driver.close()