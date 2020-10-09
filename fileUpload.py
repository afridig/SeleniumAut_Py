from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/") #opens up the website

driver.maximize_window() #maximizes the webpage

driver.switch_to_frame(0) #switching to the target frame

driver.find_element_by_name("RESULT_FileUpload-10").send_keys("C://Users/User/Desktop/dummy.txt")

#OR

#file="C://Users/User/Desktop/dummy.txt"
#driver.find_element_by_name("RESULT_FileUpload-10").send_keys(file)

driver.close()

