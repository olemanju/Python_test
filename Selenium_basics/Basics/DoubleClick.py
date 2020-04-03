from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.action_chains import ActionChains


class Doubleclick:


    def launchBrowser(self):
        driver = webdriver.Chrome('D:/Softwares/Drivers/Chrome/79/chromedriver_win32/chromedriver.exe')

        driver.get("https://demoqa.com/tooltip-and-double-click/")

        driver.maximize_window()
        driver.implicitly_wait(20)

        action = ActionChains(driver)

        mse_over= driver.find_element_by_id('tooltipDemo')
        action.move_to_element(mse_over).perform()
        s=mse_over.get_attribute('class')
        print(s)
        time.sleep(3)

        con_click = driver.find_element_by_id('rightClickBtn')
        action.context_click(con_click).perform()
        fav = driver.find_element_by_xpath('//div[@id="rightclickItem"]/div[4]')
        c=fav.get_attribute("onclick")
        print(c)
        fav.click()


        dub_button= driver.find_element_by_id('doubleClickBtn')


        action.double_click(dub_button).perform()
        time.sleep(1)

        alert= driver.switch_to.alert
        v= alert.text
        print(v)
        alert.accept()
        time.sleep(2)

        driver.refresh()

        time.sleep(2)





obj= Doubleclick()
obj.launchBrowser()
