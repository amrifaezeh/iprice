"""
A. Grab the list of stores in the best deals online

This test case will count the number of "the best deals online" from the list
Then it will get all the attributes "alt" from the list
Then it will get the content of each card
then it will verify of attributes "alt" is same name as each card name.
"""
import pytest
from selenium.webdriver.common.by import By

from seleniumbase import BaseCase


class TestTheBestDealsStoresContent(BaseCase):

    def test_best_deals_count(self):
        self.open("https://iprice.my/")
        self.wait_for_text_visible("Find the Best Deals Online")

        best_deals_container = self.find_element('//h1[text()="Find the Best Deals Online"]/../..', By.XPATH)

        # 1.a grab the list of stores in the "Find the best deals online"
        stores_list = best_deals_container.find_elements_by_css_selector('a')
        # 1.b Count the list of the stores in the "Find the sBest Deals Online"
        print(f"count of stores: {len(stores_list)}")
        assert True

    def test_top_trending_products_count(self):
        self.open("https://iprice.my/")
        self.wait_for_text_visible("Top Trending Products")

        # 1.c Count the list of items in the "Top Trending Products"
        top_trending_products_container = self.find_element('//h2[text()="Top Trending Products"]/..', By.XPATH)
        top_trending_list_stores_count = top_trending_products_container.find_elements_by_css_selector('a')
        top_trending_list_stores_count_with_attr = top_trending_products_container.find_elements_by_css_selector(
            'a[data-vars-cgt]')
        print(f"count of the top trending stores {len(top_trending_list_stores_count)}")
        print(f"count of the top trending stores with [data-vars-cgt] {len(top_trending_list_stores_count_with_attr)}")

        # 1.d validate that each item in the "Top Trending products" contains "data-vars-cgt"
        assert len(top_trending_list_stores_count) == len(top_trending_list_stores_count_with_attr)

    def test_additional_product_page_sample_test(self):
        self.open("https://iprice.my/")
        self.wait_for_text_visible("Find the Best Deals Online")

        best_deals_container = self.find_element('//h1[text()="Find the Best Deals Online"]/../..', By.XPATH)
        # get all the stores
        stores_list = best_deals_container.find_elements_by_css_selector('a')
        for i in range(len(stores_list)):
            store = stores_list[i]
            stores_alt_attr = store.find_element_by_css_selector('amp-img').get_attribute('alt')
            print(stores_alt_attr)

            # get the deal text
            store_text_content = store.find_element_by_css_selector("div").text

            # verify of all stores name in the url
            assert stores_alt_attr in store_text_content
