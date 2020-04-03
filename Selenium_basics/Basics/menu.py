from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class MenuHandle:

    def launchBrowser(self):
        driver = webdriver.Chrome('D:/Softwares/Drivers/Chrome/79/chromedriver_win32/chromedriver.exe')

        driver.get("https://demoqa.com/menu/")

        driver.maximize_window()
        driver.implicitly_wait(20)

        music= driver.find_element_by_id('ui-id-9')

        action= ActionChains(driver)
        action.move_to_element(music).perform()
        rock= driver.find_element_by_id('ui-id-13')
        action.move_to_element(rock).perform()
        modem=driver.find_element_by_id('ui-id-16')
        action.move_to_element(modem).perform()
        va=modem.get_attribute("class")
        print(va)
        time.sleep(3)


obh= MenuHandle()
obh.launchBrowser()