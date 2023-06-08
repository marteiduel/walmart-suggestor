from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

# Path to your chromedriver executable
chrome_driver_path = 'C:/path/to/chromedriver.exe'

# Specify the path to your Chrome user profile
chrome_profile_path = 'C:/path/to/Chrome/Profile'

chrome_options = Options()
chrome_options.add_argument("user-data-dir=" + chrome_profile_path)

# Additional options if needed
chrome_options.add_argument("start-maximized")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options)

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

for link in links:
    driver.get(link)
    arrow_down = driver.find_element(By.CLASS_NAME, "relative.mr3")
    arrow_down.click()
    accordeon = link.find(
        'div', attrs={'data-testid': 'category-accordion-Shopped'})

products = accordeon.find_all('div', attrs={'class': 'pa3 pb0 ph4-m'})

total_number_of_products = len(products)

for product in products:
    product_name = product.find(
        'div', attrs={'data-testid': "productName"}).text
    product_quantity = product.find(
        'div', attrs={'class': "pt1 f7 f6-m bill-item-quantity gray"}).text
    product_price = product.find('span', attrs={'aria-hidden': "false"}).text
    print(product_name)
    print(product_quantity)
    print(product_price)


time.sleep(300)
