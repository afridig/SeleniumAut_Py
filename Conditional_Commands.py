from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")
print() #returns one line of empty space for clarity
user_elem=driver.find_element_by_name("txtUsername")
print("username box is displayed =",user_elem.is_displayed()) #checks weather the element is displayed or not, returns a True or False Value based on the status
print()
print("username box is enabled =",user_elem.is_enabled()) #returns True or False
print()
pwd_elem=driver.find_element_by_name("txtPassword")
print("password box is displayed =",pwd_elem.is_displayed()) #checks weather the element is displayed or not, returns a True or False Value based on the status

print()
print("password box is enabled =",pwd_elem.is_enabled()) #returns True or False
print()
user_elem.send_keys("admin")
pwd_elem.send_keys("admin123")

driver.find_element_by_name("Submit").click() #clicks on the login button

leaveMod=driver.find_element_by_id("menu_leave_viewLeaveModule")
leaveMod.click()

leaveList=driver.find_element_by_id("menu_leave_viewLeaveList")
leaveList.click() #clicks the leaveList module button

pendApproval=driver.find_element_by_id("leaveList_chkSearchFilter_1")
print("Pending Approval chkbox is selected =",pendApproval.is_selected())
print()
cancelledChkbx=driver.find_element_by_id("leaveList_chkSearchFilter_0")
print("Cancelled chkbox is selected =",cancelledChkbx.is_selected())

driver.close()

#The following code demnstrates if these were radio buttons on another websited

#driver.get("https://www.piac.com.pk/") #accessing PIA website
#driver.find_element_by_id("popup").click() #closing the initial popup window
#print()
#roundTripButton = driver.find_element_by_css_selector("input[value=ROUND_TRIP")
#print("Return trip radio button is selected =", roundTripButton.is_selected()) #checking the status of the Return radi0 button
#print() #returns a line's space for clarity

#oneWayButton = driver.find_element_by_css_selector("input[value=ONE_WAY")
#print("One way radio button is selected =", oneWayButton.is_selected()) #checking the status of the One Way radio button
#print() #returns a line's space for clarity

#driver.close()






