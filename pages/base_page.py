from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(("xpath", locator))
        ).click()

    def type(self, locator, value):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(("xpath", locator))
        ).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(("xpath", locator))
        ).send_keys(value)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(("xpath", locator))
        )
