import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    # service_obj = Service("C:/Users/Siddharth/Documents/Sid/Selenium/drivers/Chrome-120/chromedriver.exe")
    # driver = webdriver.Chrome(service=service_obj)

    driver = webdriver.Chrome()
    url = "https://the-internet.herokuapp.com/"
    driver.get(url)
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.close()
