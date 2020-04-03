from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class WindowHandle:

    def launchBrowser(self):
        driver = webdriver.Chrome('D:/Softwares/Drivers/Chrome/79/chromedriver_win32/chromedriver.exe')

        driver.get("https://demoqa.com/automation-practice-switch-windows/")

        driver.maximize_window()
        driver.implicitly_wait(20)

        parent= driver.current_window_handle

        print(parent)
        va= driver.title
        print(va)
        new_brw_window = driver.find_element_by_id('button1')
        new_brw_window.click()

        time.sleep(4)

        mul=driver.window_handles
        print(mul)
        si=len(mul)
        print("Page title before Switching : " + driver.title)
        print("Total Windows : " + str(si))

        for i in range(si):
            if mul[i] != parent:
                driver.switch_to.window(mul[i])
                print(driver.title)
                driver.maximize_window()
                wait= WebDriverWait(driver,30)
                get_emali= driver.find_element_by_xpath("//span[@class='mini-contacts email show-on-desktop in-top-bar-left in-menu-second-switch last']")
                print(get_emali.text)
                driver.close()

        time.sleep(4)
        driver.switch_to.window(parent)
        driver.refresh()
        time.sleep(2)
        print(driver.title)

        print("Second TC Started")
        nw_br_tab= driver.find_element_by_xpath("//button[text()='New Browser Tab']")
        if nw_br_tab.is_displayed():
            nw_br_tab.click()

        mul_windows= driver.window_handles
        print(len(mul_windows))
        x=len(mul_windows)

        for i in range(x):
            if mul_windows[i] !=parent:

                driver.switch_to.window(mul_windows[i])
                print("New tab")
                print(driver.title)
                time.sleep(6)
                get_mob= driver.find_element_by_xpath("//span[@class='mini-contacts phone show-on-desktop in-top-bar-left in-menu-second-switch']")
                print(get_mob.text)
                driver.close()

        driver.switch_to.window(parent)
        print(driver.title)


        #sec_tab.send_keys(Keys.CONTROL + Keys.TAB)





        time.sleep(4)
        driver.quit()


obh= WindowHandle()
obh.launchBrowser()