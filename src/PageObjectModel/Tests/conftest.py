import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from src.PageObjectModel.Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def initialization_driver(request):
    global web_driver
    browser = request.param

    if browser == "chrome":
        chrome_options = Options()
        service = Service(TestData.CHROME_EXECUTABLE_PATH)
        web_driver = webdriver.Chrome(service=service, options=chrome_options)

    request.cls.driver = web_driver
    web_driver.implicitly_wait(20)

    yield
    web_driver.quit()
