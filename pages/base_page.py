from urllib.parse import urlparse


class BasePage(object):
    # driver object, url, implicity time in class constructor
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicity_wait(timeout)
    
    # parse the relative part of url from selenium method string (current_url)
    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path
