from selenium import  webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class HandleTabs:

    def launchBrowser(self):
        driver = webdriver.Chrome('D:/Softwares/Drivers/Chrome/79/chromedriver_win32/chromedriver.exe')

        driver.get("https://demoqa.com/tabs/")

        driver.maximize_window()
        driver.implicitly_wait(20)
        main_window = driver.current_window_handle
        print(main_window)

        first_tab= driver.find_element_by_xpath("//li[@role='tab'][1]")
        first_tab.click()
        time.sleep(1)
        first_tab_text= driver.find_element_by_xpath("//div[@id='tabs-1']/p")
        print(first_tab_text.text)
        time.sleep(1)

        # move to Second tab
        sec_tab = driver.find_element_by_xpath("//li[@role='tab'][2]")
        #move to Second tab
        sec_tab.send_keys(Keys.CONTROL + Keys.TAB)
        #Click on second tab
        sec_tab.click()
        time.sleep(1)
        sec_tab_text = driver.find_element_by_xpath("//div[@id='tabs-2']/p")
        print(sec_tab_text.text)
        time.sleep(1)

        third_tab = driver.find_element_by_xpath("//li[@role='tab'][3]")
        third_tab.send_keys(Keys.CONTROL + Keys.TAB)
        third_tab.click()
        time.sleep(1)
        third_tab_text = driver.find_element_by_xpath("//div[@id='tabs-3']/p")
        print(third_tab_text.text)
        time.sleep(1)

        first_tab = driver.find_element_by_xpath("//li[@role='tab'][1]")
        first_tab.click()
        time.sleep(1)
        first_tab_text = driver.find_element_by_xpath("//div[@id='tabs-1']/p")
        print(first_tab_text.text)
        time.sleep(1)





ob= HandleTabs()
ob.launchBrowser()