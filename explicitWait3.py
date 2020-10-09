import time

import aria as aria
import button as button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

#driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe")

driver.get("https://www.ebookers.ie/")

driver.implicitly_wait(5) #this wait command belongs to the Webdriver

driver.maximize_window()
#time.sleep(3)

driver.find_element(By.ID, "mad-client-gdpr-banner-button").click() #click Accept cookies

#time.sleep(2)

driver.find_element_by_xpath("/html/body/meso-native-marquee/section/div/div/div[1]/div[1]/div/button/span[1]").click() #closing the COVID notice

#time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='tab-flight-tab-hp']/span[1]").click() #click the Flights button
#time.sleep(4)

driver.find_element(By.ID, "flight-type-one-way-label-hp-flight").click()

#time.sleep(3)

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("Dublin (DUB-Dublin)") #populating the departure text box
#time.sleep(4)

driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("Islamabad (ISB-Islamabad Intl.)"+"\n") #populating the destination text box
#time.sleep(4)

#driver.find_element(By.ID, "flight-departing-hp-flight").clear() #clearing the round trip departure date picker field
#time.sleep(4)
#driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("31/10/2020"+Keys.RETURN) #populating round trip departure field #not working towards the end

element=driver.find_element(By.ID, "flight-departing-single-hp-flight")
element.send_keys("31/10/2020"+Keys.RETURN) #going the One Way option

#driver.find_element(By.ID, "flight-returning-hp-flight").clear() #clearing the return date picker field
#driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("29/11/2020"+ Keys.RETURN) #populating the field #wont take the data in
#time.sleep(4)

#driver.find_element_by_xpath("/html/body/meso-native-marquee/section/div/div/div[1]/div[2]/div/div[1]/div/section[1]/form/div[8]/label/button").click() #clicking the Search button #not working
#wait = WebDriverWait(driver,10) #declaring a variable to hold values for explicit wait conditions

#element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/meso-native-marquee/section/div/div/div[1]/div[2]/div/div[1]/div/section[1]/form/div[8]/label/button"))) #varifying a condition on the concerned element

#element.click() #clicking the element
#time.sleep(4)
wait = WebDriverWait(driver,10) #declaring a variable to hold values for explicit wait conditions

element1 = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-1"))) #varifying a condition on the concerned element

element1.click() #clicking the element

#time.sleep(3)

driver.quit()


