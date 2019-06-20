import time
from selenium import webdriver

#Create Class

class BasicTestObject:

    def launch_browser(self):
        # Instantiate Browser
        driver = webdriver.Ie('D:/Softwares/Drivers/IEDriverServer_Win32_3.14.0/IEDriverServer')
        #Open the provided URL
        driver.get("https://www.cricbuzz.com/")


ch_browser = BasicTestObject()
ch_browser.launch_browser()
