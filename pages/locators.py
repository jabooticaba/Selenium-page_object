from selenium.webdriver.common.by import By
import sys
sys.path.insert(0, '..')

class AuthLocators:
    AUTH_EMAIL = (By.ID, "email")
    AUTH_PASS = (By.ID, "pass")
    AUTH_BTN = (By.CLASS_NAME, "btn-success")