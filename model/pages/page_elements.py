from selenium.webdriver.common.by import By
from model.locators.locators import ElementsForm, ElenetsMenu
from selenium.webdriver.support.wait import WebDriverWait as wait


class ElementsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(self.driver, 3)

    def click_elements_list_text_box(self):
        self.driver.find_element(*ElenetsMenu.text_box).click()

    def filling_out_the_form(self, full_name, email, permanent_address, current_address):
        self.driver.find_element(*ElementsForm.full_name).send_keys(full_name)
        self.driver.find_element(*ElementsForm.email).send_keys(email)
        self.driver.find_element(*ElementsForm.current_address).send_keys(current_address)
        self.driver.find_element(*ElementsForm.permanent_address).send_keys(permanent_address)
        el = self.driver.find_element(*ElementsForm.button_submit)
        self.driver.execute_script('arguments[0].scrollIntoView();', el)
        self.driver.find_element(*ElementsForm.button_submit).click()

    def cheking_info_text_form_table_name(self):
        self.driver.find_element(*ElementsForm.table_name).text()

    def cheking_info_text_form_table_email(self):
        self.driver.find_element(*ElementsForm.table_email).text()
