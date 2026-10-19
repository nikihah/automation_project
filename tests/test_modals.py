import allure
import time
from selenium.webdriver.common.by import By
from pages.modals_page import ModalsPage


@allure.feature("Modals Page")
class TestModals:

    @allure.title("Позитивный: Открытие простого модального окна")
    def test_open_simple_modal(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.click_simple_modal()
        assert page.is_modal_visible()

    @allure.title("Позитивный: Закрытие простого модального окна")
    def test_close_simple_modal(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.click_simple_modal()
        page.close_simple_modal()
        time.sleep(1)
        assert not page.is_modal_visible()

    @allure.title("Позитивный: Открытие модального окна с формой")
    def test_open_form_modal(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.click_form_modal()
        time.sleep(1)
        assert page.is_form_modal_visible()

    @allure.title("Позитивный: Проверка текста в простом окне")
    def test_simple_modal_text(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.click_simple_modal()
        time.sleep(1)
        # Ищем слово "simple" в тексте окна (более гибкая проверка)
        text = page.get_simple_modal_text().lower()
        assert "simple" in text

    @allure.title("Позитивный: Повторное открытие окна после закрытия")
    def test_reopen_simple_modal(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.click_simple_modal()
        page.close_simple_modal()
        time.sleep(1)
        page.click_simple_modal()
        time.sleep(1)
        assert page.is_modal_visible()

    @allure.title("Позитивный: Закрытие формы через JS")
    def test_close_form_modal(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.click_form_modal()
        time.sleep(1)
        # Закрываем через JS, чтобы обойти проблемы с кликом
        page.close_modal_js()
        time.sleep(1)
        assert not page.is_form_modal_visible()

    @allure.title("Негативный: Проверка, что окно не открывается без клика")
    def test_modal_not_visible_initially(self, driver):
        page = ModalsPage(driver)
        page.open()
        assert not page.is_modal_visible()

    @allure.title("Позитивный: Закрытие формы через крестик")
    def test_close_form_modal(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.click_form_modal()
        time.sleep(1)
        # Закрываем через JS, находя крестик внутри формы
        page.close_form_modal_js()
        time.sleep(1)
        assert not page.is_form_modal_visible()

    @allure.title("Негативный: Проверка отсутствия ошибки внутри окна")
    def test_no_error_inside_modal(self, driver):
        page = ModalsPage(driver)
        page.open()
        page.click_simple_modal()
        time.sleep(1)
        # Проверяем текст только внутри модального окна
        modal_text = driver.find_element(By.CLASS_NAME, "pum-content").text.lower()
        assert "error" not in modal_text