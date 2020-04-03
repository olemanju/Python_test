from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckBoxClass:

    def launchBrowser(self):
        driver = webdriver.Chrome('D:/Softwares/Drivers/Chrome/79/chromedriver_win32/chromedriver.exe')

        driver.get("https://demoqa.com/checkboxradio/")

        driver.maximize_window()
        driver.implicitly_wait(20)

        # Radio Button
        lenofRadio= driver.find_elements_by_xpath("//Legend[1]/following::label[@for[contains(.,'radio')]]")
        print(len(lenofRadio))

        for i in lenofRadio:
            if not i.is_selected():
                i.click()
                print("Radio Clicked")
                time.sleep(3)
                break

        time.sleep(1)

        # Multiple Check boxes

        mul_chkbox= driver.find_elements_by_xpath("//Legend[contains(.,'Hotel Ratings: ')]/following::label[position()<=4]")
        print(len(mul_chkbox))


        for i in mul_chkbox:

            if not i.is_selected():
                i.click()
                print("Check Box Checked ")

        time.sleep(1)

        bed_chkbox = driver.find_elements_by_xpath(
            "//Legend[contains(.,'Hotel Ratings: ')]/following::label[position()>=5]")

        h2head = driver.find_element_by_xpath("//h2[position() >=3]")

        driver.execute_script("arguments[0].scrollIntoView();", h2head)

        # driver.execute_script("return arguments[0].scrollIntoView();",h2head)
        time.sleep(1)
        for i in bed_chkbox:

            if not i.is_selected():
                i.click()
                print("Bed Check Box Checked ")

        time.sleep(2)
        driver.quit()

obj  = CheckBoxClass()
obj.launchBrowser()