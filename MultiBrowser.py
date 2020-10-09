from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe") # Using Chrome
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe") #Using Firefox

driver.get("https://www.piac.com.pk/")

print(driver.title) #returns the title of the page

print(driver.current_url) #returns the URL of the page

#print(driver.page_source) #returns the HTML code of the page

driver.close() #Closes the browser

