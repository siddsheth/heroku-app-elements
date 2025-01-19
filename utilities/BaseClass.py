import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class BaseClass:
    def OpenPage(self, page):
        self.driver.find_element(By.LINK_TEXT, page).click()
        time.sleep(1)
        assert self.driver.find_element(By.TAG_NAME, "h3").text == page
