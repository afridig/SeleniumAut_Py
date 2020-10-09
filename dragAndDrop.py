from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html") #opens up the desired webpage

driver.maximize_window() #maximizes the web page for more clarity

source_element=driver.find_element_by_xpath("//*[@id='box3']") #identifying the source element (in this case its Washington)

target_element=driver.find_element_by_xpath("//*[@id='box103']") #identifying the target element

actions=ActionChains(driver) #creating an object for drag and drop activity

actions.drag_and_drop(source_element,target_element).perform() #performing the drag and drop activity

driver.close()


