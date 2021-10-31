"""
This test will count the number of "top popular products"
and confirm that the maximum number on the arrow is equal to their list number."""

from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class TestTopTrendingProductsList(BaseCase):

    def test_top_trending_list(self):
        self.open("https://iprice.my/")
        self.wait_for_element("#homepage > div.bg h1")
        # verify of title
        assert self.driver.find_element(
            By.CSS_SELECTOR, "#homepage > div.C.I.l.eU > h2").text == "Top Trending Products"

        # get the number of elements
        top_trending_list = len(self.driver.find_elements(
            By.CSS_SELECTOR, "amp-carousel[height='46'] div.i-amphtml-carousel-scroll > a"))
        print(top_trending_list)

        # get the arrow attribute
        element_arrow = self.driver.find_element(
            By.CSS_SELECTOR, "amp-carousel[height='46'] div.i-amphtml-carousel-arrows > div").get_attribute('title')
        print(element_arrow)
        # verify maximum numbers in arrow == number of trending list
        assert str(top_trending_list) in element_arrow
