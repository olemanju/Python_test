from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class DowonAllinOne:

    def launchBrowser(self):
        driver = webdriver.Chrome('D:/Softwares/Drivers/Chrome/79/chromedriver_win32/chromedriver.exe')

        driver.get("https://demoqa.com/automation-practice-form/")

        driver.maximize_window()
        driver.implicitly_wait(20)

        text_con1= driver.find_element_by_xpath("//div/em/strong");
        print(text_con1.text)

        par_link= driver.find_element_by_link_text("Partial Link Test")
        if par_link.is_displayed():
            par_link.click()

        time.sleep(4)

        newpage_text= driver.find_element_by_xpath("//h1")
        print(newpage_text.text)
        time.sleep(2)
        driver.back()
        time.sleep(4)

        first_name = driver.find_element_by_name("firstname")
        first_name.send_keys(Keys.SHIFT+"manjunatha")

        last_name = driver.find_element_by_id('lastname')
        last_name.send_keys("achintya")

        sex_selection = driver.find_elements_by_xpath("//input[@name='sex']")
        print(len(sex_selection))

        for i in sex_selection:
            if not i.is_selected():
                i.click()
                print(i.get_attribute("value"))
                print("Radio Selected")
                break

        date_pic = driver.find_element_by_id("datepicker")
        driver.execute_script("arguments[0].scrollIntoView();",date_pic)
        #driver.execute_script("arguments[0].scrollIntoView();", h2head)
        prof = driver.find_elements_by_xpath("//input[@name='profession']")
        print(len(prof))

        for i in prof:
            if not i.is_selected():
                i.click()
                print(i.get_attribute("value"))

        time.sleep(4)

        file_up = driver.find_element_by_id('photo')
        file_up.send_keys("D:\\JOBSearch\\NRI.pdf")
        time.sleep(4)
        print("Doc Updated")

        tool_check = driver.find_elements_by_xpath("//input[@name='tool']")

        for i in tool_check:
            if not i.is_selected():
                i.click()
        print("Tool Check box is selected")


        content_drop = driver.find_element_by_id("continents");
        driver.execute_script("arguments[0].scrollIntoView();", content_drop)

        vart="Australia"
        drp = Select(content_drop)
       # print(drp.options)
        #for option in drp.find_elements_by_tag_name('option'):
        for opt in drp.options:
            drp.select_by_visible_text(vart)
            break
        print("Dropdown Selected")

        time.sleep(5)

        mul_seelct = driver.find_element_by_id('continentsmultiple')
        drp_sel = Select(mul_seelct)
        #print(drp_sel.options)
        """
        mul_se = driver.find_element_by_xpath("//select[@id='continentsmultiple']/option")
        dr_sel_mul= Select(mul_se)
        print(mul_se)

        action = ActionChains(driver)
        action.click_and_hold(drp_sel.select_by_visible_text("Europe")).perform()

        time.sleep(2)
        """
        time.sleep(3)














obh= DowonAllinOne()
obh.launchBrowser()