from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html") #opening up the website

driver.maximize_window() #this will maximize the window

#Scrolling down by pixels #first approach
#driver.execute_script("window.scrollBy(0,1000)","")

#Scrolling down the page till the required element is visible
#flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[35]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

#Scrolling down till the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

driver.close()
