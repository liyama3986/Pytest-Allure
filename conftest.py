import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from allure_commons.types import AttachmentType
import allure


@pytest.fixture(scope="function")
def browser():
    # 使用WebDriver Manager自动管理浏览器驱动
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # 无头模式，不显示浏览器
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        browser = item.funcargs.get('browser')
        if browser is not None:
            allure.attach(
                browser.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=AttachmentType.PNG
            )