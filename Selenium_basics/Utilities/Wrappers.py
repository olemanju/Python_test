from  selenium.webdriver.common.by import By

class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver


    def getByType(self, locatorType):

        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return  By.CSS_SELECTOR
        elif locatorType == "classname":
            return  By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("locator Type " + locatorType + " Not Correct/Supported")
        return False

    def getElement(self,locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element Not Found")
        return element


    def isElementpresent(self,locator, byType):
        try:
            element = self.driver.find_element(byType,locator)
            if element is not None:
                print("Element Found")
                return  True
            else:
                return  False
        except:
            print("Element Not found")
            return  False


    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)

            if len(elementList) > 0:
                print("Element found")
                return True
            else:
                return False
        except:
            print("Element Not Found")
            return False
