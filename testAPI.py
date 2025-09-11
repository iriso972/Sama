import requests
import allure

token = "X7WWKYQ-JQPM4HR-JJJ1GQA-ZA6V985"  #Будет в сопроводительном письме, так как репозиторий открытый


@allure.title("Поиск с пустым id")
@allure.description("В запросе указываем пустой id")
def test_bez_id():
    headers = {
        "accept": "application/json",
        "X-API-KEY": "token"
    }
    response = requests.get("https://api.kinopoisk.dev/v1.4/movie/id",
                            headers=headers)
    assert response.status_code == 400


@allure.title("Поиск контента по ID")
@allure.description("В запросе указываем id фильма")
def test_search_film_id():
    headers = {
        "accept": "application/json",
        "X-API-KEY": "token"
    }
    response = requests.get("https://api.kinopoisk.dev/v1.4/movie/1395460", headers=headers)
    assert response.status_code == 200


@allure.title("Поиск фильма по названию")
@allure.description("В запросе указываем название фильма в JSON объекте")
def test_search_by_name():
    headers = {
        "accept": "application/json",
        "X-API-KEY": "token"
    }
    response = requests.get(
    "https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query=%D0%91%D0%B5%D1%81%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D0%BD%D1%8B%D0%B5",
        headers=headers)
    assert response.status_code == 200


@allure.title("Получить список жанров")
@allure.description("Запрашиваем все доступные жанры в JSON объекте")
def test_by_genres():
    headers = {
        "accept": "application/json",
        "X-API-KEY": "token"
    }
    response = requests.get("https://api.kinopoisk.dev/v1/movie/possible-values-by-field?field=genres.name", headers=headers)
    assert response.status_code == 200


@allure.title("Поиск без токена")
@allure.description("В запросе из headers убираем значение X-API-KEY")
def test_bez_tokena():
    headers = {
        "accept": "application/json"
            }
    response = requests.get("https://api.kinopoisk.dev/v1.4/movie/1395460", headers=headers)
    assert response.status_code == 401