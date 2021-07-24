import sys
sys.path.insert(0, '..')
from pages.auth_page import AuthPage
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.headless = False
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def test_auth_page():
  driver = webdriver.Chrome(options=chrome_options)
  page = AuthPage(driver)
  time.sleep(3)
  page.enter_email("test123@yandex.ru")
  page.enter_pass("123456")
  page.btn_click()

  assert page.get_relative_link() == "/all_pets", "login error"

  time.sleep(3)