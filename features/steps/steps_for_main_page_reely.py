from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given("Open main page Reely")
def open_main_page(context):
    context.driver.get('https://soft.reelly.io')

@given("Log in to the page")
def log_in(context):
    context.driver.find_element(By.ID, 'email-2').send_keys('kruts.media@gmail.com')
    context.driver.find_element(By.ID, 'field').send_keys('kruts.media')
    context.driver.find_element(By.CSS_SELECTOR, '.login-button.w-button').click()
    sleep(3)

@when("Click on the Secondary option at the left side menu")
def click_secondary_option(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/secondary-listings']").click()
    sleep(10)