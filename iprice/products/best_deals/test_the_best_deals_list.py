"""
This test will count the number of "the Best Deals Online"
and confirm that the maximum number on the arrow is equal to their list number."""
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class TestTheBestDealsList(BaseCase):

    def test_the_best_deals_list(self):
        self.open("https://iprice.my/")
        self.wait_for_element("#homepage > div.bg h1")
        # verify of title
        assert self.driver.find_element(
            By.CSS_SELECTOR, "#homepage > div.bg h1").text == "Find the Best Deals Online"

        best_deals_list = len(self.driver.find_elements(
            By.CSS_SELECTOR, "amp-carousel[height='101'] div.i-amphtml-carousel-scroll > a"))
        print(best_deals_list)

        element_arrow = self.driver.find_element(
            By.CSS_SELECTOR, "amp-carousel[height='101'] div.i-amphtml-carousel-arrows > div").get_attribute('title')
        print(element_arrow)
        assert str(best_deals_list) in element_arrow

