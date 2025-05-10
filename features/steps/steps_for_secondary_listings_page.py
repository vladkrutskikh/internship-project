from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then("Verify the right page Secondary deals opens")
def verify_page_secondary_opens(context):
    context.app.secondary_listings_page.page_secondary_check()

@when("Go to the final page using the pagination button")
def clicking_pagination_arrow_till_the_end(context):
    context.app.secondary_listings_page.click_pagination_btn_last()

@when("For MOB go to the final page using the pagination button")
def clicking_pagination_arrow_till_the_end_mob(context):
    context.app.secondary_listings_page.click_pagination_btn_last_mob()

@when("Go back to the first page using the pagination button")
def click_pagination_btn_first(context):
    context.app.secondary_listings_page.click_pagination_btn_first()

@when("For MOB go back to the first page using the pagination button")
def click_pagination_btn_first_mob(context):
    context.app.secondary_listings_page.click_pagination_btn_first_mob()



