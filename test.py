text = """
5/29/23, 5:25 PM Order details - Walmart.com
https://www.walmart.com/orders/200011058419487 1/2
Progresso, Italian Style Bread Crumbs, 15 oz. SubstitutionsQty 1 $2.08
Great Value Italian Style Panko Bread Crumbs, 8 oz UnavailableQty 1 $1.77
Navel Oranges, 4 lb Bag Weight-adjustedQty 1 $4.98
Fresh Roma Tomato, Each Weight-adjustedQty 3 $0.86
Spring Valley Vitamin C with Rose Hips Tablets Dietary Supplement, 1,000 mg, 250
CountShoppedQty 1 $9.88
Equate Daily Fiber, 100% Psyllium Husk Dietary Supplement Capsules, 300 CountShoppedQty 1 $10.98
McCormick Garlic Powder, 3.12 oz ShoppedQty 1 $4.23
Breyers Frozen Dairy Dessert Cookies & Cream Ice Cream Alternative, 48 oz ShoppedQty 1 $4.97
Great Value Finely Shredded Fiesta Blend Cheese, 32 oz ShoppedQty 1 $7.48
Great Value Long Grain Enriched Rice, 5 lbs ShoppedQty 2 $5.88
Fresh Green Onions Bunch, Each ShoppedQty 1 $0.88
Great Value Chicken Broth, 32 oz ShoppedQty 2 $2.74May 27, 2023 order
Order# 2000110-58419487
Subtotal $54.96
Free delivery from store  $7.95$0
Tax $2.11
Driver tip $0.00
5/29/23, 5:25 PM Order details - Walmart.com
https://www.walmart.com/orders/200011058419487 2/2Total $57.07
Payment method
 Ending in 9975
"""
import csv
import re

words_for_quantity = ["UnavailableQty", "Weight-adjustedQty", "SubstitutionsQty", "ShoppedQty"]

# Initialize empty list to store extracted data
data = []

# Split the text into lines
lines = text.strip().split("\n")

# Process each line
for line in lines:
    # Check if the line contains the dollar symbol ($) and one of the words
    if "$" in line and any(word in line for word in words_for_quantity):
        # Extract the item name, quantity, and price
        dollar_sign = line.index("$")
        price_match = re.search(r"\d+\.\d{2}", line)
        if price_match:
            price = price_match.group()
        else:
            price = ""

        quantity_place = None
        for word in words_for_quantity:
            if word in line:
                quantity_place = line.index(word)
                break

        if quantity_place is not None:
            quantity_with_word = line[quantity_place:dollar_sign]
            quantity = quantity_with_word.split()[1]

        item_name = line[:quantity_place].strip()

        # Append the extracted data to the list
        data.append([item_name, quantity, price])

# Print the extracted data
for item in data:
    print(f"Item Name: {item[0]}, Quantity: {item[1]}, Price: {item[2]}")

# Save the extracted data to a CSV file
with open("items.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Item Name", "Quantity", "Price"])
    writer.writerows(data)
