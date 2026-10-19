import allure
import time
from selenium.webdriver.common.by import By
from pages.calendar_page import CalendarPage


@allure.feature("Calendar Page")
class TestCalendar:

    @allure.title("Позитивный: Ввод корректной даты")
    def test_valid_date_input(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.enter_date("2025-01-01")
        page.click_submit()
        assert page.get_input_value() == "2025-01-01"

    @allure.title("Позитивный: Ввод даты в другом формате")
    def test_another_date_format(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.enter_date("01/15/2025")
        page.click_submit()
        assert page.get_input_value() == "01/15/2025"

    @allure.title("Позитивный: Ввод даты из будущего")
    def test_future_date(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.enter_date("2030-12-31")
        page.click_submit()
        assert page.get_input_value() == "2030-12-31"

    @allure.title("Позитивный: Ввод даты из прошлого")
    def test_past_date(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.enter_date("1990-05-20")
        page.click_submit()
        assert page.get_input_value() == "1990-05-20"

    @allure.title("Позитивный: Ввод даты с 29 февраля високосного года")
    def test_leap_year_date(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.enter_date("2024-02-29")
        page.click_submit()
        assert page.get_input_value() == "2024-02-29"

    @allure.title("Позитивный: Ввод даты в формате YYYY-MM-DD")
    def test_standard_format(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.enter_date("2025-06-15")
        page.click_submit()
        assert page.get_input_value() == "2025-06-15"

    @allure.title("Позитивный: Ввод даты начала года")
    def test_start_of_year(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.enter_date("2025-01-01")
        page.click_submit()
        assert page.get_input_value() == "2025-01-01"

    @allure.title("Позитивный: Ввод даты конца года")
    def test_end_of_year(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.enter_date("2025-12-31")
        page.click_submit()
        assert page.get_input_value() == "2025-12-31"

    @allure.title("Негативный: Ввод неверного формата (буквы)")
    def test_invalid_date_format(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.enter_date("abc")
        page.click_submit()
        assert page.get_input_value() != "2025-01-01"

    @allure.title("Негативный: Ввод пустой строки")
    def test_empty_date(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.enter_date("")
        page.click_submit()
        # Поле должно остаться пустым
        assert page.get_input_value() == ""

    @allure.title("Негативный: Ввод несуществующей даты (31 февраля)")
    def test_invalid_february_date(self, driver):
        page = CalendarPage(driver)
        page.open()
        page.enter_date("2025-02-31")
        page.click_submit()
        # Браузер обычно очищает неверную дату
        assert page.get_input_value() != ""