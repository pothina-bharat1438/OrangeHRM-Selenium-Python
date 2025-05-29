from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from objectLocators import locators


class OrangeHRMLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def login(self, url, username, password):
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located(locators.USERNAME)).send_keys(username)
        self.wait.until(EC.presence_of_element_located(locators.PASSWORD)).send_keys(password)
        self.wait.until(EC.presence_of_element_located(locators.LOGIN_BTN)).click()
        print("Successfully Logged in:", self.driver.current_url)
        time.sleep(2)

    def navigateToMOdule(self,module):
        self.driver.find_element(By.XPATH, f"//li[contains(., '{module}')]").click()

    def addEmployee(self,employee_list):
        for emp in employee_list:
            self.wait.until(EC.presence_of_element_located(locators.ADD_EMP)).click()
            self.wait.until(EC.presence_of_element_located(locators.FIRST_NAME)).send_keys(emp['firstName'])
            self.wait.until(EC.presence_of_element_located(locators.LAST_NAME)).send_keys(emp['lastName'])
            self.wait.until(EC.presence_of_element_located(locators.SUBMIT_BTN)).click()
            time.sleep(10)

        self.wait.until(EC.presence_of_element_located(locators.EMP_LIST)).click()

        for emp in employee_list:
            firstNameElement = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div/div[@class='oxd-table-card']/div/div[contains(., '{emp['firstName']}')]/div")))
            lastNameElement = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div/div[@class='oxd-table-card']/div/div[contains(., '{emp['firstName']}')]/following-sibling::div[contains(., '{emp['lastName']}')]/div")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", firstNameElement)
            actualFirstName = firstNameElement.text
            actualLastName = lastNameElement.text
            assert actualFirstName == emp['firstName'] and actualLastName == emp['lastName'], f"Expected {emp['firstName']}' '{emp['lastName']} but got '{actualFirstName}{actualLastName}'"
            print(actualFirstName, actualLastName,"--Name Verified--")

    def logout(self):
        self.wait.until(EC.presence_of_element_located(locators.PROFILE_OPTIONS)).click()
        self.wait.until(EC.presence_of_element_located(locators.LOGOUT_BTN)).click()

    def close(self):
        self.driver.close()



