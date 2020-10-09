from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html") #openng the website

driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click() #clicking on the button

print(driver.current_window_handle) #returns the current window's handle value and prints it off

handles=driver.window_handles #stores handle values of all the windows that are opened

for handle in handles:
    driver.switch_to_window(handle)
    print(driver.title) #prints the titles of the windows

    if driver.title=="Frames & windows":
        driver.close() #this will just close the parent window

driver.quit()

