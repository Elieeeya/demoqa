import time

from model.pages.page_elements import ElementsPage
from model.pages.page_menu import MenuPage
from model.control.utils import FakeUser


class TestFillForm:

    def test_tex_box_form(self, driver):
        self.driver = driver
        menu_page = MenuPage(self.driver)
        elements_menu = ElementsPage(self.driver)
        menu_page.click_menu_elements()
        elements_menu.click_elements_list_text_box()
        form = ElementsPage(self.driver)
        form.filling_out_the_form(full_name=FakeUser.fake_login,
                                  email=FakeUser.fake_email,
                                  current_address=FakeUser.fake_address,
                                  permanent_address=FakeUser.fake_address
                                  )

        assert f'Name:{FakeUser.fake_login}' == f'Name:{FakeUser.fake_login}'
        assert  f'Email:{FakeUser.fake_email}' == f'Email:{FakeUser.fake_email}'
