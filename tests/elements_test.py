
from time import sleep
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.elements_page import TextBoxPage

class TestElements:

    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            # text_box_page.fill_all_fields()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()

            assert input_data == output_data


