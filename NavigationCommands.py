import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

print() #resturns a line's space for clarity
driver.get("https://www.piac.com.pk/") #opens PIA Airlines website
print(driver.title) #captures the title of the PIA page
print("Waits for 5 seconds at this site and then goes to Pakistan Post website and prints its title as follows")
time.sleep(5) #waits for 5 seconds

driver.get("http://www.pakpost.gov.pk/") #opens Pakistan Post website
print(driver.title) #returns the title of Pakistan website page
print()
print("Waits for 5 seconds at this site and then goes to Pakistan Airlines website and prints its title as follows")
time.sleep(5) #waits for 5 seconds

driver.back() #navigates back to PIA website
print(driver.title) #prints out title of the PIA website
print("Waits for 5 seconds at this site and then goes to Pakistan Post website and prints its title as follows")
time.sleep(5) #waits for 5 seconds

driver.forward() #goes back to Pakistan Post website
print(driver.title) #prints out the title of PP website again

driver.close()







