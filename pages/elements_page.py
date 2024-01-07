import random
import time
from generator.generator import generated_person
from locators.elements_page_locators import ButtonsPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, TextBoxLocators, WebTablePageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    
    def click_random_checkbox(self):
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1,15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break
            
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()
    
    
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON, 
                  'impressive': self.locators.IMPRESSIVE_RADIOBUTTON, 
                  'no': self.locators.NO_RADIOBUTTON,}
        
        self.element_is_visible(choices[choice]).click()


    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text
    

class WebTablePage(BasePage):

    locators = WebTablePageLocators()

    def add_new_person(self):
        # count = random.randint(1,3)
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            time.sleep(5)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -=1
            return [firstname, lastname, str(age), email,  str(salary), department]
        

    def check_new_added_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data
    

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        # row = delete_button.find_element_by_xpath(self.locators.ROW_PARENT)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()
    

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)
    
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    
    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text
    

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):

    locators = ButtonsPageLocators()

    # def click_on_different_button(self, type_click):
    #     if type_click == 'double':
    #         self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
    #         return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)
    #     if type_click == 'right':
    #         self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
    #         return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)
    #     if type_click == 'click':
    #         self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
    #         return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)


    # def check_clicked_on_the_button(self, element):
    #     return self.element_is_present(element).text

    def click_double_click_button(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
        return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)
    
    def click_right_click_button(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)
    
    def click_button(self):
        self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
        return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)
    
    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text











