import PyPDF2
import glob

# Iterate over PDF files in the directory
pdf_files = glob.glob("*.pdf")

# Open the output text file
with open("printPDF.txt", "w") as output_file:
    for pdf_file in pdf_files:
        # Open each PDF file
        with open(pdf_file, "rb") as file:
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
