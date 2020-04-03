from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Dropdown:

    def launchBrowser(self):
        driver = webdriver.Chrome('D:/Softwares/Drivers/Chrome/79/chromedriver_win32/chromedriver.exe')

        driver.get("https://demoqa.com/selectmenu/")
        driver.maximize_window()
        driver.implicitly_wait(20)

        ss= driver.find_element_by_id('speed-button')
        ss.click()
        time.sleep(1)
        speed_drop= driver.find_element_by_id('speed')

        time.sleep(1)

        sel_speed= Select(speed_drop)
        sel_speed.select_by_index(1)
        time.sleep(2)

oj= Dropdown()
oj.launchBrowser()
