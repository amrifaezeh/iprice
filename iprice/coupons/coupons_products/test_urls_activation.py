"""
This test case will count the number of list form "Top Store"
Then it will get all the urls from the list
Then it will return all urls are active with status code 200
"""
import urllib.request

from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class TestURLSActivate(BaseCase):
    urls = []
    top_store_list = None

    def test_urls_from_top_store_are_activate(self):
        self.open("https://iprice.my/coupons/")
        self.wait_for_element("#coupon-overview header > h2")
        # verify of title
        assert self.driver.find_element(
            By.CSS_SELECTOR, "#coupon-overview header > h2").text == "Top Stores"
        # get the number of top stores
        self.top_store_list = len(self.driver.find_elements(By.CSS_SELECTOR, "section[data-uat=\"top-stores\"] > div"))
        print(self.top_store_list)

        # get the urls
        for i in range(1, self.top_store_list):
            # get all urls
            self.urls = self.driver.find_element(
                By.CSS_SELECTOR,
                f"#coupon-overview div.mu.lD section[data-uat=\"top-stores\"] > div:nth-child({i ++1}) > a"
            ).get_attribute('href')
            print(f"{self.urls}")

            status_code = urllib.request.urlopen(self.urls).getcode()
            website_is_up = status_code == 200

            print(website_is_up)
            if website_is_up:
                print("URL activated")
            else:
                print(f"URL {self.urls} is not active")
                return False
