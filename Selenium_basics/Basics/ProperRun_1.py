import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Create Class

class BasicTestObject:

    def launch_browser(self):
        # Instantiate Browser
        driver = webdriver.Chrome('D:/Softwares/Drivers/chromedriver_win32/chromedriver')
        #Open the provided URL
        driver.get("https://letskodeit.teachable.com/pages/practice")

        driver.maximize_window()
        driver.implicitly_wait(20)

        driver.find_element_by_xpath("(//a[contains(text(),'Sign Up')])[1]").click()

        gettitle = driver.title
        print(gettitle)

        User_name = driver.find_element(By.ID, "user_name")
        User_name.send_keys("Manjunatha")

        User_email = driver.find_element(By.ID, "user_email")
        User_email.send_keys("achintyamanjunatha@gmail.com")





        driver.quit()



ch_browser = BasicTestObject()
ch_browser.launch_browser()
