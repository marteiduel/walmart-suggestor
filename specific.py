import PyPDF2

# Specify the path of the PDF file to open
pdf_file_path = "5.pdf"

# Open the output text file
with open("5printPDF.txt", "w") as output_file:
    # Open the PDF file
    with open(pdf_file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        line_number = 1
        for page in reader.pages:
            # Extract text from each page
            text = page.extract_text()
            # Split the text into lines
            lines = text.split("\n")
            # Write each line with a line number to the output file
            for line in lines:
                output_file.write(f"{line_number} {line}\n")
                line_number += 1

# Print a message when done
print("Text content extracted and saved to 'printPDF.txt'.")
