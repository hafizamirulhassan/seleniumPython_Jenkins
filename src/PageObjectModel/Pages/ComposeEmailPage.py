import time

from selenium.webdriver.common.by import By
from src.PageObjectModel.Config.config import TestData
from src.PageObjectModel.Pages.CommonPage import CommonPage


class ComposeEmailPage(CommonPage):
    LOGO_GMAIL = (By.XPATH, "(//a[contains(@aria-label, 'Gmail')])[2]")
    TITLE_INBOX = (By.XPATH, "//a[contains(@aria-label,  'Inbox')]")

    def __init__(self, driver):
        super().__init__(driver)

    # def get_inbox_home_page_title(self, title):
    #     return self.get_Title(title)

    def verify_LogoGmail_Icon_Exist(self):
        return self.isElement_visible(self.LOGO_GMAIL)

    def get_Inbox_Title_Value(self, title):
        if self.get_element_text(self.TITLE_INBOX):
            return self.get_element_text(self.TITLE_INBOX)
