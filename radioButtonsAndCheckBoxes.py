import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe")
#driver=webdriver.Ie(executable_path="C:\Drivers\IEDriverServer_x64_3.150.1\IEDriverServer.exe") #using Internet Explorer
driver.get("https://fs4.formsite.com/at5MDy/nrdlnwtddk/index.html?1601592570828") #going straight for the Volunteer Sign Form

inputBoxes = driver.find_elements_by_class_name("text_field") #using a attribute like class_name we can locate multiple elements
print("There are", len(inputBoxes), "textboxes in the 'Volunteer Sign Form'.")

print("The 'Name' textbox is displayed =", driver.find_element(By.ID, "RESULT_TextField-2").is_displayed()) #this will return the status of the textbox

print("The 'Name' textbox is enabled =", driver.find_element(By.ID, "RESULT_TextField-2").is_enabled()) #this will return the status of the textbox if its enabled or not

driver.find_element(By.ID, "RESULT_TextField-2").send_keys("GUL") #populating the Name textbox
driver.find_element(By.ID, "RESULT_TextField-3").send_keys("abc@abcmail.com") #populating the email address textbox
driver.find_element(By.ID, "RESULT_TextField-4").send_keys("123456789") #populating the phone number field
driver.find_element_by_id("RESULT_TextField-6").send_keys("Main Street") #populating the street field
driver.find_element(By.ID, "RESULT_TextField-7").send_keys("Mardan") #City field
driver.find_element(By.ID, "RESULT_TextField-8").send_keys("VA") #State field
driver.find_element(By.ID, "RESULT_TextField-9").send_keys("23200") #Zip Code field



#working with the radio buttons

radioButt1D = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[20]/table/tbody/tr[1]/td/label").is_displayed() #checking weather the radio button is displayed or not
radioButt1S = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[20]/table/tbody/tr[1]/td/label").is_selected() #weather its selected or not
radioButt1E = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[20]/table/tbody/tr[1]/td/label").is_enabled() #weather its enabled or not

print() #one line space for clarity
print("Radio Button 'Yes' (Volunteer work authoriaztion) is displayed =", radioButt1D) #printing the value
print("Radio Button 'Yes' (Volunteer work authoriaztion) is selected =", radioButt1S) #printing the value
print("Radio Button 'Yes' (Volunteer work authoriaztion) is enabled =", radioButt1E) #printing the value

#time.sleep(4)
#wait = WebDriverWait(driver,20) #declaring a variable to hold values for explicit wait conditions

#radioButton1 = wait.until(EC.element_to_be_clickable((By.ID, "RESULT_RadioButton-10_1"))) #varifying a condition on the concerned element

#radioButton1.click() #clicking the element

#The above code (WebDriveWait) didn't work to resolve the issue with the element obsecurity

driver.find_element_by_xpath("/html/body/form/div[2]/div[17]/table/tbody/tr/td[1]/label").click() #click the Radio Button 'Yes' #not working says another element obsecures it
print("Radio Button 'Yes' (Volunteer work authoriaztion) is selected =", radioButt1S) #printing the status

#working with checkboxes

driver.find_element(By.XPATH, "/html/body/form/div[2]/div[20]/table/tbody/tr[1]/td/label").click() #ticking the Sunday checkbox
driver.find_element(By.XPATH, "/html/body/form/div[2]/div[20]/table/tbody/tr[7]/td/label").click() #ticking the Saturday checkbox
driver.find_element(By.XPATH,"/html/body/form/div[2]/div[19]/table/tbody/tr[4]/td/label").click() #clicking 'NewsPaper Advertisement# to the question where did you hear about us

satChkBox=driver.find_element(By.XPATH, "/html/body/form/div[2]/div[20]/table/tbody/tr[7]/td/label").is_selected() #Checking the status of the Saturday checkbox
print("Saturday checkbox is selected =",satChkBox) #printing the status of the Saturday checkbox

driver.quit()




