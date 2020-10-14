#assertIsNone & assertNotNone

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.assertIsNone(driver) #nagative test.. this will return a FALSE value and test will fail

        #positive test
        #driver=None #test will pass as the this statement will return TRUE
        #self.assertIsNone(driver)

        #using the assertIsNotNone command
        #self.assertIsNotNone(driver) #this will return TRUE if the driver object contains a NONE value otherwise FALSE
        #driver=None #this will return a FALSE in case of assertIsNotNone command producing a failes test

if __name__ == "__main__":
    unittest.main()