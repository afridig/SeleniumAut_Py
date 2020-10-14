from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://phptravels.com/demo/") #opens up the website

#driver.save_screenshot("C:\Screenshot\homePage.png") #capturing the screenshot of the specified page and saving it to the target location #accepts jpg, png etc extension

driver.get_screenshot_as_file("C:\Screenshot\homePage2.png") #capturing the screenshot and saving it to the target location #this command only accepts png extension

driver.close()

