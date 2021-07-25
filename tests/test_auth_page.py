import sys
sys.path.insert(0, '..')
from pages.auth_page import AuthPage
import time

def test_auth_page(selenium):
  page = AuthPage(selenium)
  time.sleep(3)
  page.enter_email("test123@yandex.ru")
  page.enter_pass("123456")
  page.btn_click()

  assert page.get_relative_link() == "/all_pets", "login error"

  time.sleep(3)