from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Page:
    LOGIN_CREDENTIALS = ('kruts.media@gmail.com')
    PASSWORD_CREDENTIALS = ('kruts.media')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        print(f"Trying to click: {locator}")
        element = self.driver.find_element(*locator)
        print(f"Element found: {element.tag_name}, {element.text}")
        element.click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def get_current_window(self):
        window = self.driver.current_window_handle
        print('Current window: ', window)
        return window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        windows = self.driver.window_handles
        print(f'All windows: {windows}')
        self.driver.switch_to.window(windows[1])
        print(f'Switched to new window => {windows[1]}')

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print(f'Switched to new window => {window_id}')

    def verify_partial_url(self, expected_partial_url):
        current_url = self.driver.current_url
        assert expected_partial_url in current_url, \
            f"Expected '{expected_partial_url}' in '{current_url}'"

    def close(self):
        self.driver.close()
        sleep(1)

    def wait_for_url_change(self, old_url):
        self.wait.until(lambda driver: driver.current_url != old_url)

    def verify_text(self):
         pass

    def verify_partial_text(self):
        pass