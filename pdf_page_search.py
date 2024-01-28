import argparse
import PyPDF2
import re

parser = argparse.ArgumentParser(prog="pdf_page_search", description="Outputs a file listing occurrences of a string in a pdf")

parser.add_argument("-f", "--filename", metavar="filename", type=str, help="path to the file\n")

parser.add_argument("-s", "--string", metavar="string", type=str, help="string to search for\n")

parser.add_argument("-o", "--output", metavar="output", type=str, help="filepath for output\n", default="output.txt")

parser.add_argument("-x", "--exclude", action="store_false", help="toggle to exclude pages with occurrence 0")

args = parser.parse_args()

if (not(args.filename and args.string and args.output)):
    raise ValueError("invalid args, please run the program with -h for help")

reader = PyPDF2.PdfReader(args.filename)

file_len = len(reader.pages)
pages_occurrences = {}

for i in range(file_len):
    occurrences = len([s.start() for s in re.finditer(args.string, reader.pages[i].extract_text())])
    if occurrences or args.exclude:
        pages_occurrences.setdefault(str(i + 1), occurrences)

with open(args.output, "w+", encoding="utf-8") as output:
    for page, occurrences in pages_occurrences.items():
        output.write(f"Page: {page}, Occurrences: {occurrences}\n")
