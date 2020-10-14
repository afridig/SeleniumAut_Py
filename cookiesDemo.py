import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.com/") #opens up the website

#capture all the cookies created by the browser

cookies=driver.get_cookies()
print(len(cookies)) #print the number of cookies that have been created
print(cookies) #print all the cookies pairs

#adding new cookies to the browser
cookie={'name':'Mycookie', 'value':'1234567890'} #creating a cookie pair
driver.add_cookie(cookie) #adding that cookie to the browser

#repeting the code to compare the new number of cookies after the addition we just performed
cookies=driver.get_cookies()
print(len(cookies)) #print the number of cookies that have been created
print(cookies) #print all the cookies pairs

#deleting the cookie
driver.delete_cookie("Mycookie")
time.sleep(3)

#repeting the code to compare the new number of cookies after the delete action we just performed
cookies=driver.get_cookies()
print(len(cookies)) #print the number of cookies that have been created
print(cookies) #print all the cookies pairs

#deleting all the cookies
driver.delete_all_cookies() #deleting all the cookies
cookies=driver.get_cookies() #capturing all the cookies after performing the delete action
print(len(cookies)) #0

driver.close()


