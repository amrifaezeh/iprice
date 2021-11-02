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
        self.wait_for_text_visible("Top Stores")

        # get the number of top stores
        top_store_list = len(self.find_elements("section[data-uat=\"top-stores\"] > div"))
        print(top_store_list)

        # get the urls
        for i in range(1, top_store_list):
            # get all urls
            urls = self.find_element(
                f"#coupon-overview section[data-uat=\"top-stores\"] > div:nth-child({i ++1}) > a"
            ).get_attribute('href')
            print(f"{urls}")
            # 2.a make sure all url of stores in "Top Stores" are all active

            status_code = urllib.request.urlopen(urls).getcode()
            website_is_up = status_code == 200

            print(website_is_up)
            if website_is_up:
                print("URL activated")
            else:
                print(f"URL {self.urls} is not active")
                return False

            # 2.b Make sure that list of stores in "Top Stores" is redirected to their proper store url

            self.open(f"{urls}")
            browser_url = self.get_current_url()
            assert urls == browser_url
            self.driver.back()
