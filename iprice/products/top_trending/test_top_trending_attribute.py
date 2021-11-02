"""
This test will Count the number of "Top Trending"
And it will find the attribute by name "data-vars-cgt"
Then it will verify attribute "data-vars-cgt" is exist in the list
"""
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class TestTopTrendingProductsListAttribute(BaseCase):

    def test_top_trending_list_attribute(self):
        self.open("https://iprice.my/")
        self.wait_for_element("#homepage > div.bg h1")
        assert self.find_element("#homepage > div.C.I.l.eU > h2").text == "Top Trending Products"

        top_trending_list = len(self.find_elements(
            "div.C.I.l.eU amp-carousel[height='46'] div.i-amphtml-carousel-scroll > a"))
        print(top_trending_list)

        for i in range(top_trending_list):
            element = self.find_element(
                f"div.C.I.l.eU amp-carousel[height='46'] div.i-amphtml-carousel-scroll > a:nth-child({i ++1})")
            attrs = self.driver.execute_script(
                'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) '
                '{ items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
                element)
            print(attrs)
            assert 'data-vars-cgt' in attrs
            if 'data-vars-cgt' in attrs:
                print(f"in element {i} attribute data-vars-cgt Exist")
            else:
                print(f"in element {i} attribute data-vars-cgt is not Exist")
                return False
