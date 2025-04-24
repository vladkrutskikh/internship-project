from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then("Verify the right page Secondary deals opens")
def verify_page_secondary_opens(context):
    actual_url = context.driver.current_url
    expected_url_page = "https://soft.reelly.io/secondary-listings"
    assert expected_url_page in actual_url, f'Expected URL "soft.reelly.io/secondary-listings" is not shown'

    context.driver.find_element(By.CSS_SELECTOR, "a.menu-text-link-leaderboard.w--current")


@when("Go to the final page using the pagination button")
def click_pagination_btn_last(context):
    while True:
        try:
            context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            sleep(1)

            current = context.driver.find_element(By.CSS_SELECTOR, '[wized="currentPageProperties"]').text.strip()
            total = context.driver.find_element(By.CSS_SELECTOR, '[wized="totalPageProperties"]').text.strip()

            if not (current.isdigit() and total.isdigit()):
                print("Waiting for digits...")
                sleep(1)
                continue

            print(f"Current page: {current}, total pages: {total}")

            if current == total:
                print("Last page is reached.")
                break

            button = context.driver.find_element(By.CSS_SELECTOR, ".pagination__button.w-inline-block")
            button.click()

            sleep(4)
        except Exception as e:
            print(f"Error: {e}")
            break

    sleep(3)

@when("Go back to the first page using the pagination button")
def click_pagination_btn_first(context):
    while True:
        try:
            context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            sleep(1)

            current = context.driver.find_element(By.CSS_SELECTOR, '[wized="currentPageProperties"]').text.strip()
            total = context.driver.find_element(By.CSS_SELECTOR, '[wized="totalPageProperties"]').text.strip()

            if not (current.isdigit() and total.isdigit()):
                print("Waiting for digits...")
                sleep(1)
                continue

            print(f"Current page: {current}, total pages: {total}")

            if current == "1":
                print("Reached the first page.")
                break

            button = context.driver.find_element(By.CSS_SELECTOR, '[wized="previousPageMLS"]')
            button.click()

            sleep(4)
        except Exception as e:
            print(f"Error: {e}")
            break

    sleep(3)
