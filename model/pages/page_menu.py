import time

from selenium.webdriver.common.by import By
from model.locators.locators import MenuForm, ElenetsMenu
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(self.driver, 3)

    def click_menu_elements(self):
        el = self.driver.find_element(*MenuForm.menu_elements)
        self.driver.execute_script('arguments[0].scrollIntoView();', el)
        self.driver.find_element(*MenuForm.menu_elements).click()

    def click_menu_form(self):
        el = self.driver.find_element(*MenuForm.menu_form)
        self.driver.execute_script('arguments[0].scrollIntoView();', el)
        self.driver.find_element(*MenuForm.menu_form).click()

    def click_menu_alerts(self):
        el = self.driver.find_element(*MenuForm.menu_alerts)
        self.driver.execute_script('arguments[0].scrollIntoView();', el)
        self.driver.find_element(*MenuForm.menu_alerts).click()

    def click_menu_widget(self):
        el = self.driver.find_element(*MenuForm.menu_widget)
        self.driver.execute_script('arguments[0].scrollIntoView();', el)
        self.driver.find_element(*MenuForm.menu_widget).click()

    def click_menu_interactions(self):
        el = self.driver.find_element(*MenuForm.menu_interactions)
        self.driver.execute_script('arguments[0].scrollIntoView();', el)
        self.driver.find_element(*MenuForm.menu_interactions).click()

    def click_menu_books_store_application(self):
        el = self.driver.find_element(*MenuForm.menu_books_store_application)
        self.driver.execute_script('arguments[0].scrollIntoView();', el)
        self.driver.find_element(*MenuForm.menu_books_store_application).click()


    def type_back_menu(self):
        self.driver.back()