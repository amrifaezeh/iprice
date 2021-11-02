# iPrice selenium test 
this is an assessment project that I did for iPrice

## Requirements

I made a test case which use BDD format (Given, When, Then, And)
Scenario: Navigate to iPrice ,
randomly choose one of the best Deals and claim promo code or voucher if it has promo code
, else go back to the iPrice page and choose another deal from the list. 

Given User choose one of the best deals online
And navigating to Coupons Page
And User choose a Coupon
When User copy the coupon and sign in with Email
Then User is successfully navigated to the store

![](iprice.gif)

##how to run?

pytest Path.py
```
 
pip install -e . 

```