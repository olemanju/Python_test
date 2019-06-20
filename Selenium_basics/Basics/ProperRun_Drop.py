import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

        drp_sel = driver.find_element(By.ID, "carselect")

        sel = Select(drp_sel)

        sel.select_by_index(0)
        time.sleep(3)

        sel.select_by_value("benz")
        time.sleep(3)

        sel.select_by_visible_text("Honda")
        time.sleep(3)

        driver.quit()



ch_browser = BasicTestObject()
ch_browser.launch_browser()
