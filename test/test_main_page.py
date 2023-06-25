from model.pages.page_menu import MenuPage


class TestMainPage:
    def test_click_element(self, driver):
        self.driver = driver
        menu_page = MenuPage(self.driver)
        menu_page.click_menu_elements()
        menu_page.type_back_menu()

    def test_click_form(self, driver):
        self.driver = driver
        menu_page = MenuPage(self.driver)
        menu_page.click_menu_form()
        menu_page.type_back_menu()

    def test_click_alerts(self, driver):
        self.driver = driver
        menu_page = MenuPage(self.driver)
        menu_page.click_menu_alerts()
        menu_page.type_back_menu()

    def test_click_widget(self, driver):
        self.driver = driver
        menu_page = MenuPage(self.driver)
        menu_page.click_menu_widget()
        menu_page.type_back_menu()

    def test_click_interactions(self, driver):
        self.driver = driver
        menu_page = MenuPage(self.driver)
        menu_page.click_menu_interactions()
        menu_page.type_back_menu()

    def test_click_books_store_application(self, driver):
        self.driver = driver
        menu_page = MenuPage(self.driver)
        menu_page.click_menu_books_store_application()
        menu_page.type_back_menu()
