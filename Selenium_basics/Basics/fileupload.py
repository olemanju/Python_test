from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class FileUpload:

    def launchBrowser(self):
        driver = webdriver.Chrome('D:/Softwares/Drivers/Chrome/79/chromedriver_win32/chromedriver.exe')

        driver.get("https://demoqa.com/keyboard-events/")

        driver.maximize_window()
        driver.implicitly_wait(20)

        file_up= driver.find_element_by_id('browseFile')
        file_up.send_keys("D:/JOBSearch/NRI.pdf")
        time.sleep(5)

        click_upload= driver.find_element_by_id('uploadButton')
        click_upload.click()

        wait=WebDriverWait(driver,30)
        wait.until(EC.alert_is_present(),'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
        alert= driver.switch_to.alert
        print(alert.text)
        alert.accept()
        print("alert accepted")
        time.sleep(5)



obh= FileUpload()
obh.launchBrowser()