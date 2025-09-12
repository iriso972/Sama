import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.MainPage import AuthPage


@pytest.mark.ui
@allure.epic("Тестирование UI")
@allure.title("Авторизация с пустым полем номера телефона")
@allure.description("Пустое поле номера телефона")
def test_auth(driver):
    with allure.step("Открываем страницу авторизации"):
        auth_page = AuthPage(driver)
        auth_page.go()

    with allure.step("Нажимаем кнопку Войти"):
        driver.find_element(By.CSS_SELECTOR, ".styles_loginButton__6_QNl")\
            .click()

    with allure.step("Нажимаем кнопку подтверждения"):
        driver.find_element(By.ID, "passp:sign-in").click()

    with allure.step("Ожидаем появление сообщения об ошибке формата номера"):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                         ((By.ID, "field:input-phone:hint")))

    with allure.step("Проверяем появление сообщения об ошибке"):
        assert (driver.find_element(By.ID, "field:input-phone:hint"))\
                                        .text == "Недопустимый формат номера"
