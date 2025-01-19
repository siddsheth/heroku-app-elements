from page_objects.checkboxes import Checkboxes
from utilities.BaseClass import BaseClass


class Test_Checkbox(BaseClass):
    def test_open_Checkbox_page(self):
        self.OpenPage("Checkboxes")

    def test_check_checkbox1(self):
        ch = Checkboxes(self.driver)
        ch.check_checkbox(1)

    def test_uncheck_checkbox2(self):
        ch = Checkboxes(self.driver)
        ch.uncheck_checkbox(2)
