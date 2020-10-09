from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe")

driver.get("https://phptravels.com/demo/") #opening the website

links=driver.find_elements(By.TAG_NAME, "a") #capture all the links and storing them in a variable

print("Number of links present in the webpage are: ",len(links)) #print how many links present in a page

#extracting each and every link from links list and printing them
#for loop will read each link and print the same out

for link in links:
    print(link.text)

#Clicking on the link, either by using the link_text method or partial link_text method

#driver.find_element(By.LINK_TEXT,"Pricing").click()
driver.find_element_by_partial_link_text("Pri").click()

driver.close()








