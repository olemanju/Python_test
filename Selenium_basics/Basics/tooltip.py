from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class ToolTip:


    def launchBrowser(self):
        driver = webdriver.Chrome('D:/Softwares/Drivers/Chrome/79/chromedriver_win32/chromedriver.exe')

        driver.get("https://demoqa.com/tooltip/")

        driver.maximize_window()
        driver.implicitly_wait(20)

        para_val= driver.find_element_by_xpath("(//p)[1]").text
        print(para_val)
        va= para_val[0:40]
        print(va)

        age_text= driver.find_element_by_id('age')
        att_val= age_text.get_attribute("title")
        print(att_val)

        age_text.send_keys(Keys.SHIFT+"manjunatha")

        time.sleep(5)



obj= ToolTip()
obj.launchBrowser()
