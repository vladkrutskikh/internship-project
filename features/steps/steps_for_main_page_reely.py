from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given("Open main page Reely")
def open_main_page(context):
    context.app.main_page.open()

@given("Log in to the page")
def log_in(context):
    context.app.main_page.login()

@when("Click on the Secondary option at the left side menu")
def click_secondary_option(context):
    context.app.main_page.click_secondary_listings()