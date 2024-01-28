import argparse
import PyPDF2
import re

parser = argparse.ArgumentParser(prog="pdf_page_search", description="Outputs a file listing occurences of a string in a pdf")

parser.add_argument("filename", "-f", "--filename", type=str, help="path to the file")

parser.add_argument("search_string", "-s", --"string", type=str, help="string to search for")

parser.add_argument("output", "-o", "--output", type=str, help="filepath for output", default="output.txt")

args = parser.parse_args()

# if (not(args.filename and args.search_string and args.output)):
# may not need validation for this if parsed correctly

reader = PyPDF2.PdfReader(args.filename)

file_len = len(reader.pages)
pages_occurrences = {}

for i in range(file_len):
    pages_occurrences.get(i, len([s.start() for s in re.finditer(args.search_string, reader.pages[i].extract_text())]))

with open(args.output) as output:
    for page, occurrences in pages_occurrences:
        output.write(f"Page: {page}, Occurrences: {occurrences}")
