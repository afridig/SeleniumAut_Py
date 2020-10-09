import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe")

#driver.get("https://fs4.formsite.com/form_app/FormSite?FormId=LoadLogin&LoginDestination=%2FFormSite%3FFormId%3DLoadEdit%26FormNbr%3D0") #opening the website #going the longer way
driver.get("https://fs4.formsite.com/at5MDy/nrdlnwtddk/index.html?1601592570828") #going straight for the Volunteer Sign Form
#driver.find_element_by_id("UserId").send_keys("afridi261") #populating the username textbox #going the longer way
#driver.find_element_by_id("Password").send_keys("AutomationP1") #populating the password textbox #going the longer way
#driver.find_element_by_id("login").click() #clicking the login button #going the longer way

#How to find how many input boxes there are in the webpage?
#driver.find_element_by_xpath("/html/body/div[6]/header/a").click() #not needed

inputBoxes = driver.find_elements_by_class_name("text_field") #using a attribute like class_name we can locate multiple elements
print("There are", len(inputBoxes), "textboxes in the 'Volunteer Sign Form'.")

print("The 'Name' textbox is displayed =", driver.find_element(By.ID, "RESULT_TextField-2").is_displayed()) #this will return the status of the textbox

print("The 'Name' textbox is enabled =", driver.find_element(By.ID, "RESULT_TextField-2").is_enabled()) #this will return the status of the textbox if its enabled or not

driver.find_element(By.ID, "RESULT_TextField-2").send_keys("GUL") #populating the Name textbox
driver.find_element(By.ID, "RESULT_TextField-3").send_keys("abc@abcmail.com") #populating the email address textbox
driver.find_element(By.ID, "RESULT_TextField-4").send_keys("123456789")

driver.quit()
