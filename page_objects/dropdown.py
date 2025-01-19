from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class Dropdown(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def select_from_dropdown(self, option_text):
        self.driver.find_element(By.TAG_NAME, "select").click()
        options = self.driver.find_elements(By.XPATH, "//select/option")
        for option in options:
            if option.text == option_text:
                option.click()
                break

