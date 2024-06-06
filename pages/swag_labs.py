from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(loc='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def exist_field_name(self, loc):
        try:
            self.find_element(loc)
        except NoSuchElementException:
            return False
        return True
