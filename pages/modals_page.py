from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ModalsPage(BasePage):
    URL = "https://practice-automation.com/modals/"

    SIMPLE_MODAL_BUTTON = (By.ID, "simpleModal")
    FORM_MODAL_BUTTON = (By.ID, "formModal")
    MODAL_CONTAINER = (By.CLASS_NAME, "pum-container")
    CLOSE_BUTTON = (By.CLASS_NAME, "pum-close")
    SIMPLE_MODAL_TEXT = (By.XPATH, "//div[contains(@class, 'pum-content')]//p")
    BACK_BUTTON = (By.XPATH, "//a[contains(text(), 'Back')]")

    def open(self):
        self.driver.get(self.URL)

    def click_simple_modal(self):
        self.click(self.SIMPLE_MODAL_BUTTON)

    def click_form_modal(self):
        element = self.find(self.FORM_MODAL_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def close_simple_modal(self):
        self.click(self.CLOSE_BUTTON)

    def close_modal_js(self):
        try:
            close_btn = self.driver.find_element(*self.CLOSE_BUTTON)
            self.driver.execute_script("arguments[0].click();", close_btn)
        except Exception:
            pass

    def close_form_modal_js(self):
        # Находим окно с формой, а внутри него — крестик
        try:
            form_container = self.driver.find_element(By.CSS_SELECTOR, ".pum-container.pum-responsive-tiny")
            close_btn = form_container.find_element(By.CLASS_NAME, "pum-close")
            self.driver.execute_script("arguments[0].click();", close_btn)
        except Exception:
            # Если не нашли, пробуем кликнуть по любому крестику через JS
            self.close_modal_js()

    def is_modal_visible(self):
        return self.is_visible(self.MODAL_CONTAINER)

    def get_simple_modal_text(self):
        return self.find(self.SIMPLE_MODAL_TEXT).text

    def is_form_modal_visible(self):
        return self.is_visible((By.CSS_SELECTOR, ".pum-container.pum-responsive-tiny"))