import time
from locators.elements_page_locators import TextBoxLocators
from pages.base_page import BasePage
# from faker import Faker


# class TextBoxPage(BasePage):
#     locators = TextBoxLocators()
    

#     def fill_all_fields(self):
#         self.element_is_visiable(self.locators.FULL_NAME).send_keys('Radiy Temirgaliev')
#         self.element_is_visiable(self.locators.EMAIL).send_keys('radiy@mail.com')
#         self.element_is_visiable(self.locators.CURRENT_ADDRESS).send_keys('Matthews, NC')
#         self.element_is_visiable(self.locators.PERMANENT_ADDRESS).send_keys('Matthews, NC')
#         time.sleep(2)
#         submit_button = self.wait_for_element_to_be_clickable(self.locators.SUBMIT)
#         self.scroll_to_element(submit_button)
#         submit_button.click()
#         time.sleep(3)
    
    # def check_filled_form(self):
    #     full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
    #     email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
    #     current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
    #     permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
    #     return full_name, email, current_address, permanent_address


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def fill_all_fields(self):
        full_name = self.wait_for_element_to_be_visible(self.locators.FULL_NAME)
        full_name.send_keys('Radiy Temirgaliev')

        email = self.wait_for_element_to_be_visible(self.locators.EMAIL)
        email.send_keys('radiy@mail.com')

        current_address = self.wait_for_element_to_be_visible(self.locators.CURRENT_ADDRESS)
        current_address.send_keys('Matthews, NC')

        permanent_address = self.wait_for_element_to_be_visible(self.locators.PERMANENT_ADDRESS)
        permanent_address.send_keys('Matthews, NC')
        time.sleep(5)
        submit_button = self.wait_for_element_to_be_clickable(self.locators.SUBMIT)
        self.scroll_to_element(submit_button)
        submit_button.click()
        time.sleep(5)
