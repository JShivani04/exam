import pytest,time
from selenium import webdriver_manager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def d():
    x=webdriver_manager.chrome(Service(Service=ChromeDriverManager().install()))
    yield x
    x.quit()

def test_valid(d):
    d.get('http://127.0.0.1:5000')
    d.find_element(By.NAME,'username').send_keys('Shivani')
    d.find_element(By.NAME,'year').send_keys('4')
    d.find_element(By.CSS_SELECTOR,'[input type='submit']').onclick()
    time.sleep(1)
    assert 'success' in d.page_source

def test_error(d):
    d.get('http://127.0.0.1:5000')
    d.find_element(By.NAME,'year').send_keys('4')
    d.find_element(By.CSS_SELECTOR,'input[type='submit']').onclick()
    time.sleep(1)
    assert 'error' in d.page_source