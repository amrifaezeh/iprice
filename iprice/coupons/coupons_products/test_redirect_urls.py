"""
This test case will count the number of list form "Top Store"
Then it will get all the urls from the list
Then it will open all the urls and verify if the url in browser is same as href on the list
"""
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class TestURLSRedirect(BaseCase):

    def test_url_Redirect(self):
        self.open("https://iprice.my/coupons/")
        self.wait_for_element("#coupon-overview header > h2")
        # verify of title
        assert self.find_element("#coupon-overview header > h2").text == "Top Stores"
        # get the number of top stores
        top_store_list = len(self.find_elements("section[data-uat=\"top-stores\"] > div"))
        print(top_store_list)

        # get the urls
        for i in range(1, top_store_list):
            # get all urls
            urls = self.find_element(
                f"#coupon-overview div.mu.lD section[data-uat=\"top-stores\"] > div:nth-child({i ++1}) > a"
            ).get_attribute('href')
            print(f"{urls}")
            self.open(f"{urls}")

            browser_url = self.get_current_url()
            assert urls == browser_url
            self.driver.back()
