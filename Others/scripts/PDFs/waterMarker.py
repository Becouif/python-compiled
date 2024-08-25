

import PyPDF2


# take input argument from command line as much as possible
# inputs = sys.argv[1:]
template = PyPDF2.PdfFileReader(open('result.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('watermark.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_result.pdf', 'wb') as file:
        output.write(file)

