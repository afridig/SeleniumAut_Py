import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe") # Using Chrome

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title) #returns the title of the page

print(driver.current_url) #returns the url of the page

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

#driver.close()#closes just the currently focussed browser

driver.quit()#closes all the opened browsers



