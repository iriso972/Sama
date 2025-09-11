#SAMA
Проект по автоматизации тестирования приложения "Кинопоиск"

Проект содержит автоматизированные тесты с использованием Selenium WebDriver, Python, Pytest, WebDriverWait.

Структура проекта

- conftest.py           # Инициализация браузера (фикстура)
- testUI.py             # UI тесты
- testAPI.ру            # API тесты
- requirements.txt      # Зависимости проекта
- README.md             # Документация
- gitignore             # Игнорируемые файлы
- Auth_test.py          # UI тест на авторизацию 
- MainPage.py           # Главная страница папки "page"

Порядок действий:
1. Клонируем репозиторий (https://github.com/iriso972/Sama.git) на локальную машину.
2. Открываем его в Pycharm.
3. Устанавливаем зависимости 'pip install -r requirements.txt'.
4. Запускаем тесты 'pytest'.
5. Cобираем данные для отчёта 'pytest --alluredir allure-result'.
6. Формируем отчёт 'allure serve allure-result'.

ВАЖНО: В начале тестового файла есть ожидания. Так как сайт может запустить capcha для проверки на
робота, проверку выполнить в ручном режиме: кликнуть чек-бокс и выполнить требуемые действия.

Стек:
pytest
selenium
requests
allure

