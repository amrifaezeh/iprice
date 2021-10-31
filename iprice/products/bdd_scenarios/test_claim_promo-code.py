"""
Feature: BDD implementation

Scenario: Navigate to iPrice , randomly choose one of the best Deals and claim promo code or voucher

Given User choose one of the beast deals
And navigating to Coupons Page
And User choose a Coupon
When User copy the coupon and sign in with Email
Then User is successfully navigated to the store
"""

import random

from selenium.webdriver.common.by import By
from seleniumbase import BaseCase
from iprice.page_object.page_objects import SeleniumBases


class TestClaimPromoCode(BaseCase):
    random_email = SeleniumBases.get_random_email()

    def test_claim_promo_code(self):
        self.open("https://iprice.my/")
        self.wait_for_element("#homepage > div.bg h1")

        best_deals_list_numbers = len(self.driver.find_elements(
            By.CSS_SELECTOR, "#homepage div.l.eU amp-carousel[height='101'] div.i-amphtml-carousel-scroll > a"))
        print(best_deals_list_numbers)

        option = random.randint(1, best_deals_list_numbers)
        print(option)
        # choose random form the best deals online
        BDO_selector = self.driver.find_element(
            By.CSS_SELECTOR,
            f"#homepage div.l.eU amp-carousel[height='101'] div.i-amphtml-carousel-scroll > a:nth-child({option})")

        BDO_value = BDO_selector.get_attribute('href')
        print(BDO_value)
        arrow = self.driver.find_element(
            By.CSS_SELECTOR,
            "div.l.eU amp-carousel[height='101'] div.i-amphtml-carousel-arrows > div.amp-carousel-button-next"
        )
        if option in range(1, 8):
            BDO_selector.click()

        if option in range(9, 16):
            # click on arrow next
            arrow.click()
            self.wait(1)
            self.wait_for_element(
                f"#homepage div.l.eU amp-carousel[height='101'] div.i-amphtml-carousel-scroll > a:nth-child({option})")
            BDO_selector.click()
        if option in range(16, best_deals_list_numbers):
            # click on arrow next
            arrow.click()
            self.wait(1)
            arrow.click()
            self.wait(1)
            BDO_selector.click()
        # verify of correct navigation to the shop
        self.wait_for_element("header#main-menu-top")
        browser_url = self.driver.current_url
        assert BDO_value == browser_url

        # click on the voucher or code
        self.wait_for_element("#store-active-coupon form a[data-vars-action=\"coupons\"]")
        self.driver.find_element(By.CSS_SELECTOR, "#store-active-coupon form a[data-vars-action=\"coupons\"]").click()
        self.wait(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        # grab the code from pop up
        self.wait_for_element_visible("#code")
        voucher_value = self.driver.find_element(By.ID, "code").text
        print(voucher_value)

        # enter your email here
        self.driver.find_element(
            By.CSS_SELECTOR, "#email-capture input[placeholder=\"Enter your email here\"]").send_keys(self.random_email)
        print(self.random_email)

        # Get the latest deals and coupons right in your inbox!
        assert self.driver.find_element(
            By.CSS_SELECTOR,
            "#email-capture > div > div > p").text == "Get the latest deals and coupons right in your inbox!"

        # click on like Icone
        self.driver.find_element(By.CSS_SELECTOR, "svg[data-vars-cgt=\"click_coupon_works_thumb_up\"]").click()

        # click on sign up
        self.driver.find_element(By.CSS_SELECTOR, "#email-capture input[value=\"Sign Up\"]").click()
        self.wait(1)
        success_message = self.driver.find_element(By.CSS_SELECTOR, "div[submit-success] span")
        if success_message.is_displayed():
            print("Element Displayed")
            # verification of success message displayed
            assert success_message.text == "Thanks for signing up, you'll be receiving coupons and deals in no time!"
        else:
            print("Element is not Displayed")

        # click on store
        store = self.driver.find_element(
            By.CSS_SELECTOR, "#coupon-popup > div.fz.g2.h-100vh-xs > div.d7 > div.qd.dn.cO > a")

        store_url = store.get_attribute('href')
        print(store_url)
        store.click()
