import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Path to your chromedriver executable
chrome_driver_path = 'C:/path/to/chromedriver.exe'

# Specify the path to your Chrome user profile
chrome_profile_path = 'C:/path/to/Chrome/Profile'

chrome_options = Options()
chrome_options.add_argument("user-data-dir=" + chrome_profile_path)
chrome_options.add_argument("start-maximized")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.walmart.com/account/login?vid=oaoh"

driver.get(url)

email = driver.find_element(By.CLASS_NAME, "w_ZjHt")
email.send_keys("")  # Enter your email here

continue_button = driver.find_element(By.CLASS_NAME, "w_hhLG")
continue_button.click()

time.sleep(2.5)

password = driver.find_element(By.ID, "react-aria-1")
password.send_keys("")  # Enter your password here

login_button = driver.find_element(
    By.XPATH, "//button[contains(text(), 'Sign In')]")
login_button.click()

time.sleep(2.5)

driver.get("https://www.walmart.com/orders")

view_details_buttons = driver.find_elements(
    By.XPATH, "//a[contains(text(), 'View details')]")

links = [button.get_attribute("href") for button in view_details_buttons]

product_list = []

for link in links:
    time.sleep(1)
    driver.get(link)
    time.sleep(1)
    date = driver.find_element(
        By.XPATH, '//h1[@class="w_kV33 w_LD4J w_mvVb f3 f-subheadline-m di-m dark-gray-m print-bill-date lh-copy"]').text
    print(date)
    arrow_down = driver.find_element(By.CLASS_NAME, "relative.mr3")
    arrow_down.click()
    try:
        accordeon = driver.find_element(
            By.XPATH, '//div[@data-testid="category-accordion-Shopped"]')
        products = accordeon.find_elements(
            By.XPATH, '//div[contains(@class, "pa3 pb0 ph4-m")]')
        time.sleep(1)
        for product in products:
            try:
                product_name = product.find_element(
                    By.XPATH, './/div[@data-testid="productName"]').text
                product_quantity = product.find_element(
                    By.XPATH, './/div[@class="pt1 f7 f6-m bill-item-quantity gray"]').text
                product_price = product.find_element(
                    By.XPATH, './/span[@aria-hidden="false"]').text
                print(product_name)
                print(product_quantity)
                print(product_price)
                product_data = {
                    "name": product_name,
                    "quantity": product_quantity,
                    "price": product_price,
                    "date": date
                }

                product_list.append(product_data)

            except NoSuchElementException:
                print("Some elements not found for the current product.")
                continue

    except NoSuchElementException:
        print("Accordion element not found for the current link.")
        continue

with open("raw_product_list.json", "w") as file:
    json.dump(product_list, file, indent=4)
