from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html") #opens up the website

button=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span") #identifying the elemet that needs to be right-clicked

actions=ActionChains(driver) #creating an object to use in the right click command

actions.context_click(button).perform() #right clicking on the desired button

driver.close()