
from time import sleep
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.elements_page import CheckBoxPage, TextBoxPage

class TestElements:

    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            # text_box_page.fill_all_fields()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()

            assert input_data == output_data


    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)

            assert input_checkbox == output_result
            
