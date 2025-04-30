from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import Page

class SecondaryPage(Page):
    expected_url_page = "https://soft.reelly.io/secondary-listings"

    def page_secondary_check(self):
        actual_url = self.driver.current_url
        assert self.expected_url_page in actual_url, f'Expected URL "soft.reelly.io/secondary-listings" is not shown'

        self.driver.find_element(By.CSS_SELECTOR, "a.menu-text-link-leaderboard.w--current")

    def wait_for_listing_update(self):
        locator = (By.CSS_SELECTOR, '.listing-card')
        old_items = self.driver.find_elements(*locator)
        old_count = len(old_items)

        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(*locator)) != old_count
        )

    def click_pagination_btn_last(self):
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

                WebDriverWait(self.driver, 10).until(
                    lambda d: d.find_element(By.CSS_SELECTOR, '[wized="currentPageProperties"]').text.strip().isdigit()
                )

                current = self.driver.find_element(By.CSS_SELECTOR, '[wized="currentPageProperties"]').text.strip()
                total = self.driver.find_element(By.CSS_SELECTOR, '[wized="totalPageProperties"]').text.strip()

                print(f"Current page: {current}, total pages: {total}")

                if current == total:
                    print("Last page is reached.")
                    break

                self.driver.find_element(By.CSS_SELECTOR, ".pagination__button.w-inline-block").click()
                self.wait_for_listing_update()

            except Exception as e:
                print(f"Error: {e}")
                break

    def click_pagination_btn_first(self):
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

                WebDriverWait(self.driver, 10).until(
                    lambda d: d.find_element(By.CSS_SELECTOR, '[wized="currentPageProperties"]').text.strip().isdigit()
                )

                current = self.driver.find_element(By.CSS_SELECTOR, '[wized="currentPageProperties"]').text.strip()
                total = self.driver.find_element(By.CSS_SELECTOR, '[wized="totalPageProperties"]').text.strip()

                print(f"Current page: {current}, total pages: {total}")

                if current == "1":
                    print("Reached the first page.")
                    break

                self.driver.find_element(By.CSS_SELECTOR, '[wized="previousPageMLS"]').click()
                self.wait_for_listing_update()

            except Exception as e:
                print(f"Error: {e}")
                break