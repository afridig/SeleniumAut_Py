from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe")

driver.get("https://techcanvass.com/examples/webtable.html") #opening the website where the webtable resides

tableRows=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr")) #rows in the table
print(tableRows) #printing the number of rows in the table

tableCols=(len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th")) )#this will capture, count  and store the number of columns in the table
print(tableCols) #printing the number of columns present in the table

print("Company Name"+"  "+"	Make"+"     "+"Ex-showroom Price(INR)") #printing the header row separately

for r in range(2,tableRows+1):
    for c in range(1,tableCols+1):
        value=driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text #extracting the values from the rows and columns dynamically
        print(value,end='         ') #putting the data in proper tabular format
    print()

driver.close()





