import time

from page_objects.dropdown import Dropdown
from utilities.BaseClass import BaseClass


class Test_Dropdown(BaseClass):
    def test_open_dropdown_page(self):
        self.OpenPage("Dropdown")

    def test_select_option(self):
        dd = Dropdown(self.driver)
        dd.select_from_dropdown("Option 1")
        time.sleep(5)
