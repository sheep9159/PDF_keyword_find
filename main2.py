import os
import shutil


from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def readPdf(dir_and_name, pdf_file, num):

    fp = pdf_file
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)

    doc.initialize()

    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    if 'Airbus' in x.get_text() or 'airbus' in x.get_text():
                        file_origin = dir_and_name
                        file_target = 'result' + '/' + str(num) + '.' + 'pdf'
                        shutil.copyfile(file_origin, file_target)
                        num += 1
                        break

    return num


def file_name(file_dir):

    file_names = []

    for root, dirs, files in os.walk(file_dir, topdown=False):
        for file in files:
            if 'pdf' in file and 'back' not in file and 'front' not in file:
                file_names.append(os.path.join(root, file))

    return file_names


if __name__ == '__main__':

    dir = 'test2'
    num = 0

    for dir_and_name in file_name(dir):
        # print(dir_and_name)
        with open(dir_and_name, 'rb') as pdf_file:
            num = readPdf(dir_and_name, pdf_file, num)

    print('there are {} pdfs in 2018 HCII'.format(num))