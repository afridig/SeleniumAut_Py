import time

from selenium import webdriver

fp=webdriver.FirefoxProfile()
#this will disable the window that apears asking wheather to save the file to a certain location etc.
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf") #Mime time
fp.set_preference("browser.download.manager.showWhenStarting",False)
#set the following preferences to change the dafault download location to a different one
fp.set_preference("browser.download.dir","C:\Downloadedfiles") #setting up the desired download location
fp.set_preference("bowser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe",
                         firefox_profile=fp)

driver.get("http://demo.automationtesting.in/FileDownload.html") #opens up the website

driver.maximize_window() #maximizing the window

#downloading text files
driver.find_element_by_id("textbox").send_keys("testing text file downloads") #populating the textbox to anable file generate button
driver.find_element_by_id("createTxt").click() #clicking the file generate button which in turn enables the file download button
driver.find_element_by_id("link-to-download").click() #this will bassically download the link

#downloading pdf files
driver.find_element_by_id("pdfbox").send_keys("testing pdf file downloads") #populating the pdf file text box
driver.find_element_by_id("createPdf").click() #clicking the generate file button
driver.find_element_by_id("pdf-link-to-download").click() #clicking the download link button

time.sleep(4) #gives a few seconds to the browser to download the files

driver.close() #closing the browser