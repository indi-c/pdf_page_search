import argparse
import PyPDF2

parser = argparse.ArgumentParser(prog="pdf_page_search", description="Outputs a file listing occurences of a string in a pdf")

parser.add_argument("-f", "--filename", type=str, help="path to the file")

parser.add_argument("-s", --"string", type=str, help="string to search for")

parser.add_argument("-o", "--output", type=str, help="filepath for output")



if __name__ == "__main__":
    pass