from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class Checkboxes(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def check_checkbox(self, num):
        xpath = "//input[" + str(num) + "]"
        self.driver.find_element(By.XPATH, xpath).click()
        assert self.driver.find_element(By.XPATH, xpath).is_selected()

    def uncheck_checkbox(self, num):
        xpath = "//input[" + str(num) + "]"
        self.driver.find_element(By.XPATH, xpath).click()
        assert not self.driver.find_element(By.XPATH, xpath).is_selected()
