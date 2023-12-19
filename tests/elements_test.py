
from time import sleep
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.elements_page import TextBoxPage

class TestElements:

    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            # time.sleep(5)
            text_box_page.fill_all_fields()
            
            # text_box_page.check_filled_form()

#             output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

# class TestElements:
#     class TestTextBox:

#         def test_text_box(self, driver):
#             text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
#             text_box_page.open()
#             text_box_page.fill_all_fields('Greg', 'griloz@gmail.com', 'Charlotte', 'NC')
#             sleep(4)


            
             

            

