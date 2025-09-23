import requests
import allure
import pytest
from dotenv import load_dotenv
import os

load_dotenv('const.env')

token = os.environ.get('token')


@pytest.mark.api
@allure.title("Поиск с пустым id")
@allure.description("В запросе указываем пустой id")
def test_bez_id():
    with allure.step("Подготавливаем заголовки запроса с токеном"):
        headers = {
            "accept": "application/json",
            "X-API-KEY": token
         }
    with allure.step("Отправляем GET запрос с пустым id"):
        response = requests.get("https://api.kinopoisk.dev/v1.4/movie/id",
                                headers=headers)
    with allure.step("Проверяем код ответа 400"):
        assert response.status_code == 400


@pytest.mark.api
@allure.title("Поиск контента по ID")
@allure.description("В запросе указываем id фильма")
def test_search_film_id():
    with allure.step("Подготавливаем заголовки запроса с токеном"):
        headers = {
            "accept": "application/json",
            "X-API-KEY": token
        }
    with allure.step("Отправляем GET запрос с id фильма"):
        response = requests.get("https://api.kinopoisk.dev/v1.4/movie/1395460",
                                headers=headers)
    with allure.step("Проверяем код ответа 200"):
        assert response.status_code == 200


@pytest.mark.api
@allure.title("Поиск фильма по названию")
@allure.description("В запросе указываем название фильма в JSON объекте")
def test_search_by_name():
    with allure.step("Подготавливаем заголовки запроса с токеном"):
        headers = {
            "accept": "application/json",
            "X-API-KEY": token
         }
    with allure.step("Отправляем GET запрос с поисковым запросом"):
        response = requests.get(
         "https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query="
             "%D0%91%D0%B5%D1%81%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D0%BD%D1%8B%D0%B5",
             headers=headers)
    with allure.step("Проверяем код ответа 200"):
        assert response.status_code == 200


@pytest.mark.api
@allure.title("Получить список жанров")
@allure.description("Запрашиваем все доступные жанры в JSON объекте")
def test_by_genres():
    with allure.step("Подготавливаем заголовки запроса с токеном"):
        headers = {
            "accept": "application/json",
            "X-API-KEY": token
        }
    with allure.step("Отправляем GET запрос списка жанров"):
        response = requests.get("https://api.kinopoisk."
                          "dev/v1/movie/possible-values-by-field?field=genres.name",
                           headers=headers)
    with allure.step("Проверяем код ответа 200"):
        assert response.status_code == 200


@pytest.mark.api
@allure.title("Поиск без токена")
@allure.description("В запросе из headers убираем значение X-API-KEY")
def test_bez_tokena():
    with allure.step("Подготавливаем заголовки запроса без токена"):
        headers = {
            "accept": "application/json"
        }
    with allure.step("Отправляем GET запрос с id фильма без токена"):
        response = requests.get("https://api.kinopoisk.dev/v1.4/movie/1395460",
                                headers=headers)
    with allure.step("Проверяем код ответа 401"):
        assert response.status_code == 401
