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

        gettitle = driver.title
        print(gettitle)

        time.sleep(3)

        bmw_rad = driver.find_element(By.ID, "bmwradio")
        if bmw_rad.is_displayed():
            bmw_rad.click()
        else:
            print("BMW Radio button is not Present")

        time.sleep(3)

        honda_rad = driver.find_element(By.ID, "hondaradio")

        if honda_rad.is_displayed():
            honda_rad.click()
        else:
            print("Honda Radio button is not Present")

        time.sleep(3)
        # Check box Selection

        bmw_check = driver.find_element(By.ID, "bmwcheck")

        if bmw_check.is_displayed():
            bmw_check.click()
        else:
            print("BMW Check box Checked")

        time.sleep(3)


        Total_ckeckboxes = driver.find_elements_by_xpath("//div[@id='checkbox-example']/fieldset//label/input")

        if len(Total_ckeckboxes) > 0:
            print("Check boxes are present")
            for x in Total_ckeckboxes:
                x.click()
        time.sleep(3)
        driver.quit()



ch_browser = BasicTestObject()
ch_browser.launch_browser()
