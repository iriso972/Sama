import allure
from selenium.webdriver.common.by import By

@allure.epic("Тестирование UI")
@allure.title("Поиск фильма по названию")
@allure.description("Поиск, переход на страницу, выбор фильма")
def test_search(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("Медиатор")
    driver.find_element(By.ID, "suggest-item-tvSeries-1395460").click()
    assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='2da92aed']").text == "Медиатор"

@allure.epic("Тестирование UI")
@allure.title("Поиск фильма с использованием неподдерживаемого языка")
@allure.description("Ввод в поле поиска иероглифов")
def test_negative(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("人で座ってください")
    assert driver.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"

@allure.epic("Тестирование UI")
@allure.title("Поиск фильма с незаполненным названием")
@allure.description("Пустое поле поиска")
def test_search_english(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit'][aria-label='Найти']").click()
    assert driver.find_element(By.ID, "search")

@allure.epic("Тестирование UI")
@allure.title("Поиск фильма по актеру")
@allure.description("Ввод в поле поиска имени актера, переход на страницу актёра для выбора фильма с его участием ")
def test_actors(driver):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.NAME, "kp_query").send_keys("Брэд Питт")
    driver.find_element(By.ID, "suggest-item-person-25584").click()
    assert driver.find_element(By.CSS_SELECTOR, "h1[data-tid='f22e0093']").text == "Брэд Питт"




