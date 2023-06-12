import time

from selenium.webdriver.common.by import By

from src.PageObjectModel.Config.config import TestData
from src.PageObjectModel.Pages.CommonPage import CommonPage
from src.PageObjectModel.Pages.ComposeEmailPage import ComposeEmailPage


class LoginPage(CommonPage):
    USER_EMAIL = (By.ID, "identifierId")
    NEXT_BUTTON1 = (By.ID, "identifierNext")
    PASSWORD = (By.XPATH, "//input[@name='Passwd']")
    NEXT_BUTTON2 = (By.ID, "passwordNext")

    def __init__(self, driver):
        super().__init__(driver)
        driver.maximize_window()
        driver.delete_all_cookies()
        time.sleep()
        self.driver.get(TestData.BASE_URL)

    def login_Gmail(self, email, password):
        self.sendKeys_input(self.USER_EMAIL, email)
        self.click_btn(self.NEXT_BUTTON1)
        time.sleep(5)
        self.sendKeys_input(self.PASSWORD, password)
        self.click_btn(self.NEXT_BUTTON2)
        time.sleep(20)
        return ComposeEmailPage(self.driver)
