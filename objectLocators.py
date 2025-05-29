from selenium.webdriver.common.by import By

class locators():
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    ADD_EMP = (By.XPATH, "//nav//ul//li[contains(., 'Add Employee')]")
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    SUBMIT_BTN = (By.XPATH,"//button[@type='submit']")
    EMP_LIST = (By.XPATH, "//nav//ul//li[contains(., 'Employee List')]")
    PROFILE_OPTIONS = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    LOGOUT_BTN = (By.XPATH, "//ul[@class='oxd-dropdown-menu']/li[contains(.,'Logout')]")
    