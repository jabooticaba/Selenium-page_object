from .base_page import BasePage
from .locators import AuthLocators

import time, os

class AuthPage(BasePage):
    
    def __init__(self, driver, timeout=10):
      super().init(driver, timeout)
      url = os.getenv("LOGIN_URL") or "http://petfriends1.herokuapp.com/login"
      driver.get(url)
      self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
      self.passw = driver.find_element(*AuthLocators.AUTH_PASS)
      self.btn = driver.find_element(*AuthLocators.AUTH_BTN)