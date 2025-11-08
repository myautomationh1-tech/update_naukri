from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        el = self.wait.until(EC.element_to_be_clickable((by, locator)))
        el.click()
        return el

    def type(self, by, locator, text, clear_first=True):
        el = self.wait.until(EC.visibility_of_element_located((by, locator)))
        if clear_first:
            el.clear()
        el.send_keys(text)
        return el

    def is_visible(self, by, locator):
        try:
            self.wait.until(EC.visibility_of_element_located((by, locator)))
            return True
        except:
            return False

    def get_text(self, by, locator):
        return self.find(by, locator).text

    def open_url(self, url):
        self.driver.get(url)

    def upload_file(self, by, locator, filepath):
        el = self.find(by, locator)
        el.send_keys(os.path.abspath(filepath))

    def take_screenshot(self, fname):
        dirpath = os.path.dirname(fname)
        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)
        self.driver.save_screenshot(fname)
