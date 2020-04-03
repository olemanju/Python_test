from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class HandleFrame:

    def launchBrowser(self):
        driver = webdriver.Chrome('D:/Softwares/Drivers/Chrome/79/chromedriver_win32/chromedriver.exe')

        driver.get("https://demoqa.com/iframe-practice-page/")

        driver.maximize_window()
        driver.implicitly_wait(20)

        head_text= driver.find_element_by_xpath("//div[@class='demo-frame']/h2")
        print(head_text.text)

        seq = driver.find_elements_by_tag_name('iframe')

        print("No of frames present in the web page are: ", len(seq))
        #time.sleep(2)
        driver.execute_script("window.scrollTo(0, 200)")
        frame1 = driver.find_element_by_id("IF1")

        driver.switch_to.frame(frame1)
        print("inside Frame1")
        time.sleep(2)
        ln = driver.find_element_by_link_text("Skip to content")
        ln.click()
        #phone_text = driver.find_element_by_class_name("mini-contacts phone show-on-desktop in-top-bar-left in-menu-second-switch")
        #print(phone_text.text)

        maven_t= driver.find_element_by_xpath("(//span[text()='Maven'])[2]")

        driver.execute_script("arguments[0].scrollIntoView;", maven_t)
        print(maven_t.get_attribute("class"))
        time.sleep(2)

        driver.switch_to.default_content()
        print("default page")
        ran_t= driver.find_element_by_xpath("//div[@class='demo-frame']/p")
        print(ran_t.text)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 1000)")
        frame2 = driver.find_element_by_name("iframe2")
        driver.execute_script("arguments[0].scrollIntoView;", frame2)
        time.sleep(2)
        driver.switch_to.frame(frame2)
        driver.execute_script("window.scrollTo(0, 400)")
        print("New Frame")
        time.sleep(2)
        link_tx= driver.find_element_by_link_text("Droppable")
        print(link_tx.get_attribute("href"))

        drp= driver.find_element_by_link_text("Tooltip")

        driver.execute_script("arguments[0].scrollIntoView;", drp)

        #time.sleep(4)


        time.sleep(4)




obh= HandleFrame()
obh.launchBrowser()