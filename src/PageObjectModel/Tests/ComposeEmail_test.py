import time

import pytest

from src.PageObjectModel.Config.config import TestData
from src.PageObjectModel.Logs.logFile import logClass
from src.PageObjectModel.Pages.LoginPage import LoginPage
from src.PageObjectModel.Tests.test_base import BaseTest


class Test_ComposeEmail(BaseTest, logClass):

    # def test_gmailLogin_title(self):
    #     self.loginPage = LoginPage(self.driver)
    #     composeEmailPage = self.loginPage.login_Gmail(TestData.USER_NAME, TestData.PASSWORD)
    #     time.sleep(30)
    #     title = composeEmailPage.get_inbox_home_page_title(TestData.COMPOSE_EMAIL_PAGE_TITLE)
    #     time.sleep(20)
    #     assert title == TestData.COMPOSE_EMAIL_PAGE_TITLE
    #     time.sleep(20)

    def test_gmail_inboxName_title(self):

        self.loginPage = LoginPage(self.driver)
        composeEmailPage = self.loginPage.login_Gmail(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(5)
        inboxValue = composeEmailPage.get_Inbox_Title_Value(TestData.COMPOSE_EMAIL_PAGE_INBOX_TITLE_VALUE)
        time.sleep(5)
        assert inboxValue == TestData.COMPOSE_EMAIL_PAGE_INBOX_TITLE_VALUE

    def test_gmail_logo(self):
        self.loginPage = LoginPage(self.driver)
        composeEmailPage = self.loginPage.login_Gmail(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(5)
        assert composeEmailPage.verify_LogoGmail_Icon_Exist()
