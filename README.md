# Efective Mobile
Тестовое задание по автоматизации тестирования главной страницы effective-mobile.ru

### Шаги
1. Склонировать проект 'git clone https://github.com/krivoiplintus/Effective_Mobile.git'
2. Установить зависимости 'pip install -r requirements.txt'
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'
6. Собрать контейнер 'docker build -t my-test .'
7. Запустить контейнер 'docker run  my-test'

### Стек:
- pytest
- selenium
- allure
- docker

### Струткура:
- ./test - тесты
- ./pages - описание страниц
- ./configyration - провайдер настроек
  - test_config.ini - настройки для тестов
- ./test_data - провайдер тестовых данных
  - test_data.json - тестовые данные

### Полезные ссылки
- [base_url](https://www.effective-mobile.ru/)