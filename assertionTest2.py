import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebpage=driver.title

        self.assertTrue(titleOfWebpage=="Google") #poitive condition --> test will pass if the the statement returns a TRUE value
        #self.assertTrue(titleOfWebpage == "Google123")  # negative condition --> test will fail if the the statement returns a FALSE value
        #another way to test a negative condition is by assertFalse statement
        #self.assertFalse(titleOfWebpage=="Google") #this statement will return TRUE if the condition becomes in the parenthesis becomes false
        #self.assertFalse(titleOfWebpage=="Google123") #Negative condition returning TRUE as a whole which passes the test

if __name__ == "__main__":
    unittest.main()