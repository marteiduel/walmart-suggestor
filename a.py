from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
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
    items = driver.find_element(
        By.XPATH, "//div[@data-testid='category-accordion-Shopped']")
    for item in items:
        product_name = item.find_element(by=By.CLASS_NAME, value="w_V_DM")
        print(product_name)
        time.sleep(300)
        # total_items = [div.get_attribute("class") for div in product_name]
        # print(total_items)


time.sleep(300)
