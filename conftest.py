from typing import Any, Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def driver() -> Generator[WebDriver, Any, None]:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver

    driver.quit()