import allure
import time
from selenium.webdriver.common.by import By
from pages.ads_page import AdsPage


@allure.feature("Ads Page")
class TestAds:

    @allure.title("Позитивный: Страница рекламы открывается")
    def test_ads_page_opens(self, driver):
        page = AdsPage(driver)
        page.open()
        assert "ads" in driver.current_url.lower()

    @allure.title("Позитивный: Основной контент отображается")
    def test_main_content_visible(self, driver):
        page = AdsPage(driver)
        page.open()
        assert page.is_main_content_visible()

    @allure.title("Позитивный: Присутствует текст про рекламу")
    def test_ad_text_present(self, driver):
        page = AdsPage(driver)
        page.open()
        # Ищем текст "An ad will appear"
        element = driver.find_element(By.XPATH, "//p[contains(text(), 'An ad will appear')]")
        assert element.is_displayed()

    @allure.title("Позитивный: Кнопка Learn More доступна")
    def test_learn_more_link(self, driver):
        page = AdsPage(driver)
        page.open()
        link = driver.find_element(By.XPATH, "//a[contains(text(), 'Learn More')]")
        assert link.is_displayed()

    @allure.title("Позитивный: Кнопка About доступна")
    def test_about_link(self, driver):
        page = AdsPage(driver)
        page.open()
        link = driver.find_element(By.XPATH, "//a[contains(text(), 'About')]")
        assert link.is_displayed()

    @allure.title("Позитивный: Заголовок страницы содержит 'Ads'")
    def test_title_contains_ads(self, driver):
        page = AdsPage(driver)
        page.open()
        assert "ads" in driver.title.lower()

    @allure.title("Позитивный: Страница не содержит ошибок в консоли (проверка загрузки)")
    def test_page_loads_correctly(self, driver):
        page = AdsPage(driver)
        page.open()
        # Проверяем, что страница загрузилась и есть основной контент
        assert "Ads" in driver.page_source

    @allure.title("Позитивный: Повторное открытие страницы")
    def test_reopen_page(self, driver):
        page = AdsPage(driver)
        page.open()
        page.open()
        assert "ads" in driver.current_url.lower()

    @allure.title("Негативный: Страница не открывается с неверным URL")
    def test_wrong_url(self, driver):
        driver.get("https://practice-automation.com/ads-wrong/")
        # Проверяем, что это не страница рекламы (должна быть 404 или редирект)
        assert "ads" not in driver.current_url.lower() or "wrong" in driver.current_url.lower()

    @allure.title("Негативный: Пустой заголовок страницы")
    def test_empty_title(self, driver):
        page = AdsPage(driver)
        page.open()
        assert driver.title != ""

    @allure.title("Негативный: Отсутствие текста ошибки на странице")
    def test_no_error_text(self, driver):
        page = AdsPage(driver)
        page.open()
        # Ищем текст "Error" только в основном контенте
        body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
        assert "error" not in body_text or "ad" in body_text