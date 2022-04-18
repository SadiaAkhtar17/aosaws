from faker import Faker
fake = Faker(locale='en_CA')
aos_url = 'https://advantageonlineshopping.com/#/'
aos_title = '\xa0Advantage Shopping'
aos_register_url = 'https://advantageonlineshopping.com/#/register'
username = f'{fake.user_name()[:10]}{fake.pyint(11,99)}'
password = fake.password()[:10]
new_username = fake.user_name()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
city = fake.city()
province = fake.province_abbr()
phone = fake.phone_number()
postalcode = fake.postalcode_in_province()
country = fake.current_country()
new_user_url = 'https://advantageonlineshopping.com/#/myAccount'
address = f'{fake.street_address()}'
address1 = f'{fake.street_address()}, {city}, {fake.province_abbr()}, {fake.current_country()} {postalcode}'
order_number = ""
tracking_number = ""
product_name = ""
order_element = ""
facebook_url = 'https://www.facebook.com/MicroFocus/'
twitter_url = 'https://twitter.com/MicroFocus'
linkedin_url = 'https://www.linkedin.com/company/micro-focus/'
message = fake.sentence(nb_words=20)
orders_url = 'https://advantageonlineshopping.com/#/MyOrders'
