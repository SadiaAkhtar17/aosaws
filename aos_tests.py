import unittest
import aos_methods as methods
import aos_locators as locators


class AOSPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.validate_homepage_texts_links()
        methods.check_main_logo()
        methods.contactus_form()
        methods.create_new_user()
        methods.validate_new_user_created()
        methods.log_out()
        methods.log_in()
        methods.validate_user_login()
        methods.checkout_shoppingcart()
        methods.validate_order_created()
        methods.delete_order()
        methods.delete_account()
        methods.log_in()
        methods.validate_user_account_deleted()
        methods.tearDown()
