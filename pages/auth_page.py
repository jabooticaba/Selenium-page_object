from .base_page import BasePage
from .locators import AuthLocators
import sys
sys.path.insert(0, '..')
import time, os

class AuthPage(BasePage):
    
    def __init__(self, driver):
      super().__init__(driver)
      url = "http://petfriends1.herokuapp.com/login"
      driver.get(url)
      self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
      self.passw = driver.find_element(*AuthLocators.AUTH_PASS)
      self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
      time.sleep(3)
    
    def enter_email(self, value):
      self.email.send_keys(value)

    def enter_pass(self, value):
      self.passw.send_keys(value)

    def btn_click(self):
      self.btn.click()