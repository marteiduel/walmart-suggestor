import csv
import re

pdf_text = """
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

# Define keywords for identifying item lines
keywords = [
    "ShoppedQty",
    "CountShoppedQty",
    "SubstitutionsQty",
    "UnavailableQty",
    "Weight-adjustedQty",
]

# Regular expression patterns
item_line_pattern = r"^(.+?)\s+({})\s+(\d+)\s+\$([\d.]+)$".format("|".join(keywords))
date_pattern = r"\b(\d{1,2}/\d{1,2}/\d{2})\b"

# Initialize empty list to store item data
items = []

# Extract item data from the PDF text
lines = pdf_text.split("\n")
current_date = None

for line in lines:
    line = line.strip()
    if not line:
        continue

    # Extract date from the line
    date_match = re.search(date_pattern, line)
    if date_match:
        current_date = date_match.group(1)
        continue

    # Check if the line represents an item
    item_match = re.match(item_line_pattern, line)
    if item_match:
        item_name = item_match.group(1)
        quantity = item_match.group(3)
        price = item_match.group(4)

        items.append([item_name, quantity, price, current_date])

# Save item data to a CSV file
with open("items.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Item Name", "Quantity", "Price", "Date"])
