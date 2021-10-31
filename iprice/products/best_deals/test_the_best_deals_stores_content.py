"""
This test case will count the number of "the best deals online" from the list
Then it will get all the attributes "alt" from the list
Then it will get the content of each card
then it will verify of attributes "alt" is same name as each card name.
"""
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class TestTheBestDealsStoresContent(BaseCase):

    def test_list_of_store_content(self):
        self.open("https://iprice.my/")
        self.wait_for_element("#homepage > div.bg h1")
        # verify of title
        assert self.driver.find_element(
            By.CSS_SELECTOR, "#homepage > div.bg h1").text == "Find the Best Deals Online"

        # get number of best deals
        list_no = len(self.driver.find_elements(
            By.CSS_SELECTOR, "div.bg amp-carousel[height='101'] div.i-amphtml-carousel-scroll > a"))
        print(list_no)

        # print all the stores name
        for i in range(list_no):
            # get all the stores by name
            stores = self.driver.find_element(
                By.CSS_SELECTOR,
                f"amp-carousel[height='101'] div.i-amphtml-carousel-scroll > a:nth-child({i ++1})"
            ).get_attribute('href').replace("https://iprice.my/coupons/", "")[:-1]
            print(stores)

            stores_alt_attr = self.driver.find_element(
                By.CSS_SELECTOR,
                f"amp-carousel[height='101'] div.i-amphtml-carousel-scroll > a:nth-child({i ++1}) > amp-img"
            ).get_attribute('alt')
            print(stores_alt_attr)
            # get the div content
            stores_content = self.driver.find_element(
                By.CSS_SELECTOR,
                f"amp-carousel[height='101'] div.i-amphtml-carousel-scroll > a:nth-child({i ++1}) > div"
            ).text
            print(stores_content)
            # verify of all stores name in the url
            assert stores_alt_attr in stores_content


