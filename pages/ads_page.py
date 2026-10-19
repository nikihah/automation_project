from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdsPage(BasePage):
    URL = "https://practice-automation.com/ads/"

    AD_IFRAME = (By.ID, "aswift_0")
    AD_CLOSE_BUTTON = (By.ID, "dismiss-button")
    AD_BANNER = (By.CLASS_NAME, "adsbygoogle")
    MAIN_CONTENT = (By.TAG_NAME, "body")

    def open(self):
        self.driver.get(self.URL)

    def is_ad_present(self):
        try:
            self.find(self.AD_BANNER)
            return True
        except Exception:
            return False

    def switch_to_ad_iframe(self):
        iframe = self.find(self.AD_IFRAME)
        self.driver.switch_to.frame(iframe)

    def close_ad(self):
        self.click(self.AD_CLOSE_BUTTON)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def is_main_content_visible(self):
        return self.find(self.MAIN_CONTENT).is_displayed()