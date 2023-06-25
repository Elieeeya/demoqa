import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

base_url = 'https://demoqa.com/'


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()
