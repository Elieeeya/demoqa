import time
from conftest import base_url
from selenium.webdriver.support.wait import WebDriverWait as wait
from model.locators.locators import ElementsForm, ElenetsMenu, CheckBox
from model.control.utils import *


class CheckBoxPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(self.driver, 3)

    def checking_clicks_on_plus_icons_success(self):
        self.driver.find_element(*CheckBox.button_plus).click()

    def checking_clicks_on_minus_icons_success(self):
        self.driver.find_element(*CheckBox.button_minus).click()

    def put_a_checkbox_on_the_pack_house_success(self):
        self.driver.find_element(*CheckBox.click_home).click()
        text_home = self.driver.find_element(*CheckBox.text_home_folder).text()
        assert 'home' in text_home

    def remove_the_active_checkbox_from_the_home_folder(self):
        self.driver.find_element(*CheckBox.click_home).click()
        self.driver.get_attribute(*CheckBox.click_home)

