from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe")

driver.get("https://fs4.formsite.com/at5MDy/nrdlnwtddk/index.html?1601592570828") #opening the website

element=driver.find_element(By.ID, "RESULT_RadioButton-5")
drp=Select(element)

#Three ways to select options from drop down menus

#First one=Select by visible text
#drp.select_by_visible_text("Morning") #selects morning

#second one = select by index

#drp.select_by_index(2) #selects afternoon

#third one = select by value

#drp.select_by_value("Radio-2") #selects the evening option

# counting number of options in the drop-down
print(len(drp.options))


# capture all the options and print them in the console window

all_options=drp.options

for option in all_options:
    print(option.text)

driver.close()







