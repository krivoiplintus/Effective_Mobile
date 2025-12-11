import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from page.main_page import MainPage


@allure.title("Переход на страницу с вакансиями")
def test_сurrent_vacancies_click(browser: WebDriver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(browser)
    main_page.сurrent_vacanciesic_click()
    title_new_page = main_page.list_vacancies_open()
    with allure.step("Проверить, что title открывшейся страници соответствует ожидаемому"):
        assert title_new_page == "Вакансии"


@allure.title("Переход по кнопке Оставить заявку")
def test_leave_request_click(browser: WebDriver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(browser)
    main_page.leave_request_click()
    clickable_element = main_page.send_an_application_vis()
    with allure.step("Проверить, что кнопка Отправить заявку видна"):
        assert clickable_element is not None


@allure.title("Переход по кнопке Узнать больше")
def test_find_out_more_click(browser: WebDriver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(browser)
    main_page.find_out_more_click()
    clickable_element = main_page.card_vis()
    with allure.step("Проверить, что карточки с вариантами сотрудничества видны"):
        assert clickable_element is not None
