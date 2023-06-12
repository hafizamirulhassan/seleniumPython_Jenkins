import time

import pytest

from src.PageObjectModel.Config.config import TestData
from src.PageObjectModel.Pages.LoginPage import LoginPage
from src.PageObjectModel.Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_Gmail_Login(self):
        self.loginPage = LoginPage(self.driver)
        time.sleep(5)
        self.loginPage.login_Gmail(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(5)
