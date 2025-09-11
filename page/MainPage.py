from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AuthPage:
    def __init__(self, driver:WebDriver) -> None:
        self.__url = "https://www.kinopoisk.ru/"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)
        WebDriverWait(self.__driver, 40).until(EC.visibility_of_element_located((By.CLASS_NAME,"kinopoisk-header-logo__img")))