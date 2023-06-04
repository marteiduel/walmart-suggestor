import csv
import re
import glob
import PyPDF2

# Define keywords for identifying item lines
keywords = [
    "ShoppedQty",
    "CountShoppedQty",
    "SubstitutionsQty",
    "UnavailableQty",
    "Weight-adjustedQty",
    "Qty"
]

# Regular expression patterns
item_line_pattern = r"^(.+?)\s+({})\s+(\d+)\s+\$([\d.]+)$".format(
    "|".join(keywords))
date_pattern = r"\b(\d{1,2}/\d{1,2}/\d{2})\b"

# Retrieve a list of PDF file paths in the current folder
pdf_files = glob.glob("*.pdf")

# Create a CSV file to consolidate all the results
csv_file = "consolidated_results.csv"
with open(csv_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Item Name", "Quantity", "Price", "Date"])

    # Process each PDF file
    for pdf_file in pdf_files:
        # Read the PDF file and extract text
        with open(pdf_file, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            pdf_text = ""
            for page in reader.pages:
                pdf_text += page.extract_text()

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

                # Append item data to the consolidated CSV file
                writer.writerow([item_name, quantity, price, current_date])

        print(f"Processed {pdf_file} and appended item data to {csv_file}.")

print(f"All PDF files processed. Consolidated results saved to {csv_file}.")
