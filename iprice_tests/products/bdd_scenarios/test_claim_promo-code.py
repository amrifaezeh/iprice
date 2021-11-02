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
import urllib.request

from selenium.webdriver.common.by import By
from seleniumbase import BaseCase
from iprice_tests.helpers.user_helper import UserHelper


class TestClaimPromoCode(BaseCase):

    def test_claim_promo_code(self):
        self.visit("https://iprice.my/")
        self.wait_for_text_visible("Find the Best Deals Online")

        best_deals_container = self.find_element('//h1[text()="Find the Best Deals Online"]/../..', By.XPATH)

        stores_list = best_deals_container.find_elements_by_css_selector('a')
        print(f"count of stores: {len(stores_list)}")

        i = 0
        while i < 3:

            i += 1
            option = random.randint(1, len(stores_list))

            # choose random form the best deals online
            bdo_selector = best_deals_container.find_element_by_css_selector(f'a:nth-child({option})')
            store_coupon_page_url = bdo_selector.get_attribute('href')
            store_title = bdo_selector.text
            print(f"visiting {store_title}")

            self.visit(store_coupon_page_url)

            # verify of correct navigation to the shop
            self.wait_for_element("header#main-menu-top")
            current_active_coupon = self.find_element('#breadcrumb-desktop').text
            assert store_title in current_active_coupon

            # click on the voucher or code
            self.wait_for_element("#store-active-coupon form a[data-vars-action=\"coupons\"]")
            self.find_element("#store-active-coupon form a[data-vars-action=\"coupons\"]").click()

            self.switch_to_window(1)
            self.wait_for_element_visible("#coupon-popup")
            selector = self.find_element(".nocode-text-cell, #code")
            class_code_or_no_code = selector.get_attribute('class')
            if class_code_or_no_code == 'nocode-text-cell':
                self.switch_to_window(0)
                continue

            # enter your email here
            random_email = UserHelper.get_random_email()
            self.find_element("#email-capture input[placeholder=\"Enter your email here\"]").send_keys(
                random_email)
            print(f"random email generated : {random_email}")

            successful_message = "Get the latest deals and coupons right in your inbox!"
            # Get the latest deals and coupons right in your inbox!
            assert self.find_element(
                "#email-capture > div > div > p").text == successful_message

            # click on sign up

            self.find_element("#coupon-popup")
            self.find_element("input[value='Sign Up']").click()

            self.wait_for_element("div[submit-success] span")
            success_message = self.find_element("div[submit-success] span")
            if success_message.is_displayed():
                print("Element Displayed")
                # verification of success message displayed
                successful_message = "Thanks for signing up, you'll be receiving coupons and deals in no time!"
                assert success_message.text == successful_message
            else:
                print("Element is not Displayed")

            # click on like Icon
            self.find_element("svg[data-vars-cgt=\"click_coupon_works_thumb_up\"]").click()

            # click on store
            store = self.find_element("#coupon-popup > div > div > div > a")

            store_url = store.get_attribute('href')
            print(store_url)

            try:
                status_code = urllib.request.urlopen(store_url).getcode()
                website_is_up = status_code == 200
                assert website_is_up
            except Exception as e:
                print(e)
                assert False

            break
