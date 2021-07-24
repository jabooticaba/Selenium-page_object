from urllib.parse import urlparse
import sys
sys.path.insert(0, '..')

class BasePage(object):
    # driver object, url, implicity time in class constructor
    def __init__(self, driver):
        self.driver = driver
    
    # parse the relative part of url from selenium method string (current_url)
    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path
