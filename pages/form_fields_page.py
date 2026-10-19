from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FormFieldsPage(BasePage):
    URL = "https://practice-automation.com/form-fields/"

    # Нашли точный ID поля Message
    MESSAGE_INPUT = (By.ID, "message")
    
    # XPath: находим label с текстом "Automation tools", 
    # затем идем к следующему за ним ul и берем все li внутри
    AUTOMATION_TOOLS_LIST = (By.XPATH, "//label[contains(text(), 'Automation tools')]/following-sibling::ul/li")

    def open(self):
        self.driver.get(self.URL)

    def get_automation_tools_text(self):
        elements = self.driver.find_elements(*self.AUTOMATION_TOOLS_LIST)
        tools = [el.text for el in elements if el.text.strip()]
        return ", ".join(tools)

    def fill_message(self, text):
        # Используем стандартный метод ввода, так как это textarea
        self.type(self.MESSAGE_INPUT, text)

    def get_message_value(self):
        return self.find(self.MESSAGE_INPUT).get_attribute("value")