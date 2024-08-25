import PyPDF2
import sys


# take input argument from command line as much as possible
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('result.pdf')
    merger.close()


pdf_combiner(inputs)


