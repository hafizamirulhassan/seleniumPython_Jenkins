import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from src.PageObjectModel.Config.config import TestData


@pytest.fixture(params=["chrome", "edge"], scope='class')
def initialization_driver(request):
    global web_driver
    browser = request.param

    if browser == "chrome":
        # chrome_options = Options()
        # # chrome_options.add_argument("--headless")
        # service = Service(TestData.CHROME_EXECUTABLE_PATH)
        # web_driver = webdriver.Chrome(service=service, options=chrome_options)

        options = webdriver.ChromeOptions()
        web_driver = webdriver.Remote(
            command_executor="http://192.168.10.3:4444/wd/hub",
            options=options
        )

    # if browser == "firefox":
    #     # firefox_options = webdriver.FirefoxOptions()
    #     #  # firefox_options.add_argument("--headless")
    #     # service = Service(TestData.FIREFOX_EXECUTABLE_PATH)
    #     # web_driver = webdriver.Firefox(service=service, options=firefox_options)
    #
    #     options = FirefoxOptions()
    #     web_driver = webdriver.Remote(
    #         command_executor="http://192.168.10.3:4444/wd/hub",
    #         options=options
    #     )

    if browser == "edge":
        # edge_options = webdriver.EdgeOptions()
        # # firefox_options.add_argument("--headless")
        # service = Service(TestData.EDGE_EXECUTABLE_PATH)
        # web_driver = webdriver.Edge(service=service, options=edge_options)

        options = EdgeOptions()
        driver = webdriver.Remote(
            command_executor="http://192.168.10.3:4444/wd/hub",
            options=options
        )

    request.cls.driver = web_driver
    web_driver.implicitly_wait(20)

    yield
    web_driver.quit()
