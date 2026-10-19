import allure
from pages.form_fields_page import FormFieldsPage


@allure.feature("Form Fields Page")
class TestFormFields:

    @allure.title("Заполнение поля Message списком Automation Tools")
    def test_fill_message_with_tools(self, driver):
        page = FormFieldsPage(driver)
        page.open()
        
        # 1. Получаем список инструментов в виде строки через запятую
        tools_text = page.get_automation_tools_text()
        
        # 2. Заполняем поле Message этим текстом
        page.fill_message(tools_text)
        
        # 3. Проверяем, что в поле оказался именно тот текст
        actual_value = page.get_message_value()
        assert actual_value == tools_text
        
        # Дополнительно прикрепляем текст в Allure для наглядности
        allure.attach(tools_text, name="Вставленный текст", attachment_type=allure.attachment_type.TEXT)