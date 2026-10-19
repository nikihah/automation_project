from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CalendarPage(BasePage):
    URL = "https://practice-automation.com/calendars/"

    DATE_INPUT = (By.NAME, "g1065-1-selectorenteradate")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Submit')]")

    def open(self):
        self.driver.get(self.URL)

    def enter_date(self, date_text):
        element = self.find(self.DATE_INPUT)
        self.driver.execute_script(f"arguments[0].value = '{date_text}';", element)

    def click_submit(self):
        element = self.find(self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def get_input_value(self):
        return self.find(self.DATE_INPUT).get_attribute("value")