import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ui
@allure.title("Поиск фильма по названию")
@allure.description("Поиск, переход на страницу, выбор фильма")
def test_search(driver):
    with allure.step("Открываем главную страницу"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("Вводим название фильма в поле поиска"):
        search_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable
                                                       ((By.NAME, "kp_query")))
        search_input.send_keys("Медиатор")
    with allure.step("Выбираем фильм из подсказок"):
        item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable
                                               ((By.ID, "suggest-item-tvSeries-1395460")))
        item.click()
    with allure.step("Проверяем, что открылась правильная страница фильма"):
        film_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located
                                            ((By.CSS_SELECTOR, "span[data-tid='2da92aed']")))
        assert film_title.text == "Медиатор"


@pytest.mark.ui
@allure.title("Поиск фильма с использованием неподдерживаемого языка")
@allure.description("Ввод в поле поиска иероглифов")
def test_negative(driver):
    with allure.step("Открываем главную страницу"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("Вводим иероглифы в поле поиска"):
        input_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable
                                                      ((By.NAME, "kp_query")))
        input_field.send_keys("人で座ってください")
    with allure.step("Проверяем, что отображается сообщение о пустом результате"):
        empty_suggest = WebDriverWait(driver, 10).until(EC.visibility_of_element_located
                                        ((By.XPATH, "//*[contains(@class, 'emptySuggest')]")))
        assert empty_suggest.text == "По вашему запросу ничего не найдено"


@pytest.mark.ui
@allure.title("Поиск фильма с незаполненным названием")
@allure.description("Пустое поле поиска")
def test_search_empty(driver):
    with allure.step("Открываем главную страницу"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("Оставляем поле поиска пустым и нажимаем на кнопку Найти"):
        search_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable
                                                       ((By.NAME, "kp_query")))
        search_input.send_keys("")
        search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable
                                        ((By.CSS_SELECTOR, "button[type='submit'][aria-label='Найти']")))
        search_button.click()
    with allure.step("Проверяем, что загрузилась страница поиска"):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))


@pytest.mark.ui
@allure.title("Поиск фильма по актеру")
@allure.description("Ввод в поле поиска имени актера, переход на его страницу")
def test_actors(driver):
    with allure.step("Открываем главную страницу"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("Вводим имя актера в поле поиска"):
        search_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable
                                                       ((By.NAME, "kp_query")))
        search_input.send_keys("Брэд Питт")
    with allure.step("Выбираем актера из подсказок"):
        actor_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable
                                                     ((By.ID, "suggest-item-person-25584")))
        actor_item.click()
    with allure.step("Проверяем, что открылась правильная страница актера"):
        actor_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located
                                                     ((By.CSS_SELECTOR, "h1[data-tid='f22e0093']")))
        assert actor_name.text == "Брэд Питт"
