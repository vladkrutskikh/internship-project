from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class MainPage(Page):
    LOGIN_BTN = (By.CSS_SELECTOR, ".login-button.w-button")
    LOGIN_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    SECONDARY_LISTINGS_BTN = (By.CSS_SELECTOR, "a[href='/secondary-listings']")

    def __init__(self, driver):
        super().__init__(driver)
        self.app = None

    def open(self):
        self.open_url('https://soft.reelly.io/sign-in')
        from time import sleep
        sleep(8)

    def login(self):
        self.input_text(self.LOGIN_CREDENTIALS, *self.LOGIN_FIELD)
        self.input_text(self.PASSWORD_CREDENTIALS, *self.PASSWORD_FIELD)
        self.click(*self.LOGIN_BTN)
        from time import sleep
        sleep(8)

    def click_secondary_listings(self):
        self.click(*self.SECONDARY_LISTINGS_BTN)