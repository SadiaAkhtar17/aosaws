import sys
import datetime
import aos_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
#s = Service(executable_path='../chromedriver.exe')

#driver = webdriver.Chrome(service=s)

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


def setUp():
    print(f'Advantage Online Shopping test started at: {datetime.datetime.now()}')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://advantageonlineshopping.com/#/')

    if driver.current_url == 'https://advantageonlineshopping.com/#/' and driver.title == '\xa0Advantage Shopping':
        print(f'We\'re at Advantage Online Shopping homepage:  {driver.current_url}')
        print(f'We\'re seeing title message: ', {driver.title})
        print()
    else:
        print(f'We\'re not at the Advantage Shopping homepage. Check your code!')
        driver.close()
        driver.quit()

def tearDown():
    if driver is not None:
        print(f'-------------- AOS TEST ------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

def create_new_user():
    print(f'*-----------------CREATE NEW USER-------------------------*')
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(1)
        if driver.current_url == 'https://advantageonlineshopping.com/#/register':
            driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
            sleep(1)
            driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
            sleep(1)
            driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
            sleep(1)
            driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
            sleep(1)
            driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
            sleep(1)
            driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
            sleep(1)
            driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
            sleep(1)
            Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')
            sleep(1)
            driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
            sleep(1)
            driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
            sleep(1)
            driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
            sleep(1)
            driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postalcode)
            sleep(1)
            driver.find_element(By.NAME, 'i_agree').click()
            sleep(1)
            driver.find_element(By.ID, 'register_btnundefined').click()
            sleep(1)
            print(f'Full name: {locators.full_name}')
            print(f'Address: {locators.address}')
        else:
            print(f'Something went wrong, verify your code')
    else:
        print(f'We are not at the CREATE A NEW ACCOUNT page')


def validate_new_user_created():
    print(f'*------------------- VALIDATE NEW USER CREATED -----------------------*')
    if driver.current_url == locators.aos_url:
        sleep(1)
        if driver.find_element(By.XPATH, f'//a[contains(., "{locators.username}")]'):
            sleep(3)
            print(f'Username: {locators.username} is displayed at Top right Menu.')
            sleep(2)
            print(f'New User account fullname is: {locators.full_name}')
            print(f'New User account address is: {locators.address1}')
            print(f'Expected: New User account with username {locators.username} validated successfully!')
            print()
        else:
            print(f'New user created not validated.')

    else:
        print(f'New User Account not created successfully. Please verify all the required fields (*) are completed.')


def log_in():
    print(f'*------------------- LOG IN ------------------------*')
    if driver.current_url == locators.aos_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(4)
        driver.find_element(By.NAME, 'username').send_keys(locators.username)
        sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(1)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        if driver.current_url == locators.aos_url:
            assert driver.current_url == locators.aos_url
            print(f' We log in with new username and password. \n'f'log in with Username: {locators.username} and password: {locators.password}, name shows at the top right corner of the home page')
        else:
            print(f'Login not successful, please verify you login credentials')


def log_out():
    print(f'*--------------------- LOGOUT -------------------------*')
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(1)
    if driver.current_url == locators.aos_url:
        print(f'Logged out successfully at: {datetime.datetime.now()}')
        sleep(1)
        print()

    else:
        print(f'Unable to log out. Something went wrong.')


def validate_user_login():
    print(f'*---------------- VALIDATE USER LOGIN ----------------------*')
    if driver.current_url == locators.aos_url:
       assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
       print(f'user log in with user name {locators.username}')
       print(f'Expected user: {locators.full_name} login successful')
       sleep(1)
    else:
        print(f'User not login, please verify your code')


def check_main_logo():
    print(f'*------------------- CHECK MAIN LOGO ----------------------*')
    if driver.current_url == locators.aos_url:
        # Validate ADVANTAGE LOGO link
        sleep(1)
        driver.find_element(By.XPATH, '//span[contains(., "dvantage")]').click()
        sleep(1)
        print(f'Top Navigation Menu Link ADVANTAGE LOGO is displayed and clickable.')
        sleep(2)


def contactus_form():
    print(f'*--------------------- CONTACTUS FORM -------------------------*')
    if driver.find_element(By.ID, 'supportCover').is_displayed():
        driver.find_element(By.XPATH, '//select[@name="categoryListboxContactUs"]').send_keys('Tablets')
        sleep(1)
        driver.find_element(By.XPATH, '//select[@name="productListboxContactUs"]').send_keys('HP ElitePad 1000 G2 Tablet')
        sleep(1)
        driver.find_element(By.XPATH, '//input[@name="emailContactUs"]').send_keys(locators.email)
        sleep(1)
    if driver.find_element(By.NAME, 'subjectTextareaContactUs').is_displayed():
#        print('This subject line')
        driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.message)
        sleep(5)
        driver.find_element(By.ID, 'send_btnundefined').click()
        sleep(1)
        print('Thank you for contact us with Advantage support.')
        sleep(1)
        display_btn = driver.find_element(By.XPATH, '//a[@class="a-button ng-binding"]')
        sleep(1)
        print(f'CONTINUE SHOPPING button display feature is : {display_btn.is_displayed()}')
        sleep(1)
        driver.find_element(By.XPATH, '//a[@class="a-button ng-binding"]').click()
        sleep(1)
        print(f'CONTINUE SHOPPING button clickable feature is : {display_btn.is_enabled()}')
        sleep(5)
    else:
        print(f'CONTACT US form is displayed')


def validate_homepage_texts_links():
    print(f'*----------------- VALIDATE HOMEPAGE TEXTS LINKS -------------------*')
    if driver.current_url == locators.aos_url:
        sleep(1)
        assert driver.find_element(By.XPATH, '//span[contains(., "SPEAKERS")]').is_displayed()
        driver.find_element(By.ID, 'speakersTxt').click()
        sleep(2.5)
        driver.back()
        sleep(1.5)
        driver.find_element(By.ID, 'speakersLink').click()
        sleep(2)
        driver.back()
        sleep(1)

        # Validate TABLETS text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//span[contains(., "TABLETS")]').is_displayed()
        driver.find_element(By.ID, 'tabletsTxt').click()
        sleep(2.5)
        driver.back()
        sleep(1.5)
        # Validate the TABLETS 'Shop Now' link is clickable
        driver.find_element(By.ID, 'tabletsLink').click()
        sleep(2)
        print(f'Home page item TABLETS is displayed and clickable. Shop Now link is clickable.')
        driver.back()
        sleep(1)

        # Validate LAPTOPS text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//span[contains(., "LAPTOPS")]').is_displayed()
        driver.find_element(By.ID, 'laptopsTxt').click()
        sleep(2.5)
        driver.back()
        sleep(1.5)
        # Validate the LAPTOPS 'Shop Now' link is clickable
        driver.find_element(By.ID, 'laptopsLink').click()
        sleep(2)
        print(f'Home page item LAPTOPS is displayed and clickable. Shop Now link is clickable.')
        driver.back()
        sleep(1)

        # Validate MICE text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//span[contains(., "MICE")]').is_displayed()
        driver.find_element(By.ID, 'miceTxt').click()
        sleep(2.5)
        driver.back()
        sleep(1.5)
        # Validate the MICE 'Shop Now' link is clickable
        driver.find_element(By.ID, 'miceLink').click()
        sleep(2)
        print(f'Home page item MICE is displayed and clickable. Shop Now link is clickable.')
        driver.back()
        sleep(1)

        # Validate HEADPHONES text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//span[contains(., "HEADPHONES")]').is_displayed()
        driver.find_element(By.ID, 'headphonesTxt').click()
        sleep(2.5)
        driver.back()
        sleep(1.5)
        # Validate the HEADPHONES 'Shop Now' link is clickable
        driver.find_element(By.ID, 'headphonesLink').click()
        sleep(2)
        print(f'Home page item HEADPHONES is displayed and clickable. Shop Now link is clickable.')
        driver.back()
        sleep(1)

        # Validate SPECIAL OFFER text is displayed
        assert driver.find_element(By.XPATH, '//h3[text()="SPECIAL OFFER"]').is_displayed()
        print(f'Home page item SPECIAL OFFER is displayed.')
        sleep(3.5)

        # Validate SEE OFFER text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//button[text()="SEE OFFER"]').is_displayed()
        driver.find_element(By.ID, 'see_offer_btn').click()
        sleep(1.5)
        print(f'Home page item SEE OFFER is displayed and clickable.')
        driver.back()
        driver.refresh()
        sleep(2.5)

        # Validate ALL YOU WANT FROM A TABLET text is displayed
        assert driver.find_element(By.XPATH, '//h2[text()="ALL YOU WANT FROM A TABLET"]').is_displayed()
        print('Home page item "ALL YOU WANT FROM A TABLET" is displayed.')
        driver.refresh()
        sleep(2)

        # Validate EXPLORE NOW text and link are displayed and clickable
        assert driver.find_element(By.XPATH, '//button[text()="EXPLORE NOW"]').is_displayed()
        driver.find_element(By.NAME, 'explore_now_btn').click()
        sleep(2)
        print(f'Home page item EXPLORE NOW is displayed and clickable.')
        driver.back()
        sleep(2)

        # Validate POPULAR ITEMS
        # Popular Item 1
        assert driver.find_element(By.XPATH, '//label[contains(@id, "details_16")]').is_displayed()
        driver.find_element(By.ID, 'details_16').click()
        sleep(2)
        print(f'Home page item POPULAR ITEM 1 is displayed and clickable.')
        driver.back()
        sleep(2)

        # Popular Item 2
        assert driver.find_element(By.XPATH, '//label[contains(@id, "details_10")]').is_displayed()
        driver.find_element(By.ID, 'details_10').click()
        sleep(2)
        print(f'Home page item POPULAR ITEM 2 is displayed and clickable.')
        driver.back()
        sleep(2)

        # Popular Item 3
        assert driver.find_element(By.XPATH, '//label[contains(@id, "details_21")]').is_displayed()
        driver.find_element(By.ID, 'details_21').click()
        sleep(2)
        print(f'Home page item POPULAR ITEM 3 is displayed and clickable.')
        driver.back()
        sleep(2)

        # Validate SOCIAL MEDIA Links
        if driver.find_element(By.XPATH, '//h3[contains(., "FOLLOW US")]').is_displayed():
            for element in driver.find_elements(By.XPATH, "//*[contains(@name, 'follow_')]"):
                sleep(2)
                element_image_name = element.get_attribute('name')
                element.click()
                sleep(2)
                driver.switch_to.window(driver.window_handles[1])
                # Loop through the Social Media Links
                if element_image_name == 'follow_facebook':
                    if driver.current_url == locators.facebook_url:
                        print(f'Social Media Link FACEBOOK homepage is displayed and clickable.')
                    else:
                        print(f'Facebook link is not reachable. Please check your code.')
                elif element_image_name == 'follow_twitter':
                    if driver.current_url == locators.twitter_url:
                        print(f'Social Media Link TWITTER homepage is displayed and clickable.')
                    else:
                        print(f'Twitter link is not reachable. Please check your code.')
                elif element_image_name == 'follow_linkedin':
                    if driver.current_url == locators.linkedin_url:
                        print(f'Social Media Link LINKEDIN homepage is displayed and clickable.')
                    else:
                        print(f'LinkedIn link is not reachable. Please check your code.')
                else:
                    print('Social Media links are not reachable. Please check your code.')
                sleep(2)
                # Close each Social Media tab that is opened
                driver.close()
                sleep(2)
                driver.switch_to.window(driver.window_handles[0])
            print()
        else:
            print(f'The "FOLLOW US" Social Media Links not reachable. Please check the link again.')
    else:
        print(f'Home page links not clickable. please check your code.')


def checkout_shoppingcart():
    print(f'*----------------- CHECKOUT SHOPPINGCART -------------------*')
    if driver.current_url == locators.aos_url:
        driver.get('https://advantageonlineshopping.com/#/product/16')
        sleep(2)
        driver.find_element(By.NAME, 'save_to_cart').click()
        sleep(1)
        driver.find_element(By.ID, 'shoppingCartLink').click()
        sleep(1)
        driver.find_element(By.ID, 'checkOutButton').click()
        sleep(3)
        print(f'We are now on the ORDER PAYMENT and SHIPPING DETAILS page')
        print(f'Order Summary information is displayed')
        print(f'The full name: {locators.full_name} is displayed on the ORDER PAYMENT and SHIPPING DETAILS page')
        driver.find_element(By.ID, 'next_btn').click()
        sleep(5)
        if driver.current_url == 'https://advantageonlineshopping.com/#/orderPayment':
            print(f'We are on the ORDER PAYMENT and PAYMENT METHOD page')
            print(f'Payment information for SafePay username, SafePay password')
            driver.find_element(By.NAME, 'safepay').click()
            sleep(1)
            driver.find_element(By.NAME, 'safepay_username').send_keys(locators.username)
            sleep(1)
            driver.find_element(By.NAME, 'safepay_password').send_keys(locators.password)
            sleep(1)
            driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
            assert driver.find_element(By.XPATH, '//h3[contains(text(), "ORDER PAYMENT")]').is_displayed()
            sleep(1)


def validate_order_created():
    print(f'*----------------- VALIDATE ORDER CREATED -------------------*')
    if driver.current_url == locators.orders_url:
        sleep(1)
        print(f'Order payment done and thank you message are display, "Thank you for buying with Advantage."')
        sleep(1)
        locators.tracking_number = driver.find_element(By.ID, 'trackingNumberLabel').text
        print(f'Tracking number was captured for this order: {locators.tracking_number}')
        locators.order_number = driver.find_element(By.ID, 'orderNumberLabel').text
        print(f'Order Number was captured for this order: {locators.order_number}')
        print(f'Shipping to: {locators.full_name}, Address: {locators.address1}')
        print(f'Phone number is: {locators.phone}')
        print(f'Date and time: {datetime.datetime.now()}')
    else:
        print(f'Order is not validate.')


def delete_order():
    print(f'*----------------- DELETE ORDER -------------------*')
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()
    sleep(1)
    if driver.current_url == 'https://advantageonlineshopping.com/#/MyOrders':
        locators.order_element = driver.find_element(By.XPATH, f'//label[contains(., "{locators.order_number}")]').text
        print(f'The order number is there and matching with the one that captured on the screen: {locators.order_element}')
        sleep(1)
        driver.find_element(By.LINK_TEXT, 'REMOVE').click()
        sleep(1)
        print('Are you sure you want to cancel your order?')
        driver.find_element(By.XPATH, '//*[@id="confBtn_1"]/label[2]').click()
        sleep(1)
        print(' -NO orders-')
        print('user order has been deleted, nothing left in the order list')

    else:
        print(f'Order is not deleted. Check your code.')


def delete_account():
    print(f'*----------------- DELETE ACCOUNT -------------------*')
    sleep(2)
    if driver.current_url == locators.orders_url:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(3)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
        sleep(3)
        # Account details page before deletion
        assert driver.find_element(By.XPATH, f'//label[contains(., "{locators.full_name}")]').is_displayed()
        sleep(4)
        print(f'Account details page for user: "{locators.full_name}" is displayed.')
        assert driver.find_element(By.XPATH, '//button[contains(., "Delete Account")]').is_displayed()
        sleep(2)
        popup = driver.find_element(By.XPATH, '//button[contains(., "Delete Account")]').is_displayed()
        print(f'Delete popup is displayed: {popup}')
        sleep(2)

        # Scroll down to reveal delete button
        driver.execute_script("window.scrollTo(500, 500)")
        sleep(3)

        # Click the Delete Account button
        driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
        sleep(4)

        # Delete Confirmation screen
        assert driver.find_element(By.XPATH, '//*[contains(@class, "deletePopupBtn deleteRed")]').is_displayed()
        sleep(2)
        popup1 = driver.find_element(By.XPATH, '//*[contains(@class, "deletePopupBtn deleteRed")]').is_displayed()
        print(f'Delete Confirmation screen is displayed: {popup1}')
        sleep(2)

        # Confirm deletion of account
        driver.find_element(By.XPATH, '//*[contains(@class, "deletePopupBtn deleteRed")]').click()
        sleep(4)
        print(f'Confirmation message is displayed: Account deleted successfully.')
        print(f'User {locators.full_name} with email address {locators.email} is deleted!')
        print()

    else:
        print(f'User not logged in. Please try logging in again.')


def validate_user_account_deleted():
    print(f'*----------------- VALIDATE USER ACCOUNT DELETED --------------------*')
    if driver.current_url == locators.aos_url:
        print(f'Login Form is displayed --- continue to Login.')
        sleep(3)
        error_text = driver.find_element(By.ID, 'signInResultMessage').text
        sleep(1)
        assert error_text == 'Incorrect user name or password.'
        print(f'Username: {locators.username} and Password: {locators.password} is not found. Error: {error_text}')
        print(f'Test scenario --- Username {locators.username} deleted successfully --- Test Passed!')
        sleep(2)
        print()

    else:
        print(f'Account not deleted.')



# setUp()
# validate_homepage_texts_links()
# check_main_logo()
# contactus_form()
# create_new_user()
# validate_new_user_created()
# log_out()
# log_in()
# validate_user_login()
# checkout_shoppingcart()
# validate_order_created()
# delete_order()
# delete_account()
# log_in()
# validate_user_account_deleted()
# tearDown()

