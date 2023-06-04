from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument(
    "user-data-dir=	C:/Users/marte/AppData/Local/Google/Chrome/User Data/Profile 1")

driver = webdriver.Chrome(options=options)

url = "https://www.walmart.com/account/login?vid=oaoh"

driver.get(url)
