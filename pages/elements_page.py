import time
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxLocators
from pages.base_page import BasePage
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
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.wait_for_element_to_be_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.wait_for_element_to_be_visible(self.locators.EMAIL).send_keys(email)
        self.wait_for_element_to_be_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.wait_for_element_to_be_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        submit_button = self.wait_for_element_to_be_clickable(self.locators.SUBMIT)
        self.scroll_to_element(submit_button)
        submit_button.click()
        return full_name, email, current_address, permanent_address


    def check_filled_form(self):
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1].strip()
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1].strip()
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1].strip().replace('\n', ' ')
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1].strip().replace('\n', ' ')
        return full_name, email, current_address, permanent_address
