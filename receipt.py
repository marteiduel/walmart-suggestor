from bs4 import BeautifulSoup


with open('page.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

accordeon = soup.find('div', attrs={'data-testid': 'category-accordion-Shopped'})

products = accordeon.find_all('div', attrs={'class': 'pa3 pb0 ph4-m'})

total_number_of_products = len(products)

for product in products :
    product_name = product.find('div', attrs={'data-testid':"productName"}).text
    product_quantity = product.find('div', attrs={'class':"pt1 f7 f6-m bill-item-quantity gray"}).text
    product_price = product.find('span', attrs={'aria-hidden':"false"}).text
    print(product_name)
    print(product_quantity)
    print(product_price)