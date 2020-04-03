from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Refresh_Selenium:


    def launchBrowser(self):
        driver = webdriver.Chrome('D:/Softwares/Drivers/Chrome/79/chromedriver_win32/chromedriver.exe')

        driver.get("https://demoqa.com/keyboard-events-sample-form/")

        driver.maximize_window()
        driver.implicitly_wait(20)


        heading= driver.find_element_by_class_name('entry-title')
        if heading.is_displayed():
            print("heading is displayed")
            print(heading.text)

        driver.find_element_by_id('userName').send_keys("Banana")
        driver.find_element_by_id('currentAddress').send_keys("Keyboard Events Sample Form")
        driver.find_element_by_id('permanentAddress').send_keys("King kong")
        driver.find_element_by_id('submit').click()
        #time.sleep(5)

        WebDriverWait(driver,30).until(EC.alert_is_present(),'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')


        alert= driver.switch_to.alert
        val= alert.text
        print(val)
        time.sleep(2)
        alert.accept()
        print("Clicked on Alert box")

        driver.quit()

obj= Refresh_Selenium()
obj.launchBrowser()
