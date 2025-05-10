from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page
from time import sleep

class SecondaryPage(Page):
    expected_url_page = "https://soft.reelly.io/secondary-listings"
    LISTING_ITEM = (By.CSS_SELECTOR, ".properties-pagination")
    CURRENT_PAGE_NUMBER = (By.CSS_SELECTOR, "[wized='currentPageProperties']")
    TOTAL_PAGES_NUMBER = (By.CSS_SELECTOR, "[wized='totalPageProperties']")


    def page_secondary_check(self):
        self.wait_until(EC.url_contains("soft.reelly.io/secondary-listings"))
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

                WebDriverWait(self.driver, 10).until(
                    lambda d: d.find_element(By.CSS_SELECTOR, '[wized="currentPageProperties"]').text.strip() != current
                )

            except Exception as e:
                print(f"Error: {e}")
                assert False, f"Pagination to last page failed with error: {e}"

        assert current == total, f"Did not reach last page. Current: {current}, Expected: {total}"

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

                WebDriverWait(self.driver, 10).until(
                    lambda d: d.find_element(By.CSS_SELECTOR, '[wized="currentPageProperties"]').text.strip() != current
                )

            except Exception as e:
                print(f"Error: {e}")
                assert False, f"Pagination to first page failed with error: {e}"

        assert current == "1", f"Did not reach first page. Current: {current}, Expected: 1"

    def scroll_to_load_all_items_in_view(self):
        """
        Скроллит вниз страницы и ждет загрузки новых элементов списка
        до тех пор, пока количество элементов не перестанет увеличиваться.
        """
        last_count = -1
        scroll_attempts_without_new_items = 0
        max_scroll_attempts_without_new_items = 5  # Максимальное количество попыток скролла без появления новых элементов
        scroll_timeout_per_attempt = 10  # Таймаут ожидания появления новых элементов после скролла

        print("Starting scroll loop to load all items...")

        while True:
            # Скроллим в самый низ, чтобы инициировать загрузку
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Можно добавить небольшую паузу, чтобы дать странице начать загрузку
            # sleep(1)

            try:
                # Ждем, пока количество элементов увеличится
                # Используем WebDriverWait для ожидания изменения состояния
                WebDriverWait(self.driver, scroll_timeout_per_attempt).until(
                    lambda d: len(d.find_elements(*self.LISTING_ITEM)) > last_count
                )
                # Если новые элементы появились
                current_items = self.find_elements(*self.LISTING_ITEM)  # Находим элементы снова
                current_count = len(current_items)
                print(f"New items loaded. Total items found: {current_count}")
                last_count = current_count  # Обновляем счетчик
                scroll_attempts_without_new_items = 0  # Сбрасываем счетчик попыток без загрузки

            except:  # Если таймаут ожидания новых элементов истек (новых элементов не появилось)
                current_items = self.find_elements(*self.LISTING_ITEM)  # Получаем текущее количество в последний раз
                current_count = len(current_items)
                print(f"No new items loaded within timeout after scrolling. Current total items: {current_count}")

                scroll_attempts_without_new_items += 1
                if scroll_attempts_without_new_items >= max_scroll_attempts_without_new_items:
                    print(
                        f"Reached max scroll attempts ({max_scroll_attempts_without_new_items}) without new items loading. Assuming end of list view.")
                    break  # Выходим из цикла скролла, считая, что все загружено

                print(f"Scroll attempt {scroll_attempts_without_new_items}. Trying again...")

        print("Finished scroll loop.")
        # После завершения скролла, убедимся, что элементы пагинации (номер страницы) готовы
        print("Waiting for page number element after scroll loop...")
        self.wait_until(EC.visibility_of_element_located(self.CURRENT_PAGE_NUMBER))
        self.wait_until(lambda d: d.find_element(*self.CURRENT_PAGE_NUMBER).text.strip().isdigit())
        print("Page number element is ready.")

    def click_pagination_btn_last_mob(self):
        pagination_next_btn_locator = (By.CSS_SELECTOR, ".pagination__button.w-inline-block")
        page_number_locator = (By.CSS_SELECTOR, '[wized="currentPageProperties"]')
        total_pages_locator = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')
        while True:
            try:
                self.wait_until(
                    lambda d: d.find_element(*page_number_locator).text.strip().isdigit()
                )
                current = self.find_element(*page_number_locator).text.strip()
                total = self.find_element(*total_pages_locator).text.strip()

                print(f"Current page: {current}, total pages: {total}")

                if current == total:
                    print("Last page reached successfully.")
                    break

                next_button = self.find_element(*pagination_next_btn_locator)

                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)

                sleep(0.5)

                if not self.is_element_in_viewport(next_button):
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
                    sleep(0.3)

                self.wait_until(EC.element_to_be_clickable(pagination_next_btn_locator))

                next_button = self.find_element(*pagination_next_btn_locator)

                self.driver.execute_script("arguments[0].click();", next_button)

                self.wait_until(
                    lambda d: self.find_element(*page_number_locator).text.strip() != current
                )

            except Exception as e:
                assert False, f"Pagination failed with message: {e}"

        final_current_page = self.find_element(*page_number_locator).text.strip()
        final_total_pages = self.find_element(*total_pages_locator).text.strip()
        assert final_current_page == final_total_pages, f"Не достигнута последняя страница. Текущая: {final_current_page}, Ожидаемая: {final_total_pages}"
        print("Pagination to last page succeeded.")

    def is_element_in_viewport(self, element):
        """Checking if an element is visible"""
        return self.driver.execute_script("""
            var rect = arguments[0].getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        """, element)

    def click_pagination_btn_first_mob(self):
        pagination_prev_btn_locator = (By.CSS_SELECTOR, '[wized="previousPageMLS"]')
        page_number_locator = (By.CSS_SELECTOR, '[wized="currentPageProperties"]')
        total_pages_locator = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')

        while True:
            try:
                self.wait_until(
                    lambda d: d.find_element(*page_number_locator).text.strip().isdigit()
                )

                current = self.find_element(*page_number_locator).text.strip()
                total = self.find_element(*total_pages_locator).text.strip()

                print(f"Current page: {current}, total pages: {total}")

                if current == "1":
                    print("First page reached successfully.")
                    break

                prev_button = self.find_element(*pagination_prev_btn_locator)

                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", prev_button)

                sleep(0.5)

                if not self.is_element_in_viewport(prev_button):
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", prev_button)
                    sleep(0.3)

                self.wait_until(EC.element_to_be_clickable(pagination_prev_btn_locator))

                prev_button = self.find_element(*pagination_prev_btn_locator)

                self.driver.execute_script("arguments[0].click();", prev_button)

                self.wait_until(
                    lambda d: self.find_element(*page_number_locator).text.strip() != current
                )

            except Exception as e:
                assert False, f"Error during pagination to first page with message: {e}"

        final_current_page = self.find_element(*page_number_locator).text.strip()
        assert final_current_page == "1", f"Did not reach first page. Current: {final_current_page}, Expected: 1"