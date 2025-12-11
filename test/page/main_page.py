import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configyration.config_provider import ConfigProvider


class MainPage():
    def __init__(self, driver: WebDriver) -> None:
        self.__url = ConfigProvider().get_ui_url_main_page()
        self.__driver = driver
        self.__driver.get(self.__url)
        self.__driver.fullscreen_window()

    @allure.step("Кликнуть по кнопке Актуальные вакансии")
    def сurrent_vacanciesic_click(self):
        parent_handle = self.__driver.current_window_handle
        self.__driver.find_element(By.CSS_SELECTOR, 'a[href="https://ai-hunt.ru/vacancies/"]').click()
        self.__driver.implicitly_wait(3)
        for handle in self.__driver.window_handles:
            if handle != parent_handle:
                self.__driver.switch_to.window(handle)
                break

    @allure.step("Проверить, что открылась страница со списком вакансий ")
    def list_vacancies_open(self) -> None:
        WebDriverWait(self.__driver, 10).until(EC.url_to_be("https://ai-hunt.ru/vacancies/"))
        title = self.__driver.title
        return title

    @allure.step("Кликнуть по кнопке Оставить заявку")
    def leave_request_click(self) -> None:
        self.__driver.find_elements(By.CSS_SELECTOR, 'button[data-slot="button"]')[0].click()
        self.__driver.implicitly_wait(3)

    @allure.step("Проверить видимость кнопки Отправить заявку")
    def send_an_application_vis(self) -> None:
        wait = WebDriverWait(self.__driver, 10)
        clickable_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        return clickable_element

    @allure.step("Кликнуть по кнопке Узнать больше")
    def find_out_more_click(self) -> None:
        self.__driver.find_elements(By.CSS_SELECTOR, 'button[data-slot="button"]')[1].click()

    @allure.step("Проверить видимость карточек с вариантами сотрудничества")
    def card_vis(self) -> None:
        wait = WebDriverWait(self.__driver, 10)
        clickable_element = wait.until(
            EC.visibility_of_any_elements_located((By.CSS_SELECTOR, 'div[data-slot="card"]'))
        )
        return clickable_element
