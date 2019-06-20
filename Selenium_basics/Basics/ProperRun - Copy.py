import time
from selenium import webdriver

#Create Class

class BasicTestObject:

    def launch_browser(self):
        # Instantiate Browser
        driver = webdriver.Chrome('D:/Softwares/Drivers/chromedriver_win32/chromedriver')
        #Open the provided URL
        driver.get("https://letskodeit.teachable.com/pages/practice")

        driver.maximize_window()

        driver.find_element_by_xpath("(//a[contains(text(),'Sign Up')])[1]").click()

        gettitle = driver.title

        print(gettitle)

        getUrl = driver.current_url
        print(getUrl)

        links_on_the_page = driver.find_elements_by_xpath("//a")
        leng = len(links_on_the_page)

        if links_on_the_page is not None:
            print("Links on the Page is Present: ")

        for x in links_on_the_page:
            print(x.text)

        print(str(leng))

        driver.quit()



ch_browser = BasicTestObject()
ch_browser.launch_browser()
