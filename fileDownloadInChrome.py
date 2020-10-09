import time

from selenium import webdriver

#import the following class to change the dafault download location to a different one
from selenium.webdriver.chrome.options import Options

chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": "C:\Downloadedfiles"})

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe",chrome_options=chromeOptions)

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



